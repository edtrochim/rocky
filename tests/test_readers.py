"""Readers on small synthetic inputs: every format yields table rows or text blocks with provenance."""

import zipfile
from pathlib import Path

from rocky import readers


def test_csv_table(tmp_path):
    p = tmp_path / "legend.csv"
    p.write_text("Code;Class;Definition\n1;Forest;Trees > 10 % cover\n2;Grassland;Herbaceous cover\n", encoding="utf-8")
    cls, blocks = readers.classes_from_any(p)
    assert [c.code for c in cls] == ["1", "2"] and cls[0].definition == "Trees > 10 % cover"
    assert cls[0].source_span.startswith("legend.csv row 2")


def test_xlsx_table(tmp_path):
    import openpyxl
    p = tmp_path / "legend.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Value", "Label", "Description"])
    ws.append([11, "Open water", "All areas of open water"])
    wb.save(p)
    cls, _ = readers.classes_from_any(p)
    assert cls[0].code == "11" and cls[0].name == "Open water" and "open water" in cls[0].definition.lower()


def test_html_table_and_paragraphs(tmp_path):
    p = tmp_path / "legend.html"
    p.write_text("<h1>Nomenclature</h1><p>Scope: national mapping.</p><table><tr><th>Code</th><th>Name</th></tr>"
                 "<tr><td>311</td><td>Broad-leaved forest</td></tr></table>", encoding="utf-8")
    cls, blocks = readers.classes_from_any(p)
    assert cls[0].code == "311" and cls[0].name == "Broad-leaved forest"
    assert any(b.kind == "heading" and b.text == "Nomenclature" for b in blocks)
    assert any("Scope" in b.text for b in blocks if b.kind == "text")


def test_docx_paragraphs_and_table(tmp_path):
    W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    doc = (f'<w:document xmlns:w="{W}"><w:body>'
           '<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Classes</w:t></w:r></w:p>'
           '<w:p><w:r><w:t>Forest: trees above 5 m.</w:t></w:r></w:p>'
           '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Code</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>Name</w:t></w:r></w:p></w:tc></w:tr>'
           '<w:tr><w:tc><w:p><w:r><w:t>F</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>Forest</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
           '</w:body></w:document>')
    p = tmp_path / "legend.docx"
    with zipfile.ZipFile(p, "w") as z:
        z.writestr("word/document.xml", doc)
        z.writestr("[Content_Types].xml", "<Types/>")
    cls, blocks = readers.classes_from_any(p)
    assert cls[0].code == "F" and cls[0].name == "Forest"
    assert any(b.kind == "heading" for b in blocks) and any("above 5 m" in b.text for b in blocks)


def test_text_blocks(tmp_path):
    p = tmp_path / "legend.md"
    p.write_text("# Legend\n\nForest: trees.\n\nGrassland: grass.\n", encoding="utf-8")
    cls, blocks = readers.classes_from_any(p)
    assert cls == [] and len(blocks) == 3 and blocks[0].kind == "heading"


def test_mapbiomas_json_select():
    p = Path(__file__).resolve().parents[1] / "mapbiomas_doc" / "provenance" / "legends.json"
    cls, blocks = readers.classes_from_any(p)
    brazil = [c for c in cls if c.source_span.startswith("legends.json:brazil")]
    assert len(brazil) == 38 and any(c.code == "4" and c.name == "Savanna Formation" for c in brazil)
