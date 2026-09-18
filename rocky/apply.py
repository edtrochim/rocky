"""Apply a skill's structured result to the OKF folder, deterministically.

Skills produce JSON that matches the schema in their manifest; these functions
turn that JSON into nodes and rows. They are the only writers a skill has, so
a skill can never write an arbitrary file. Each returns a small report.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from . import OKF_ROOT, okf, system, critics, validate
from .table import Table

ATTENTION = OKF_ROOT / "attention"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _classes_of(slug: str) -> list[dict]:
    out = []
    for n in system.list_classes(slug):
        f = n.front
        definition = ""
        if "## Definition (verbatim)" in n.body:
            definition = n.body.split("## Definition (verbatim)", 1)[1].split("\n## ", 1)[0].strip()
        out.append({"class_id": f.get("class_id") or f.get("code"), "code": f.get("code", ""), "name": f.get("name", ""),
                    "definition": definition if not definition.startswith("_titles only") else "",
                    "parent_code": f.get("parent_code", ""), "status": f.get("status", ""), "colour": f.get("colour", ""),
                    "language": f.get("definition_language", ""), "source_span": f.get("source_span", ""),
                    "land_use_hint": f.get("land_use_hint", ""), "nearest_examples": f.get("nearest_examples", []),
                    "open_questions": f.get("open_questions", []), "confidence": f.get("confidence", ""),
                    "framing": [l["id"] for l in f.get("links", []) if l.get("rel") in ("motivated_by", "named_by")]})
    return out


def _record_run(slug: str, skill: str, note: str) -> None:
    meta = system.read_system(slug)
    hist = list(meta.get("run_history") or [])
    hist.append({"skill": skill, "at": _now(), "note": note})
    meta["run_history"] = hist
    classes = _classes_of(slug)
    m = {k: meta.get(k, "") for k in ("name", "publisher", "version", "jurisdiction", "language", "mode", "sources")}
    m["run_history"] = hist
    m["title"] = meta.get("title")
    m["name"] = meta.get("title") or meta.get("name")
    sys_node = okf.read_node(system.system_dir(slug) / "SYSTEM.md")
    for key in ("## Scope statement (verbatim)", "## Notes", "## Framing summary"):
        if key in sys_node.body:
            sect = sys_node.body.split(key, 1)[1].split("\n## ", 1)[0].strip()
            m[{"## Scope statement (verbatim)": "scope_statement", "## Notes": "notes", "## Framing summary": "framing_summary"}[key]] = \
                "" if sect.startswith("_") else sect
    system.write_system(slug, m, classes)


# ------------------------------------------------------------- ingest
def apply_ingest(slug: str, result: dict) -> dict:
    """result: {system: {name, publisher, version, jurisdiction, language, scope_statement},
                classes: [{code, name, definition, parent_code, colour, language, source_span}]}"""
    meta = system.read_system(slug) if (system.system_dir(slug) / "SYSTEM.md").exists() else {}
    sysd = result.get("system") or {}
    m = {"name": sysd.get("name") or meta.get("title") or slug, "publisher": sysd.get("publisher") or meta.get("publisher", ""),
         "version": sysd.get("version") or meta.get("version", ""), "jurisdiction": sysd.get("jurisdiction") or meta.get("jurisdiction", ""),
         "language": sysd.get("language") or meta.get("language", ""), "scope_statement": sysd.get("scope_statement", ""),
         "mode": meta.get("mode", "propose"), "sources": meta.get("sources", []), "run_history": meta.get("run_history", [])}
    t = system.load_table(slug)
    classes = []
    for c in result.get("classes") or []:
        cid = c.get("code") or system.slugify(c.get("name", ""))
        cls = {"class_id": cid, "code": c.get("code", ""), "name": c.get("name", ""), "definition": c.get("definition", ""),
               "parent_code": c.get("parent_code", ""), "colour": c.get("colour", ""), "language": c.get("language", ""),
               "source_span": c.get("source_span", ""), "status": "titles_only"}
        classes.append(cls)
        rows = system.rows_from_proposal(slug, cid, cls["code"], cls["name"], {"definition": cls["definition"], "patterns": []})
        t = system.replace_class_rows(t, cid, rows)
    system.write_system(slug, m, classes)
    for cls in classes:
        system.write_class(slug, cls, None)
    system.save_table(slug, t)
    _record_run(slug, "ingest-classification", f"{len(classes)} classes")
    return {"classes": len(classes)}


# --------------------------------------------------------- decompose
def apply_decompose(slug: str, code: str, result: dict) -> dict:
    """result: {rationale, confidence, land_use_hint, open_questions, nearest_examples, examples_note,
                evidence: [{row_path, quote}], patterns: [...] (see system.rows_from_proposal)}"""
    node = system.read_class(slug, code)
    f = node.front
    cid = f.get("class_id") or f.get("code")
    t = system.load_table(slug)
    before = Table(rows=list(t.for_class(cid)))
    definition = node.body.split("## Definition (verbatim)", 1)[1].split("\n## ", 1)[0].strip() if "## Definition (verbatim)" in node.body else ""
    rows = system.rows_from_proposal(slug, cid, f.get("code", ""), f.get("name", ""),
                                     {"definition": "" if definition.startswith("_titles only") else definition,
                                      "patterns": result.get("patterns") or []})
    t2 = system.replace_class_rows(t, cid, rows)
    findings = [x for x in validate.validate(Table(rows=t2.for_class(cid), meta=t2.meta)) if x["level"] == "error"]
    cls = {**{k: f.get(k, "") for k in ("code", "name", "parent_code", "colour", "source_span")},
           "class_id": cid, "definition": "" if definition.startswith("_titles only") else definition,
           "language": f.get("definition_language", ""), "status": result.get("status") or "proposed",
           "rationale": result.get("rationale", ""), "evidence": result.get("evidence", []),
           "open_questions": list(result.get("open_questions") or []) + [f"validator: {x['message']}" for x in findings[:5]],
           "confidence": result.get("confidence", ""), "land_use_hint": result.get("land_use_hint", ""),
           "nearest_examples": result.get("nearest_examples", []), "examples_note": result.get("examples_note", ""),
           "framing": [l["id"] for l in f.get("links", []) if l.get("rel") in ("motivated_by", "named_by")]}
    system.write_class(slug, cls, t2)
    system.save_table(slug, t2)
    from .table import diff
    d = diff(before, Table(rows=t2.for_class(cid)))
    _record_run(slug, "decompose-class", f"{code}: {len(rows)} rows, {len(findings)} validator errors")
    return {"class": code, "rows": len(rows), "validator_errors": [x["message"] for x in findings],
            "diff": {k: len(v) for k, v in d.items()}}


# ----------------------------------------------------------- framing
def apply_framing(slug: str, result: dict) -> dict:
    """result: {summary, instruments: [{id, title, institution, instrument_type, jurisdiction, year,
                effect_on_classes, evidence, classes: [codes]}]}"""
    d = system.system_dir(slug) / "framing"
    d.mkdir(parents=True, exist_ok=True)
    sys_path = system.system_dir(slug) / "SYSTEM.md"
    by_class: dict[str, list[str]] = {}
    written = 0
    for ins in result.get("instruments") or []:
        fid = f"framing:{slug}:{system.slugify(ins.get('id') or ins.get('title'))}"
        p = d / f"{system.slugify(ins.get('id') or ins.get('title'))}.md"
        links = [okf.link("in_system", f"system:{slug}", p, sys_path)]
        front = {"id": fid, "kind": "framing", "title": ins.get("title", ""), "institution": ins.get("institution", ""),
                 "instrument_type": ins.get("instrument_type", ""), "jurisdiction": ins.get("jurisdiction", ""),
                 "year": ins.get("year", ""), "effect_on_classes": ins.get("effect_on_classes", ""),
                 "classes": ins.get("classes", []), "links": links, "sources": [ins.get("evidence", "")]}
        body = (f"# {ins.get('title','')}\n\n{ins.get('institution','')} · {ins.get('instrument_type','')} · {ins.get('jurisdiction','')} {ins.get('year','')}\n\n"
                f"## Effect on classes\n\n{ins.get('effect_on_classes','')}\n\n## Evidence\n\n{ins.get('evidence','')}\n\n"
                f"## Classes\n\n" + "\n".join(f"- {c}" for c in ins.get("classes", [])) + "\n")
        okf.write_node(p, front, body)
        written += 1
        for c in ins.get("classes", []):
            by_class.setdefault(str(c), []).append(fid)
    if not by_class or result.get("none_stated_for"):
        p = d / "none-stated.md"
        okf.write_node(p, {"id": f"framing:{slug}:none-stated", "kind": "framing", "title": "No framing stated",
                           "institution": "", "instrument_type": "none", "jurisdiction": "", "classes": result.get("none_stated_for", []),
                           "links": [okf.link("in_system", f"system:{slug}", p, sys_path)]},
                       "# No framing stated\n\nThe source gives no institution, instrument or purpose behind these class names.\n")
        for c in result.get("none_stated_for") or []:
            by_class.setdefault(str(c), []).append(f"framing:{slug}:none-stated")
    t = system.load_table(slug)
    for cls in _classes_of(slug):
        fids = by_class.get(cls["code"]) or by_class.get(cls["class_id"]) or []
        if fids:
            cls["framing"] = fids
            node = system.read_class(slug, cls["code"] or cls["name"])
            cls["rationale"] = node.body.split("## Rationale", 1)[1].split("\n## ", 1)[0].strip() if "## Rationale" in node.body else ""
            system.write_class(slug, cls, t if t.rows else None)
    meta = system.read_system(slug)
    m = {k: meta.get(k, "") for k in ("publisher", "version", "jurisdiction", "language", "mode", "sources", "run_history")}
    m["name"] = meta.get("title")
    m["framing_summary"] = result.get("summary", "")
    system.write_system(slug, m, _classes_of(slug))
    _record_run(slug, "extract-framing", f"{written} instruments")
    return {"instruments": written, "classes_linked": len(by_class)}


# ---------------------------------------------------------- critique
def apply_critique(slug: str, result: dict | None = None, extra_systems: list[str] | None = None) -> dict:
    """Combine rule critics with the skill's items (result['items']) and write attention/<slug>.md."""
    t = system.load_table(slug)
    classes = _classes_of(slug)
    framing_by_class = {c["class_id"]: c.get("framing", []) for c in classes}
    items = critics.run_system(t, classes, framing_by_class)
    if extra_systems:
        systems = {slug: (t, classes)}
        for s in extra_systems:
            systems[s] = (system.load_table(s), _classes_of(s))
        items += critics.run_cross_system(systems)
    for it in (result or {}).get("items") or []:
        it.setdefault("severity", 3)
        it.setdefault("affects", [])
        it["source"] = "skill"
        items.append(it)
    ranked = critics.rank(items)
    p = ATTENTION / f"{slug}.md"
    sys_path = system.system_dir(slug) / "SYSTEM.md"
    links = [okf.link("in_system", f"system:{slug}", p, sys_path)]
    def full_item(i, it):
        opts = "\n".join(f"   - {o}" for o in it.get("options") or [])
        aff = ", ".join(str(a) for a in it.get("affects") or []) or "this class only"
        return (f"## {i}. {it.get('code','')} {it.get('name','')} · `{it['kind']}` · score {it['rank_score']}\n\n"
                f"{it.get('explanation','')}\n\n   Options:\n{opts}\n\n   Affects: {aff}"
                + (f"\n\n   Framing: {it['framing_ref']}" if it.get("framing_ref") else "")
                + (f"\n\n   Evidence: {it['evidence']}" if it.get("evidence") else "") + "\n")

    def short_item(i, it):
        return f"- {i}. {it.get('code','')} {it.get('name','')} · `{it['kind']}` · score {it['rank_score']}"

    head = (f"# Attention list: {slug}\n\nRanked by severity × blast radius. Each item is a decision for a stakeholder, "
            f"with the concrete options and what depends on it. {len(ranked)} items; the full list with options is in "
            f"`{slug}.json` beside this file.\n\n")
    # as many full items as fit under the node cap, the rest as one line each
    n_full = len(ranked)
    while n_full >= 0:
        body = head + "\n".join(full_item(i, it) for i, it in enumerate(ranked[:n_full], start=1))
        if n_full < len(ranked):
            body += "\n## Further items\n\n" + "\n".join(short_item(i, it) for i, it in enumerate(ranked[n_full:], start=n_full + 1)) + "\n"
        seen = set()
        links = [okf.link("in_system", f"system:{slug}", p, sys_path)]
        for it in ranked[:n_full]:
            code = it.get("code") or it.get("class_id")
            cp = system.class_path(slug, code)
            if cp.exists() and code not in seen:
                seen.add(code)
                links.append(okf.link("about", f"system:{slug}:{system.slugify(code)}", p, cp))
            fr = it.get("framing_ref")
            if fr and fr not in seen:
                fp = system.system_dir(slug) / "framing" / f"{system.slugify(fr.split(':')[-1])}.md"
                if fp.exists():
                    seen.add(fr)
                    links.append(okf.link("hinges_on", fr, p, fp))
        front = {"id": f"attention:{slug}", "kind": "attention", "title": f"Attention list: {slug}", "system": f"system:{slug}",
                 "generated": _now(), "n_items": len(ranked), "n_detailed": n_full,
                 "by_kind": {k: sum(1 for x in ranked if x["kind"] == k) for k in sorted({x["kind"] for x in ranked})},
                 "links": links}
        if len(okf.render(front, body)) <= okf.MAX_NODE_CHARS - 200:
            break
        n_full -= max(1, n_full // 4)
    okf.write_node(p, front, body)
    (ATTENTION / f"{slug}.json").write_text(json.dumps(ranked, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    _record_run(slug, "critique-system", f"{len(ranked)} items")
    return {"items": len(ranked), "by_kind": front["by_kind"], "top": [f"{x.get('code','')} {x['kind']}" for x in ranked[:8]]}
