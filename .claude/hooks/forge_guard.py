"""PreToolUse guard for the Forge art pipeline (see CLAUDE.md and art/raccoon-style-guide.md).

Blocks, for every session and agent:
  * running any art/tools script except forge_jobs.py and the read-only checkers
  * calling Forge's generate endpoints directly, which would skip the pipeline's gates
  * inline image code that writes files (PIL / OpenCV / imageio / scikit-image with a save call)
  * editing a job's state.json by hand (only forge_jobs.py writes it)
  * editing the approved models list (only Josh edits it, by hand)
  * writing a prompt review unless you are the forge-prompt-reviewer agent
Blocks, for any agent (main session excepted):
  * forge_jobs.py approve / verdict / respond / status / lock, which record Josh's or Claude's decisions

Reads the hook input as JSON on stdin; prints a deny decision as JSON, or nothing to allow.
"""
import json, re, sys

ALLOWED_TOOLS = {"forge_jobs.py", "measure_head.py", "line_width.py", "check_tail.py"}
DECISIONS = ("approve", "verdict", "respond", "status", "lock")
REVIEWER = "forge-prompt-reviewer"


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                             "permissionDecisionReason": f"Forge pipeline guard: {reason}"}}))
    sys.exit(0)


def check_shell(cmd, agent):
    c = cmd.replace("\\", "/")
    for name in set(re.findall(r"([\w-]+\.py)\b", c)):
        if name not in ALLOWED_TOOLS and _is_art_tool(name):
            deny(f"{name} is an old script that edits pixels or calls Forge outside the pipeline. "
                 "Every image change is a Forge job: py art/tools/forge_jobs.py ...")
    if re.search(r"(7860|/sdapi/)", c) and re.search(r"(txt2img|img2img|extra-single-image|extra-batch-images)", c):
        deny("calling Forge's generate endpoints directly skips the pipeline. Make a job with forge_jobs.py.")
    if re.search(r"\b(PIL|cv2|imageio|skimage)\b", c) and re.search(r"(\.save\(|imwrite|imsave)", c):
        deny("inline code that writes images is a pixel edit. Change the image through a Forge job instead.")
    if agent and re.search(r"forge_jobs\.py\S*\s+(" + "|".join(DECISIONS) + r")\b", c):
        deny(f"agents can't run approve, verdict, respond, status or lock. Those record Josh's or Claude's "
             "decisions and run only in the main session. Report back instead.")
    writes_state = (r">>?\s*['\"]?[^\s|;&]*state\.json",                       # echo x > .../state.json
                    r"\bsed\s+-i[^|;&]*state\.json",                              # sed -i ... state.json
                    r"\b(Set-Content|Add-Content|Out-File)\b[^|;]*state\.json",   # PowerShell writes
                    r"\b(cp|mv|copy|move|Copy-Item|Move-Item)\b[^|;&]*state\.json",
                    r"state\.json['\"]?\)?\s*\.write_(text|bytes)",               # Path(...state.json).write_text
                    r"open\([^)]*state\.json[^)]*,\s*['\"][wa]")                  # open(".../state.json", "w")
    if any(re.search(rx, c) for rx in writes_state):
        deny("state.json is written only by forge_jobs.py commands.")


def _is_art_tool(name):
    import pathlib
    return (pathlib.Path(__file__).resolve().parents[2] / "art" / "tools" / name).exists()


def check_write(path, agent):
    p = path.replace("\\", "/").lower()
    if re.search(r"art/jobs/[^/]+/state\.json$", p):
        deny("state.json is written only by forge_jobs.py commands.")
    if p.endswith("art/asset-status.json"):
        deny("image status is set only through forge_jobs.py status and lock.")
    if "art/locked/" in p:
        deny("locked images are never changed. A change is a new job with the locked copy as its parent.")
    if p.endswith("art/tools/forge-approved.json"):
        deny("only Josh edits the approved models list. Tell him what you'd add and why.")
    if re.search(r"art/jobs/[^/]+/prompt-review[^/]*\.md$", p) and agent != REVIEWER:
        deny("only the forge-prompt-reviewer agent writes prompt reviews, so every review stays independent.")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    tool, inp = data.get("tool_name", ""), data.get("tool_input", {}) or {}
    agent = data.get("agent_type") or None
    if tool in ("Bash", "PowerShell"):
        check_shell(inp.get("command", ""), agent)
    elif tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        check_write(inp.get("file_path") or inp.get("notebook_path") or "", agent)


if __name__ == "__main__":
    main()
