"""ingest: create systems/<slug>/ from a source document, deterministically where possible.

    python okf/tools/ingest.py <input> --system <slug> --name "..." [--publisher ..] [--version ..]
                               [--jurisdiction ..] [--language ..] [--select <subsystem>] [--source-url ..]

Tables and JSON with code/name columns are ingested with no model call (every
class becomes a node with `status: titles_only` or `proposed` if a definition
column exists). Prose documents are split into blocks and written to
`systems/<slug>/_ingest/blocks.json` for the ingest-classification skill to
turn into classes. FAO `.LChS`/`.lccs` inputs are ingested with their rows and
put the system in refine mode.

For the MapBiomas legends.json, --select <country> picks one national legend.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from _common import out, fail, rel
from rocky import readers, system, lchs, lccs
from rocky.table import Table


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--system", required=True, help="slug for systems/<slug>/")
    ap.add_argument("--name", default="")
    ap.add_argument("--publisher", default="")
    ap.add_argument("--version", default="")
    ap.add_argument("--jurisdiction", default="")
    ap.add_argument("--language", default="")
    ap.add_argument("--select", default="", help="sub-system key inside a multi-system JSON (e.g. a MapBiomas country)")
    ap.add_argument("--source-url", default="")
    ap.add_argument("--parents", default="", help="CSV giving parent codes: <file>:<code col>:<parent col>[:<filter col>=<value>]")
    a = ap.parse_args()
    parents: dict[str, str] = {}
    if a.parents:
        import csv as _csv
        # split from the right so a Windows drive letter in the file path survives
        spec = a.parents
        flt = None
        if "=" in spec.rsplit(":", 1)[-1]:
            spec, f = spec.rsplit(":", 1)
            flt = f.split("=", 1)
        pfile, ccol, pcol = spec.rsplit(":", 2)
        with open(pfile, encoding="utf-8", newline="") as f:
            for r in _csv.DictReader(f):
                if flt and str(r.get(flt[0], "")).strip().lower() != flt[1].strip().lower():
                    continue
                if r.get(ccol) and r.get(pcol) and str(r[ccol]).strip() != str(r[pcol]).strip():
                    parents[str(r[ccol]).strip()] = str(r[pcol]).strip()

    src = Path(a.input)
    if not src.exists():
        fail(f"{src} does not exist")
    slug = a.system
    meta = {"name": a.name or src.stem, "publisher": a.publisher, "version": a.version,
            "jurisdiction": a.jurisdiction, "language": a.language,
            "sources": [rel(src)] + ([a.source_url] if a.source_url else [])}

    ext = src.suffix.lower()
    if ext in (".lchs", ".lccs"):
        t = lchs.read(src, slug) if ext == ".lchs" else lccs.read(src, slug)
        meta["mode"] = "refine"
        meta["scope_statement"] = t.meta.get("legend_description", "")
        classes = []
        for cid, code, name in t.classes():
            desc = t.attrs(class_id=cid, record="class").get("class_description")
            cls = {"class_id": cid, "code": code, "name": name, "definition": desc.value if desc else "",
                   "status": "registered" if "registry" in str(src) else "proposed", "source_span": rel(src)}
            classes.append(cls)
        system.write_system(slug, meta, classes)
        for cls in classes:
            system.write_class(slug, cls, t)
        system.save_table(slug, t)
        out({"ok": True, "system": slug, "mode": "refine", "classes": len(classes), "rows": len(t)})

    records, blocks = readers.classes_from_any(src)
    if a.select:
        records = [r for r in records if r.source_span.split(":")[-1].split(" ")[0].lower() == a.select.lower()
                   or a.select.lower() in r.source_span.lower()]
        blocks = [b for b in blocks if a.select.lower() in b.source.lower()]
        if not meta["name"] or meta["name"] == src.stem:
            meta["name"] = a.select
    meta["mode"] = "propose"
    d = system.system_dir(slug)
    (d / "_ingest").mkdir(parents=True, exist_ok=True)
    (d / "_ingest" / "blocks.json").write_text(
        json.dumps([b.__dict__ for b in blocks], indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    notes = "\n".join(b.text for b in blocks if b.kind == "text")[:3000]
    if notes:
        meta["notes"] = notes
    classes = []
    t = Table()
    t.meta = {"format": "table", "source": rel(src), "system": slug}
    for r in records:
        cid = r.code or system.slugify(r.name)
        cls = {"class_id": cid, "code": r.code, "name": r.name, "definition": r.definition, "parent_code": r.parent or parents.get(r.code, ""),
               "colour": r.colour, "language": r.language or a.language, "source_span": r.source_span,
               "status": "titles_only"}
        classes.append(cls)
        t.rows.extend(system.rows_from_proposal(slug, cid, r.code, r.name, {"definition": r.definition, "patterns": []}))
    if classes:
        system.write_system(slug, meta, classes)
        for cls in classes:
            system.write_class(slug, cls, None)
        system.save_table(slug, t)
        out({"ok": True, "system": slug, "mode": "propose", "classes": len(classes),
             "with_definition": sum(1 for c in classes if c["definition"]), "blocks": len(blocks),
             "next": "run decompose-class per class; prose blocks are in _ingest/blocks.json"})
    system.write_system(slug, meta, [])
    out({"ok": True, "system": slug, "mode": "propose", "classes": 0, "blocks": len(blocks),
         "next": "no table-shaped classes found; run the ingest-classification skill on _ingest/blocks.json"})


if __name__ == "__main__":
    main()
