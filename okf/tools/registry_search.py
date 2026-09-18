"""registry_search: find registered legends by country, region, publisher, year or word.

    python okf/tools/registry_search.py --q "uruguay"      python okf/tools/registry_search.py --q "corine" --q 2018
"""

from __future__ import annotations

import argparse

from _common import OKF_ROOT, out
from rocky import okf


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--q", action="append", default=[], help="term; repeat to require all")
    a = ap.parse_args()
    terms = [q.lower() for q in a.q]
    hits = []
    for p in sorted((OKF_ROOT / "registry").glob("*/SYSTEM.md")):
        n = okf.read_node(p)
        hay = " ".join(str(v) for v in n.front.values() if not isinstance(v, list)).lower() + " " + n.body.lower()
        if all(t in hay for t in terms):
            f = n.front
            hits.append({"id": f.get("id"), "title": f.get("title"), "country": f.get("country"), "year": f.get("year"),
                         "format": f.get("format"), "classes": f.get("n_classes_index"), "publisher": f.get("publisher"),
                         "path": p.relative_to(OKF_ROOT).as_posix()})
    out({"ok": True, "terms": terms, "hits": hits})


if __name__ == "__main__":
    main()
