"""okf_build: regenerate ONTOLOGY.md and _index.json, check the folder.

    python okf/tools/okf_build.py            build
    python okf/tools/okf_build.py --check    build into memory, fail if anything would change
                                             or any node is invalid
"""

from __future__ import annotations

import argparse
import json

from _common import OKF_ROOT, out, fail, rel
from rocky import okf


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    ontology_text = okf.render({"id": "ontology", "kind": "ontology", "title": "Ontology", "schema": okf.SCHEMA},
                               okf.ontology_markdown())
    ont_path = OKF_ROOT / "ONTOLOGY.md"
    idx_path = OKF_ROOT / "_index.json"

    changes = []
    if not ont_path.exists() or ont_path.read_text(encoding="utf-8") != ontology_text:
        changes.append(rel(ont_path))
        if not a.check:
            ont_path.parent.mkdir(parents=True, exist_ok=True)
            ont_path.write_text(ontology_text, encoding="utf-8", newline="\n")
    index_text = json.dumps({"schema": okf.SCHEMA, "nodes": okf.build_index(OKF_ROOT)}, indent=1, ensure_ascii=False) + "\n"
    if not idx_path.exists() or idx_path.read_text(encoding="utf-8") != index_text:
        changes.append(rel(idx_path))
        if not a.check:
            idx_path.write_text(index_text, encoding="utf-8", newline="\n")
    problems = okf.check(OKF_ROOT)

    if a.check:
        if problems or changes:
            fail("okf check failed", problems=problems, would_change=changes)
        out({"ok": True, "nodes": len(okf.build_index(OKF_ROOT)), "problems": [], "would_change": []})
    out({"ok": not problems, "nodes": len(okf.build_index(OKF_ROOT)), "problems": problems, "changed": changes},
        0 if not problems else 1)


if __name__ == "__main__":
    main()
