"""Round-trip and validation guarantees for the two FAO formats.

Run with ``pytest``. Registry-based cases are skipped when the raw cache is
absent (``python okf/tools/build_registry.py --refresh`` fetches it).
"""

from pathlib import Path

import pytest

from rocky import lccs, lchs, schemas, validate
from rocky.table import Table, diff

REPO = Path(__file__).resolve().parents[1]
RAW = REPO / "okf" / "registry" / "_raw"
SAMPLE = REPO / "g4g2026_ideathon.lccs"

LCHS_FILES = sorted(RAW.glob("*/*.LChS")) if RAW.exists() else []
LCCS_FILES = ([SAMPLE] if SAMPLE.exists() else []) + (sorted(RAW.glob("*/*.lccs")) if RAW.exists() else [])
MODERN_LCHS = [f for f in LCHS_FILES if f.stem in ("L49", "L51")]


def _rt(read, write, path: Path, tmp_path: Path):
    t = read(path, path.stem)
    csv = tmp_path / (path.stem + ".csv")
    t.to_csv(csv)
    t2 = Table.from_csv(csv)
    t2.meta = t.meta
    outp = tmp_path / (path.stem + ".out" + path.suffix)
    write(t2, outp)
    t3 = read(outp, path.stem)
    return t, outp, diff(t, t3)


@pytest.mark.parametrize("path", LCHS_FILES, ids=lambda p: p.name)
def test_lchs_roundtrip_exact(path, tmp_path):
    t, outp, d = _rt(lchs.read, lchs.write, path, tmp_path)
    assert d == {"added": [], "removed": [], "changed": []}
    assert schemas.validate_lchs(outp) == []


@pytest.mark.parametrize("path", LCCS_FILES, ids=lambda p: p.name)
def test_lccs3_roundtrip_exact(path, tmp_path):
    t, outp, d = _rt(lccs.read, lccs.write, path, tmp_path)
    assert d == {"added": [], "removed": [], "changed": []}


# Registry files that use types outside the LCCS3 XSD; their source is invalid for the same reason.
KNOWN_XSD_GAPS = {"L20": "LC_MultiTreeAreaManagementPractices is not declared in the LCCS3 XSD"}


@pytest.mark.parametrize("path", LCCS_FILES, ids=lambda p: p.name)
def test_lccs3_written_is_xsd_valid(path, tmp_path):
    t = lccs.read(path, path.stem)
    outp = tmp_path / (path.stem + ".out.lccs")
    lccs.write(t, outp)
    errors = schemas.validate_lccs3(outp)
    if path.stem in KNOWN_XSD_GAPS:
        gap = KNOWN_XSD_GAPS[path.stem].split()[0]
        errors = [e for e in errors if gap not in e]
    assert errors == []


@pytest.mark.parametrize("path", MODERN_LCHS, ids=lambda p: p.name)
def test_modern_lchs_registry_files_pass_vocabulary_check(path):
    t = lchs.read(path, path.stem)
    assert validate.summary(validate.validate(t))["errors"] == 0


@pytest.mark.parametrize("path", MODERN_LCHS, ids=lambda p: p.name)
def test_lchs_to_lccs3_is_xsd_valid(path, tmp_path):
    t = lchs.read(path, path.stem)
    outp = tmp_path / (path.stem + ".x.lccs")
    lccs.write(t, outp)
    assert schemas.validate_lccs3(outp) == []
    t2 = lccs.read(outp, path.stem)
    assert len(t2.classes()) == len(t.classes())


@pytest.mark.parametrize("path", LCCS_FILES[:6], ids=lambda p: p.name)
def test_lccs3_to_lchs_is_schema_valid_and_keeps_classes(path, tmp_path):
    t = lccs.read(path, path.stem)
    outp = tmp_path / (path.stem + ".x.LChS")
    lchs.write(t, outp)
    assert schemas.validate_lchs(outp) == []
    t2 = lchs.read(outp, path.stem)
    assert len(t2.classes()) == len(t.classes())
    n_el = lambda tt: len({(r.stratum_id, r.block_id) for r in tt.rows if r.record == "element"})
    assert n_el(t2) == n_el(t)


def test_diff_detects_one_changed_range():
    if not MODERN_LCHS:
        pytest.skip("registry cache absent")
    t = lchs.read(MODERN_LCHS[0], "x")
    t2 = lchs.read(MODERN_LCHS[0], "x")
    row = next(r for r in t2.rows if r.record == "element" and r.attribute == "cover")
    row.max = "99"
    d = diff(t, t2)
    assert len(d["changed"]) == 1 and not d["added"] and not d["removed"]
