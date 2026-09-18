"""Mechanical first pass at comparing two described systems.

For every pair of decomposed classes, compare element sets and cover ranges::

    same_physical_as   identical element refs, every shared range overlaps by ≥ 80 % of the narrower range
    overlaps           element sets intersect, or identical refs with partially overlapping ranges
    disjoint_from      no element in common
    undecided          one side has no decomposition

Returns a matrix the compare-systems skill reviews; only uncertain cells
(overlaps with framing differences, undecided) need the model.
"""

from __future__ import annotations

from .table import Table


def _elements(t: Table, cid: str) -> dict[str, tuple | None]:
    out: dict[str, tuple | None] = {}
    for hid in t.hps(cid):
        for sid in t.strata(cid, hid):
            for bid, ref in t.blocks(cid, hid, sid):
                a = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, block_id=bid, record="element")
                c = a.get("cover")
                rng = None
                if c and c.min and c.max:
                    try:
                        rng = (float(c.min), float(c.max))
                    except ValueError:
                        rng = None
                if ref not in out or (out[ref] is None and rng is not None):
                    out[ref] = rng
    return out


def _range_relation(a, b) -> str:
    if a is None or b is None:
        return "unknown"
    lo, hi = max(a[0], b[0]), min(a[1], b[1])
    if hi < lo:
        return "disjoint"
    inter = hi - lo
    narrower = min(a[1] - a[0], b[1] - b[0]) or 1.0
    return "same" if inter / narrower >= 0.8 else "partial"


def compare(ta: Table, classes_a: list[dict], tb: Table, classes_b: list[dict]) -> list[dict]:
    cells = []
    ea = {c["class_id"]: _elements(ta, c["class_id"]) for c in classes_a}
    eb = {c["class_id"]: _elements(tb, c["class_id"]) for c in classes_b}
    for ca in classes_a:
        A = ea[ca["class_id"]]
        for cb in classes_b:
            B = eb[cb["class_id"]]
            if not A or not B:
                rel, detail = "undecided", "no decomposition on one side"
            else:
                shared = set(A) & set(B)
                if not shared:
                    rel, detail = "disjoint_from", "no element in common"
                elif set(A) == set(B):
                    rels = {r: _range_relation(A[r], B[r]) for r in shared}
                    if all(v in ("same", "unknown") for v in rels.values()):
                        rel, detail = "same_physical_as", "same elements; ranges agree or are unstated"
                    elif any(v == "disjoint" for v in rels.values()):
                        rel, detail = "disjoint_from", "same elements but a cover range does not overlap: " + ", ".join(f"{r} {A[r]} vs {B[r]}" for r, v in rels.items() if v == "disjoint")
                    else:
                        rel, detail = "overlaps", "same elements, ranges partially overlap: " + ", ".join(f"{r} {A[r]} vs {B[r]}" for r, v in rels.items() if v == "partial")
                else:
                    rel, detail = "overlaps", f"shared {sorted(shared)}; only in A {sorted(set(A) - shared)}; only in B {sorted(set(B) - shared)}"
            if rel != "disjoint_from" or (A and B and set(A) & set(B)):
                cells.append({"a": ca.get("code") or ca["class_id"], "a_name": ca.get("name", ""),
                              "b": cb.get("code") or cb["class_id"], "b_name": cb.get("name", ""),
                              "relation": rel, "detail": detail, "decides": sorted(set(A) | set(B))})
    return cells


def best_matches(cells: list[dict]) -> list[dict]:
    """For each class of A, its best relation in B (same > overlaps > undecided)."""
    order = {"same_physical_as": 0, "overlaps": 1, "undecided": 2, "disjoint_from": 3}
    best: dict[str, dict] = {}
    for c in cells:
        cur = best.get(c["a"])
        if cur is None or order[c["relation"]] < order[cur["relation"]]:
            best[c["a"]] = c
    return list(best.values())
