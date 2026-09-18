"""equivalence: mechanical comparison of two systems (uploaded or registry), written to comparisons/.

    python okf/tools/equivalence.py --a <slug|registry:L16> --b <slug|registry:L20>

Writes comparisons/<a>__<b>.md with the equivalence matrix and returns the
uncertain cells for the compare-systems skill.
"""

from __future__ import annotations

import argparse
import json

from _common import OKF_ROOT, out, fail, rel
from rocky import okf, system, equivalence, apply
from rocky.table import Table


def load(ref: str):
    if ref.startswith("registry:"):
        code = ref.split(":", 1)[1]
        d = OKF_ROOT / "registry" / code
        t = Table.from_csv(d / "elements.csv")
        classes = []
        for p in sorted((d / "classes").glob("*.md")):
            n = okf.read_node(p)
            classes.append({"class_id": n.front.get("file_class_id") or n.front.get("code"), "code": n.front.get("code"), "name": n.front.get("name")})
        return t, [c for c in classes if c["class_id"]], d / "SYSTEM.md", ref, code
    t = system.load_table(ref)
    classes = apply._classes_of(ref)
    return t, classes, system.system_dir(ref) / "SYSTEM.md", f"system:{ref}", ref


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    a = ap.parse_args()
    ta, ca, pa, ida, sa = load(a.a)
    tb, cb, pb, idb, sb = load(a.b)
    cells = equivalence.compare(ta, ca, tb, cb)
    best = equivalence.best_matches(cells)
    d = OKF_ROOT / "comparisons"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{system.slugify(sa)}__{system.slugify(sb)}.md"
    counts = {k: sum(1 for c in best if c["relation"] == k) for k in ("same_physical_as", "overlaps", "undecided", "disjoint_from")}
    rows = "\n".join(f"| {c['a']} {c['a_name']} | {c['b']} {c['b_name']} | {c['relation']} | {c['detail'][:120]} |" for c in best)
    front = {"id": f"comparison:{system.slugify(sa)}__{system.slugify(sb)}", "kind": "comparison",
             "title": f"Comparison {sa} vs {sb}", "a": ida, "b": idb, "counts": counts, "n_cells": len(cells),
             "links": [okf.link("compares", ida, p, pa), okf.link("compares", idb, p, pb)]}
    body = (f"# Comparison: {sa} vs {sb}\n\nMechanical first pass from element sets and cover ranges (`rocky.equivalence`). "
            f"Best match per class of A. {counts}\n\n| class of A | best match in B | relation | why |\n|---|---|---|---|\n{rows}\n")
    try:
        okf.write_node(p, front, body)
    except ValueError:
        okf.write_node(p, front, body[: okf.MAX_NODE_CHARS - 1500] + "\n\n_truncated; full matrix in the .json_\n")
    (d / (p.stem + ".json")).write_text(json.dumps(cells, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    uncertain = [c for c in cells if c["relation"] in ("overlaps", "undecided")][:200]
    out({"ok": True, "comparison": rel(p), "counts": counts, "uncertain": len(uncertain)})


if __name__ == "__main__":
    main()
