#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Lab harness. Reports artifacts on disk, not claims of understanding."""
import json, sys, tomllib
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
STATE = ROOT / ".ci-lab" / "progress.json"
MANIFEST = ROOT / "labs" / "manifest.toml"


def load():
    m = tomllib.loads(MANIFEST.read_text())
    s = json.loads(STATE.read_text()) if STATE.exists() else {
        "current": m["phases"][0]["id"], "completed": []}
    return m, s


def save(s):
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(s, indent=2) + "\n")


def phase(m, pid):
    for p in m["phases"]:
        if p["id"] == pid:
            return p
    sys.exit(f"no phase {pid}")


def missing(p):
    return [r for r in p["required"] if not (ROOT / r).exists()]


def status(m, s):
    print(f"\n{m['title']}\n")
    for p in m["phases"]:
        gone = missing(p)
        if p["id"] in s["completed"]:
            mark, note = "[x]", "done"
        elif p["id"] == s["current"]:
            mark, note = "[>]", f"{len(p['required']) - len(gone)}/{len(p['required'])} artifacts"
        else:
            mark, note = "[ ]", ""
        print(f" {mark} {p['id']} {p['slug']:<32} {note}")
    print(f"\n {len(s['completed'])}/{len(m['phases'])} phases. Open progress.html for the full view.\n")


def check(m, s, pid):
    p = phase(m, pid)
    gone = missing(p)
    if gone:
        print(f"\nPhase {pid} not complete. Missing:")
        for g in gone:
            print(f"  - {g}")
        print("\nThese are files you create. The harness cannot create them for you.\n")
        return False
    if pid not in s["completed"]:
        s["completed"].append(pid)
        s["completed"].sort()
    save(s)
    print(f"\nPhase {pid} checked. All {len(p['required'])} artifacts present.\n")
    return True


def nxt(m, s):
    ids = [p["id"] for p in m["phases"]]
    todo = [i for i in ids if i not in s["completed"]]
    if not todo:
        print("\nAll phases complete. Read challenge/README.md.\n")
        return
    p = phase(m, todo[0])
    s["current"] = p["id"]
    save(s)
    show(m, s, p["id"])


def show(m, s, pid):
    p = phase(m, pid)
    print(f"\n{p['id']}  {p['title']}   (~{p['minutes']} min)")
    print(f"\n  {p['question']}\n")
    print(f"  Read   labs/{p['id']}-{p['slug']}/README.md")
    print(f"  Do     labs/{p['id']}-{p['slug']}/TASK.md")
    print("\n  Artifacts for this phase:")
    for r in p["required"]:
        print(f"    {'x' if (ROOT / r).exists() else ' '}  {r}")
    print()


def doctor(m, s):
    ok = True
    for path in [MANIFEST, ROOT / "AI_USE.md", ROOT / "AGENTS.md", ROOT / "README.md"]:
        if not path.exists():
            print(f"missing: {path.relative_to(ROOT)}")
            ok = False
    for p in m["phases"]:
        d = ROOT / "labs" / f"{p['id']}-{p['slug']}"
        for f in ["README.md", "TASK.md", "TROUBLESHOOTING.md", "expected/REFERENCE.md"]:
            if not (d / f).exists():
                print(f"missing: {d.relative_to(ROOT)}/{f}")
                ok = False
    print("\nharness ok\n" if ok else "\nharness incomplete\n")
    return ok


ROW = """<tr class="{cls}"><td class="id">{id}</td><td><b>{title}</b><div class=q>{q}</div>
<div class=art>{arts}</div></td><td class=st>{st}</td></tr>"""


def progress_html(m, s):
    rows, done_arts, all_arts = [], 0, 0
    for p in m["phases"]:
        gone = missing(p)
        done_arts += len(p["required"]) - len(gone)
        all_arts += len(p["required"])
        st = "done" if p["id"] in s["completed"] else (
            "current" if p["id"] == s["current"] else "todo")
        arts = "".join(
            f'<span class="a {"y" if (ROOT / r).exists() else "n"}">{r}</span>' for r in p["required"])
        st_txt = {"done": "complete", "current": "in progress", "todo": "not started"}[st]
        rows.append(ROW.format(cls=st, id=p["id"], title=p["title"], q=p["question"],
                               arts=arts, st=st_txt))
    pct = round(100 * done_arts / all_arts) if all_arts else 0
    (ROOT / "progress.html").write_text(HTML.format(
        title=m["title"], pct=pct, done=len(s["completed"]), total=len(m["phases"]),
        arts=f"{done_arts}/{all_arts}",
        rows="\n".join(rows), today=date.today().isoformat()))
    print(f"\nwrote progress.html  —  {pct}% of artifacts, {len(s['completed'])}/{len(m['phases'])} phases\n")


HTML = """<!doctype html><meta charset=utf-8><title>{title}</title>
<style>
:root{{--bg:#fbfbf9;--fg:#1a1a1a;--dim:#767676;--line:#e2e0da;--ok:#2f6f4f;--now:#8a5a12;--card:#fff}}
@media(prefers-color-scheme:dark){{:root{{--bg:#141414;--fg:#e8e6e1;--dim:#8f8d88;--line:#2c2c2c;--ok:#6fbf95;--now:#d3a350;--card:#1c1c1c}}}}
*{{box-sizing:border-box}}
body{{margin:0;padding:3rem 1.25rem;background:var(--bg);color:var(--fg);
font:15px/1.55 ui-sans-serif,-apple-system,Segoe UI,sans-serif}}
main{{max-width:60rem;margin:0 auto}}
h1{{font-size:1.5rem;font-weight:600;margin:0 0 .3rem}}
.sub{{color:var(--dim);margin:0 0 2rem;font-size:.9rem}}
.bar{{height:8px;background:var(--line);border-radius:99px;overflow:hidden;margin:.6rem 0 .4rem}}
.bar i{{display:block;height:100%;width:{pct}%;background:var(--ok)}}
.kpis{{display:flex;gap:2.5rem;flex-wrap:wrap;margin-bottom:2rem}}
.kpi b{{display:block;font-size:1.6rem;font-weight:600;line-height:1.2}}
.kpi span{{color:var(--dim);font-size:.8rem}}
table{{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:8px}}
td{{padding:.85rem .9rem;border-top:1px solid var(--line);vertical-align:top}}
tr:first-child td{{border-top:0}}
.id{{font-variant-numeric:tabular-nums;color:var(--dim);width:2.5rem}}
.q{{color:var(--dim);font-size:.86rem;margin-top:.15rem}}
.st{{white-space:nowrap;font-size:.8rem;color:var(--dim);text-align:right}}
.art{{margin-top:.5rem;display:flex;flex-wrap:wrap;gap:.3rem}}
.a{{font:11px/1.4 ui-monospace,monospace;padding:.15rem .4rem;border-radius:4px;
border:1px solid var(--line);color:var(--dim)}}
.a.y{{color:var(--ok);border-color:var(--ok)}}
tr.done .id,tr.done .st{{color:var(--ok)}}
tr.current{{background:color-mix(in srgb,var(--now) 8%,transparent)}}
tr.current .id,tr.current .st{{color:var(--now)}}
footer{{color:var(--dim);font-size:.78rem;margin-top:1.5rem}}
</style>
<main>
<h1>{title}</h1>
<p class=sub>Progress is measured by artifacts that exist on disk, not by phases you say you finished.</p>
<div class=bar><i></i></div>
<div class=kpis>
<div class=kpi><b>{pct}%</b><span>artifacts built</span></div>
<div class=kpi><b>{done}/{total}</b><span>phases checked</span></div>
<div class=kpi><b>{arts}</b><span>files</span></div>
</div>
<table>{rows}</table>
<footer>Regenerate with <code>uv run lab.py progress</code> · {today}</footer>
</main>
"""


def main():
    argv = sys.argv[1:] or ["status"]
    cmd, rest = argv[0], argv[1:]
    m, s = load()
    if cmd == "doctor":
        doctor(m, s)
    elif cmd == "status":
        status(m, s)
    elif cmd == "show":
        show(m, s, rest[0])
    elif cmd == "check":
        check(m, s, rest[0])
    elif cmd == "next":
        nxt(m, s)
    elif cmd == "progress":
        pass
    else:
        sys.exit("usage: lab.py doctor|status|show NN|check NN|next|progress")
    progress_html(m, s)


if __name__ == "__main__":
    main()
