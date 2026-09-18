"""The table projection: one row per smallest unit of a class description.

This is the shape every other projection is derived from. It is long-form
so that a class, a horizontal pattern, a stratum, an element (block) and a
characteristic are all rows of the same kind, and so that the file diffs
cleanly and opens in a spreadsheet.

Row grammar
-----------
record      what the row describes: legend | class | class_char | hp | stratum | element | characteristic
ids         class_id, hp_id, stratum_id, block_id, char_id  (LChS ids; empty when not applicable)
ref         BlockReference for element rows, CharacteristicReference for characteristic rows
attribute   the property name in LChS terms (class_name, cover, elementPresenceType, woodyLeafPhenology ...)
min / max   for ranges (LChS repeats the element twice; here two columns)
value       for single values and enums
evidence, framing_ref, confidence, status, note   review metadata; never written to FAO XML except as notes

A class with no rows beyond ``record=class`` is a titles-only class.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, asdict, field, fields
from pathlib import Path
from typing import Iterable, Iterator

COLUMNS = [
    "system", "record", "class_id", "class_map_code", "class_name",
    "hp_id", "stratum_id", "block_id", "char_id", "ref",
    "attribute", "min", "max", "value",
    "evidence", "framing_ref", "confidence", "status", "note",
]

RECORDS = ("legend", "class", "class_char", "hp", "stratum", "element", "characteristic")


@dataclass
class Row:
    system: str = ""
    record: str = ""
    class_id: str = ""
    class_map_code: str = ""
    class_name: str = ""
    hp_id: str = ""
    stratum_id: str = ""
    block_id: str = ""
    char_id: str = ""
    ref: str = ""
    attribute: str = ""
    min: str = ""
    max: str = ""
    value: str = ""
    evidence: str = ""
    framing_ref: str = ""
    confidence: str = ""
    status: str = ""
    note: str = ""

    def key(self) -> tuple:
        return (self.class_id, self.hp_id, self.stratum_id, self.block_id, self.char_id, self.attribute)


@dataclass
class Table:
    rows: list[Row] = field(default_factory=list)
    meta: dict = field(default_factory=dict)   # legend-level: name, description, author, source ...

    # ------------------------------------------------------------- build
    def add(self, **kw) -> Row:
        r = Row(**kw)
        self.rows.append(r)
        return r

    def extend(self, rows: Iterable[Row]) -> None:
        self.rows.extend(rows)

    # ------------------------------------------------------------ query
    def classes(self) -> list[tuple[str, str, str]]:
        """(class_id, map_code, name) in first-seen order."""
        seen: dict[str, tuple[str, str, str]] = {}
        for r in self.rows:
            if r.record == "class" and r.class_id not in seen:
                seen[r.class_id] = (r.class_id, r.class_map_code, r.class_name)
        return list(seen.values())

    def for_class(self, class_id: str) -> list[Row]:
        return [r for r in self.rows if r.class_id == class_id]

    def select(self, **kw) -> list[Row]:
        out = []
        for r in self.rows:
            if all(getattr(r, k) == v for k, v in kw.items()):
                out.append(r)
        return out

    def hps(self, class_id: str) -> list[str]:
        return _ordered({r.hp_id for r in self.rows if r.class_id == class_id and r.hp_id})

    def strata(self, class_id: str, hp_id: str) -> list[str]:
        return _ordered({r.stratum_id for r in self.rows
                         if r.class_id == class_id and r.hp_id == hp_id and r.stratum_id})

    def blocks(self, class_id: str, hp_id: str, stratum_id: str) -> list[tuple[str, str]]:
        """(block_id, ref) for element rows in a stratum."""
        seen: dict[str, str] = {}
        for r in self.rows:
            if (r.class_id, r.hp_id, r.stratum_id) == (class_id, hp_id, stratum_id) \
                    and r.record == "element" and r.block_id not in seen:
                seen[r.block_id] = r.ref
        return list(seen.items())

    def chars(self, class_id: str, hp_id: str, stratum_id: str, block_id: str) -> list[tuple[str, str]]:
        seen: dict[str, str] = {}
        for r in self.rows:
            if (r.class_id, r.hp_id, r.stratum_id, r.block_id) == (class_id, hp_id, stratum_id, block_id) \
                    and r.record == "characteristic" and r.char_id not in seen:
                seen[r.char_id] = r.ref
        return list(seen.items())

    def attrs(self, **where) -> dict[str, Row]:
        """attribute -> row for rows matching the ids given (exact match on every key)."""
        out: dict[str, Row] = {}
        for r in self.rows:
            if all(getattr(r, k) == v for k, v in where.items()):
                out.setdefault(r.attribute, r)
        return out

    def element_refs(self) -> set[str]:
        return {r.ref for r in self.rows if r.record == "element" and r.ref}

    def characteristic_refs(self) -> set[str]:
        return {r.ref for r in self.rows if r.record == "characteristic" and r.ref}

    # ---------------------------------------------------------------- io
    def to_csv(self, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
            w.writeheader()
            for r in self.rows:
                w.writerow(asdict(r))

    @classmethod
    def from_csv(cls, path: Path) -> "Table":
        t = cls()
        with Path(path).open(encoding="utf-8", newline="") as f:
            for d in csv.DictReader(f):
                t.rows.append(Row(**{k: (d.get(k) or "") for k in COLUMNS}))
        return t

    def to_records(self) -> list[dict]:
        return [asdict(r) for r in self.rows]

    def __len__(self) -> int:
        return len(self.rows)

    def __iter__(self) -> Iterator[Row]:
        return iter(self.rows)


def _ordered(s: set[str]) -> list[str]:
    def k(x: str):
        try:
            return (0, int(x), x)
        except ValueError:
            return (1, 0, x)
    return sorted(s, key=k)


def diff(a: Table, b: Table) -> dict:
    """Rows added, removed and changed between two tables, keyed by ids+attribute."""
    ka = {r.key(): r for r in a.rows if r.record != "legend"}
    kb = {r.key(): r for r in b.rows if r.record != "legend"}
    added = [asdict(kb[k]) for k in kb.keys() - ka.keys()]
    removed = [asdict(ka[k]) for k in ka.keys() - kb.keys()]
    changed = []
    for k in ka.keys() & kb.keys():
        ra, rb = ka[k], kb[k]
        if (ra.min, ra.max, ra.value, ra.ref) != (rb.min, rb.max, rb.value, rb.ref):
            changed.append({"key": k, "before": asdict(ra), "after": asdict(rb)})
    return {"added": added, "removed": removed, "changed": changed}
