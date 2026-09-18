"""Reference driver: runs a skill on a system with any model API, or hands the prompt to another runtime.

    python okf/agents/runner.py prompt  <skill> --system <slug> [--code <code>]      # write the prompt bundle, no model call
    python okf/agents/runner.py run     <skill> --system <slug> [--code <code>]      # call the model, apply the result
    python okf/agents/runner.py apply   <skill> --system <slug> [--code <code>] --result <file.json>
    python okf/agents/runner.py critique --system <slug> [--compare <slug> ...]      # rule critics only, no model

A skill is ``okf/skills/<skill>/SKILL.md`` (instructions) plus
``okf/agents/manifests/<skill>.json`` (which nodes to read, the output JSON
schema, which apply function to call). ``prompt`` writes
``systems/<slug>/_runs/<skill>[-<code>]/prompt.md`` and ``schema.json`` so a
person, a Claude Code agent or any other runtime can produce ``result.json``
and feed it to ``apply``. ``run`` does the same through the Anthropic API.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "okf" / "tools"))

from rocky import OKF_ROOT, okf, system, apply  # noqa: E402

# skills and manifests are code assets of the repository; the knowledge base (OKF_ROOT) may live elsewhere
SKILLS = HERE.parent / "skills"
MANIFESTS = HERE / "manifests"
DEFAULT_MODEL = "claude-opus-5"


def load_skill(name: str) -> tuple[dict, str, dict]:
    node = okf.read_node(SKILLS / name / "SKILL.md")
    manifest = json.loads((MANIFESTS / f"{name}.json").read_text(encoding="utf-8"))
    return node.front, node.body, manifest


def _read(path: Path, cap: int = 12000) -> str:
    text = Path(path).read_text(encoding="utf-8")
    return text if len(text) <= cap else text[:cap] + "\n…(truncated)"


def _class_node_path(slug: str, code: str) -> Path:
    return system.class_path(slug, code)


def gather_context(manifest: dict, slug: str, code: str | None, exclude_system: str = "") -> list[tuple[str, str]]:
    """(label, text) pairs in the order the manifest lists them."""
    ctx: list[tuple[str, str]] = []
    sysdir = system.system_dir(slug)
    for item in manifest.get("reads", []):
        kind = item["kind"]
        if kind == "node":
            p = OKF_ROOT / item["path"].format(system=slug, code=system.slugify(code or ""))
            if p.exists():
                ctx.append((item["path"], _read(p)))
        elif kind == "system":
            ctx.append(("SYSTEM.md", _read(sysdir / "SYSTEM.md")))
        elif kind == "class":
            if code:
                ctx.append((f"class {code}", _read(_class_node_path(slug, code))))
        elif kind == "siblings":
            rows = []
            for n in system.list_classes(slug):
                f = n.front
                rows.append(f"- {f.get('code','')} | {f.get('name','')} | parent {f.get('parent_code','') or '-'} | status {f.get('status','')} | elements {', '.join(f.get('element_refs') or []) or '-'}")
            ctx.append(("all classes of this system (code | name | parent | status | elements)", "\n".join(rows)))
        elif kind == "all_class_nodes":
            parts = []
            for n in system.list_classes(slug):
                parts.append(_read(n.path, item.get("cap", 3000)))
            ctx.append(("class nodes", "\n\n---\n\n".join(parts)))
        elif kind == "framing_nodes":
            d = sysdir / "framing"
            if d.exists():
                ctx.append(("framing nodes", "\n\n---\n\n".join(_read(p, 3000) for p in sorted(d.glob("*.md")))))
        elif kind == "ingest_blocks":
            p = sysdir / "_ingest" / "blocks.json"
            if p.exists():
                blocks = json.loads(p.read_text(encoding="utf-8"))
                text = "\n".join(f"[{b.get('kind')}{' p' + str(b['page']) if b.get('page') else ''}{' r' + str(b['row']) if b.get('row') else ''}] {b.get('text')}" for b in blocks)
                ctx.append(("source document blocks", text[: item.get("cap", 60000)]))
        elif kind == "nearest_examples":
            if code:
                from nearest_examples import nearest  # okf/tools
                n = system.read_class(slug, code)
                q = f"{n.front.get('name','')} {n.body.split('## Decomposition')[0]}"
                hits = nearest(q, item.get("k", 3), True, exclude_system or item.get("exclude_system", ""))
                for h in hits:
                    ctx.append((f"nearest registry example {h['id']} (score {h['score']})", _read(REPO / h["path"], 5000)))
        elif kind == "vocab_index":
            ctx.append(("vocabulary: elements", _read(OKF_ROOT / "vocab" / "elements" / "INDEX.md")))
            ctx.append(("vocabulary: characteristics", _read(OKF_ROOT / "vocab" / "characteristics" / "INDEX.md")))
        elif kind == "vocab_types":
            # the vocab pages for element types the sibling classes already use, plus the common ones
            refs = set(item.get("always", []))
            for n in system.list_classes(slug):
                refs.update(n.front.get("element_refs") or [])
            for ref in sorted(refs):
                p = OKF_ROOT / "vocab" / "elements" / f"{ref}.md"
                if p.exists():
                    ctx.append((f"vocab {ref}", _read(p, 4000)))
        elif kind == "table":
            p = sysdir / "elements.csv"
            if p.exists():
                ctx.append(("elements.csv", _read(p, item.get("cap", 40000))))
        elif kind == "attention_rules":
            p = OKF_ROOT / "attention" / f"{slug}.json"
            if p.exists():
                ctx.append(("rule-based attention items already found", _read(p, 20000)))
    return ctx


def build_prompt(name: str, slug: str, code: str | None, exclude_system: str = "") -> tuple[str, str, dict, dict]:
    front, body, manifest = load_skill(name)
    ctx = gather_context(manifest, slug, code, exclude_system)
    header = (f"You are running the skill `{name}` of Rocky, the land cover classification knowledge base, on the classification system `{slug}`"
              + (f", class `{code}`" if code else "") + ".\n\n"
              "Follow the instructions below exactly. Answer only with JSON matching the output schema. "
              "Never invent thresholds; leave unknown ranges null and say so in open_questions. "
              "Cite evidence as short verbatim quotes from the context.\n\n")
    parts = [header, "# Skill instructions\n\n" + body.strip() + "\n"]
    for label, text in ctx:
        parts.append(f"\n\n# Context: {label}\n\n{text}")
    user = "\n".join(parts)
    sysmsg = front.get("system_prompt") or "You are a land cover classification specialist who knows ISO 19144-2 LCML and FAO's LCCS3/LChS formats."
    return sysmsg, user, manifest["output_schema"], manifest


def run_dir(slug: str, name: str, code: str | None) -> Path:
    d = system.system_dir(slug) / "_runs" / (name + (f"-{system.slugify(code)}" if code else ""))
    d.mkdir(parents=True, exist_ok=True)
    return d


def cmd_prompt(a) -> dict:
    sysmsg, user, schema, manifest = build_prompt(a.skill, a.system, a.code, getattr(a, "exclude_system", ""))
    d = run_dir(a.system, a.skill, a.code)
    (d / "prompt.md").write_text(f"<!-- system prompt -->\n{sysmsg}\n\n<!-- user prompt -->\n{user}\n", encoding="utf-8", newline="\n")
    (d / "schema.json").write_text(json.dumps(schema, indent=1) + "\n", encoding="utf-8", newline="\n")
    return {"ok": True, "prompt": str(d / "prompt.md"), "schema": str(d / "schema.json"),
            "chars": len(user), "apply_with": f"python okf/agents/runner.py apply {a.skill} --system {a.system}"
            + (f" --code {a.code}" if a.code else "") + f" --result {d / 'result.json'}"}


def cmd_run(a) -> dict:
    import anthropic
    sysmsg, user, schema, manifest = build_prompt(a.skill, a.system, a.code, getattr(a, "exclude_system", ""))
    client = anthropic.Anthropic()
    kwargs = dict(model=a.model, max_tokens=a.max_tokens,
                  system=[{"type": "text", "text": sysmsg, "cache_control": {"type": "ephemeral"}}],
                  messages=[{"role": "user", "content": user}],
                  thinking={"type": "adaptive"},
                  output_config={"effort": a.effort, "format": {"type": "json_schema", "schema": schema}})
    d = run_dir(a.system, a.skill, a.code)
    if a.fallbacks:
        # server-side refusal fallbacks (routes by refusal category); dropped if the endpoint rejects it
        try:
            with client.beta.messages.stream(betas=["server-side-fallback-2026-07-01"], fallbacks="default", **kwargs) as s:
                msg = s.get_final_message()
        except anthropic.BadRequestError as e:
            if "fallback" not in str(e).lower():
                raise
            with client.messages.stream(**kwargs) as s:
                msg = s.get_final_message()
    else:
        with client.messages.stream(**kwargs) as s:
            msg = s.get_final_message()
    if msg.stop_reason == "refusal":
        return {"ok": False, "error": "model refused", "stop_details": getattr(msg, "stop_details", None)}
    text = next(b.text for b in msg.content if b.type == "text")
    result = json.loads(text)
    (d / "result.json").write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    (d / "usage.json").write_text(json.dumps({"model": msg.model, "usage": msg.usage.to_dict(), "at": datetime.now(timezone.utc).isoformat()}, indent=1) + "\n", encoding="utf-8")
    rep = apply_result(a.skill, a.system, a.code, result)
    rep["usage"] = msg.usage.to_dict()
    return rep


def apply_result(name: str, slug: str, code: str | None, result: dict) -> dict:
    if name == "ingest-classification":
        rep = apply.apply_ingest(slug, result)
    elif name == "decompose-class":
        rep = apply.apply_decompose(slug, code, result)
    elif name == "extract-framing":
        rep = apply.apply_framing(slug, result)
    elif name == "critique-system":
        rep = apply.apply_critique(slug, result)
    else:
        raise SystemExit(f"no apply step for skill {name}")
    rep["ok"] = True
    rep["skill"] = name
    return rep


def cmd_apply(a) -> dict:
    result = json.loads(Path(a.result).read_text(encoding="utf-8"))
    return apply_result(a.skill, a.system, a.code, result)


def cmd_critique(a) -> dict:
    rep = apply.apply_critique(a.system, None, a.compare or [])
    rep["ok"] = True
    return rep


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for c in ("prompt", "run", "apply"):
        p = sub.add_parser(c)
        p.add_argument("skill")
        p.add_argument("--system", required=True)
        p.add_argument("--code", default=None)
        p.add_argument("--exclude-system", dest="exclude_system", default="",
                       help="registry id to leave out of nearest-example retrieval (leave-one-out evaluation)")
        if c == "run":
            p.add_argument("--model", default=DEFAULT_MODEL)
            p.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
            p.add_argument("--max-tokens", type=int, default=64000)
            p.add_argument("--no-fallbacks", dest="fallbacks", action="store_false")
        if c == "apply":
            p.add_argument("--result", required=True)
    p = sub.add_parser("critique")
    p.add_argument("--system", required=True)
    p.add_argument("--compare", nargs="*", default=[])
    a = ap.parse_args()
    rep = {"prompt": cmd_prompt, "run": cmd_run, "apply": cmd_apply, "critique": cmd_critique}[a.cmd](a)
    print(json.dumps(rep, indent=1, ensure_ascii=False, default=str))
    sys.exit(0 if rep.get("ok") else 1)


if __name__ == "__main__":
    main()
