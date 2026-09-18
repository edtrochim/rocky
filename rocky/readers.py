"""Readers that turn a classification-system document into raw blocks.

Ingest never interprets. Each reader returns ``list[RawBlock]``: text with a
location (page, row, cell) and, for tables, the row cells. The
``ingest-classification`` skill turns blocks into class nodes; when the input
is a well-formed table with recognisable columns, ``table_classes`` does that
deterministically with no model call.

Supported: JSON (MapBiomas ``legends.json`` shape and generic lists), CSV,
XLSX, PDF (pdfplumber: tables first, then page text), DOCX (zip + XML, no
extra dependency), HTML (BeautifulSoup), Markdown and plain text, and the two
FAO formats via ``lchs``/``lccs`` (which yield a table directly).
"""

from __future__ import annotations

import csv
import json
import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

CODE_KEYS = ("code", "class_code", "map_code", "value", "id", "pixel", "pixel_value", "class id", "classcode", "código", "codigo")
NAME_KEYS = ("name", "class", "class_name", "label", "title", "class name", "nombre", "classe", "clase", "legend")
DEF_KEYS = ("definition", "description", "desc", "definición", "definicion", "descripcion", "descrição")
PARENT_KEYS = ("parent", "parent_code", "level1", "level_1", "group", "category")
COLOUR_KEYS = ("color", "colour", "hex", "rgb", "palette")


@dataclass
class RawBlock:
    text: str
    kind: str = "text"            # text | table_row | heading
    page: int | None = None
    row: int | None = None
    cells: list[str] = field(default_factory=list)
    header: list[str] = field(default_factory=list)
    source: str = ""


@dataclass
class ClassRecord:
    """A class as far as a deterministic reader can tell; the skill refines it."""
    code: str = ""
    name: str = ""
    definition: str = ""
    parent: str = ""
    colour: str = ""
    language: str = ""
    source_span: str = ""
    extra: dict = field(default_factory=dict)


def read(path: str | Path) -> list[RawBlock]:
    p = Path(path)
    ext = p.suffix.lower()
    if ext == ".json":
        return read_json(p)
    if ext in (".csv", ".tsv"):
        return read_csv(p)
    if ext in (".xlsx", ".xlsm"):
        return read_xlsx(p)
    if ext == ".pdf":
        return read_pdf(p)
    if ext == ".docx":
        return read_docx(p)
    if ext in (".html", ".htm"):
        return read_html(p)
    return read_text(p)


# ------------------------------------------------------------------ tables
def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def _pick(header: list[str], keys: tuple[str, ...]) -> int | None:
    h = [_norm(x) for x in header]
    for k in keys:
        if k in h:
            return h.index(k)
    for i, x in enumerate(h):
        if any(k in x for k in keys):
            return i
    return None


def table_classes(blocks: list[RawBlock]) -> list[ClassRecord]:
    """Class records from table rows whose header names a code and/or a name column."""
    out: list[ClassRecord] = []
    for b in blocks:
        if b.kind != "table_row" or not b.header:
            continue
        ic, iname = _pick(b.header, CODE_KEYS), _pick(b.header, NAME_KEYS)
        idef, ipar, icol = _pick(b.header, DEF_KEYS), _pick(b.header, PARENT_KEYS), _pick(b.header, COLOUR_KEYS)
        if iname is None and ic is None:
            continue
        g = lambda i: (b.cells[i].strip() if i is not None and i < len(b.cells) else "")
        name, code = g(iname), g(ic)
        if not name and not code:
            continue
        out.append(ClassRecord(code=code, name=name, definition=g(idef), parent=g(ipar), colour=g(icol),
                               source_span=f"{b.source} row {b.row}" + (f" page {b.page}" if b.page else "")))
    return out


def read_csv(p: Path) -> list[RawBlock]:
    blocks = []
    with p.open(encoding="utf-8-sig", newline="") as f:
        sample = f.read(4096)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
        except csv.Error:
            dialect = csv.excel
        rows = list(csv.reader(f, dialect))
    if not rows:
        return blocks
    header = [c.strip() for c in rows[0]]
    for i, r in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in r):
            continue
        blocks.append(RawBlock(text=" | ".join(r), kind="table_row", row=i, cells=r, header=header, source=p.name))
    return blocks


def read_xlsx(p: Path) -> list[RawBlock]:
    import openpyxl
    blocks = []
    wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
    for ws in wb.worksheets:
        header: list[str] = []
        for i, row in enumerate(ws.iter_rows(values_only=True), start=1):
            cells = ["" if v is None else str(v) for v in row]
            if not any(c.strip() for c in cells):
                continue
            if not header:
                header = [c.strip() for c in cells]
                continue
            blocks.append(RawBlock(text=" | ".join(cells), kind="table_row", row=i, cells=cells, header=header,
                                   source=f"{p.name}:{ws.title}"))
    return blocks


def read_json(p: Path) -> list[RawBlock]:
    """MapBiomas legends.json ({system: {classes: {code: [name, colour]}}}) or a list of dicts."""
    data = json.loads(p.read_text(encoding="utf-8"))
    blocks = []
    if isinstance(data, list):
        keys = sorted({k for d in data if isinstance(d, dict) for k in d})
        for i, d in enumerate(data, start=1):
            if isinstance(d, dict):
                cells = [str(d.get(k, "")) for k in keys]
                blocks.append(RawBlock(text=json.dumps(d, ensure_ascii=False), kind="table_row", row=i, cells=cells, header=keys, source=p.name))
        return blocks
    if isinstance(data, dict):
        for sys_name, sysd in data.items():
            if sys_name.startswith("_") or not isinstance(sysd, dict):
                continue
            classes = sysd.get("classes")
            if isinstance(classes, dict):
                header = ["system", "code", "name", "colour", "collection", "source"]
                for i, (code, val) in enumerate(classes.items(), start=1):
                    name, colour = (val[0], val[1]) if isinstance(val, (list, tuple)) and len(val) >= 2 else (str(val), "")
                    cells = [sys_name, str(code), str(name), str(colour), str(sysd.get("collection", "")), str(sysd.get("source", ""))]
                    blocks.append(RawBlock(text=f"{sys_name} {code} {name}", kind="table_row", row=i, cells=cells, header=header, source=f"{p.name}:{sys_name}"))
                if sysd.get("note"):
                    blocks.append(RawBlock(text=str(sysd["note"]), kind="text", source=f"{p.name}:{sys_name}"))
            else:
                blocks.append(RawBlock(text=json.dumps(sysd, ensure_ascii=False)[:4000], kind="text", source=f"{p.name}:{sys_name}"))
    return blocks


# --------------------------------------------------------------- documents
def read_pdf(p: Path) -> list[RawBlock]:
    import pdfplumber
    blocks = []
    with pdfplumber.open(str(p)) as pdf:
        for pno, page in enumerate(pdf.pages, start=1):
            for tbl in page.extract_tables() or []:
                if not tbl or len(tbl) < 2:
                    continue
                header = [(c or "").strip() for c in tbl[0]]
                for i, r in enumerate(tbl[1:], start=2):
                    cells = [(c or "").strip() for c in r]
                    if any(cells):
                        blocks.append(RawBlock(text=" | ".join(cells), kind="table_row", page=pno, row=i, cells=cells, header=header, source=p.name))
            text = page.extract_text() or ""
            for para in re.split(r"\n\s*\n", text):
                para = para.strip()
                if para:
                    blocks.append(RawBlock(text=para, kind="text", page=pno, source=p.name))
    return blocks


def read_docx(p: Path) -> list[RawBlock]:
    from lxml import etree
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    blocks = []
    with zipfile.ZipFile(p) as z:
        root = etree.fromstring(z.read("word/document.xml"))
    body = root.find(f"{W}body")
    for i, el in enumerate(body, start=1):
        if el.tag == f"{W}p":
            text = "".join(t.text or "" for t in el.iter(f"{W}t")).strip()
            style = el.find(f"{W}pPr/{W}pStyle")
            kind = "heading" if style is not None and "Heading" in (style.get(f"{W}val") or "") else "text"
            if text:
                blocks.append(RawBlock(text=text, kind=kind, row=i, source=p.name))
        elif el.tag == f"{W}tbl":
            rows = []
            for tr in el.iter(f"{W}tr"):
                rows.append(["".join(t.text or "" for t in tc.iter(f"{W}t")).strip() for tc in tr.iter(f"{W}tc")])
            if len(rows) >= 2:
                header = rows[0]
                for j, r in enumerate(rows[1:], start=2):
                    if any(r):
                        blocks.append(RawBlock(text=" | ".join(r), kind="table_row", row=j, cells=r, header=header, source=f"{p.name}:table{i}"))
    return blocks


def read_html(p: Path) -> list[RawBlock]:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(p.read_text(encoding="utf-8", errors="replace"), "html.parser")
    blocks = []
    for ti, table in enumerate(soup.find_all("table"), start=1):
        rows = [[c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])] for tr in table.find_all("tr")]
        rows = [r for r in rows if any(r)]
        if len(rows) >= 2:
            header = rows[0]
            for j, r in enumerate(rows[1:], start=2):
                blocks.append(RawBlock(text=" | ".join(r), kind="table_row", row=j, cells=r, header=header, source=f"{p.name}:table{ti}"))
        table.decompose()
    for el in soup.find_all(["h1", "h2", "h3", "h4", "p", "li", "dt", "dd"]):
        text = el.get_text(" ", strip=True)
        if text:
            blocks.append(RawBlock(text=text, kind="heading" if el.name.startswith("h") else "text", source=p.name))
    return blocks


def read_text(p: Path) -> list[RawBlock]:
    text = p.read_text(encoding="utf-8", errors="replace")
    blocks = []
    for i, para in enumerate(re.split(r"\n\s*\n", text), start=1):
        para = para.strip()
        if not para:
            continue
        kind = "heading" if para.startswith("#") else "text"
        blocks.append(RawBlock(text=para.lstrip("# ").strip() if kind == "heading" else para, kind=kind, row=i, source=p.name))
    return blocks


def classes_from_any(path: str | Path) -> tuple[list[ClassRecord], list[RawBlock]]:
    """Deterministic first pass: table-shaped classes if the input has them, plus all blocks for the skill."""
    blocks = read(path)
    return table_classes(blocks), blocks
