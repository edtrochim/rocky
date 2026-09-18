"""End-to-end pipeline in a temporary OKF root: ingest ten MapBiomas legends, run the rule critics,
apply a decomposition, emit both FAO formats, build a package. Uses the tools as subprocesses so the
CLI contracts are what is tested. Registry-dependent steps are skipped when the registry cache is absent."""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
LEGENDS = REPO / "mapbiomas_doc" / "provenance" / "legends.json"
TOOLS = REPO / "okf" / "tools"
RUNNER = REPO / "okf" / "agents" / "runner.py"
COUNTRIES = ["brazil", "argentina", "bolivia", "chile", "colombia", "ecuador", "paraguay", "peru", "uruguay", "venezuela"]


def run(env, *args):
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, env=env, cwd=REPO)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    return json.loads(r.stdout)


@pytest.fixture(scope="module")
def okf_root(tmp_path_factory):
    root = tmp_path_factory.mktemp("okf")
    for sub in ("vocab", "standards"):
        src = REPO / "okf" / sub
        if src.exists():
            shutil.copytree(src, root / sub)
    reg = REPO / "okf" / "registry"
    if reg.exists() and (reg / "INDEX.md").exists():
        shutil.copytree(reg, root / "registry", ignore=shutil.ignore_patterns("_raw"))
    (root / "START.md").write_text("---\nid: start\nkind: start\ntitle: Start\nschema: okf/0.1\n---\n# Start\n", encoding="utf-8")
    env = dict(os.environ, ROCKY_OKF_ROOT=str(root))
    harm = REPO / "mapbiomas_doc" / "provenance" / "harmonization.csv"
    for c in COUNTRIES:
        run(env, TOOLS / "ingest.py", LEGENDS, "--system", f"mapbiomas_{c}", "--select", c, "--name", f"MapBiomas {c}",
            "--publisher", "MapBiomas", "--jurisdiction", c, "--parents", f"{harm}:code:tier_a_code:country={c}")
    return root, env


def test_parents_from_harmonization(okf_root):
    root, env = okf_root
    node = (root / "systems" / "mapbiomas_peru" / "classes" / "32.md").read_text(encoding="utf-8")
    assert "parent_code: '22'" in node or "parent_code: 22" in node


@pytest.mark.skipif(not (REPO / "okf" / "registry" / "L23" / "elements.csv").exists(), reason="registry cache absent")
def test_eval_prepare_and_self_check(okf_root):
    root, env = okf_root
    rep = run(env, TOOLS / "eval_registry.py", "--legend", "L23", "--prepare")
    assert rep["classes"] >= 5 and rep["prompts"] == rep["classes"]
    prompt = (root / "systems" / "eval_L23" / "_runs").glob("decompose-class-*/prompt.md")
    text = next(prompt).read_text(encoding="utf-8")
    assert "registry:L23" not in text.split("# Context: nearest registry example")[1] if "# Context: nearest registry example" in text else True
    rep = run(env, TOOLS / "eval_registry.py", "--legend", "L23", "--self-check")
    a = rep["aggregate"]
    assert a["element_recall"] == 1.0 and a["presence_agreement"] == 1.0 and a["range_overlap"] == 1.0


def test_ingest_counts(okf_root):
    root, env = okf_root
    n = json.loads((root / "systems" / "mapbiomas_brazil" / "SYSTEM.md").read_text(encoding="utf-8").split("n_classes: ")[1].split("\n")[0])
    assert n == 38


def test_rule_critics_find_documented_mapbiomas_issues(okf_root):
    root, env = okf_root
    others = [f"mapbiomas_{c}" for c in COUNTRIES if c != "brazil"]
    run(env, RUNNER, "critique", "--system", "mapbiomas_brazil", "--compare", *others)
    items = json.loads((root / "attention" / "mapbiomas_brazil.json").read_text(encoding="utf-8"))
    coll = {i["code"]: i for i in items if i["kind"] == "cross_system_collision"}
    # the README-documented collisions: code 4 (six meanings), 50 (sandbank vs xerophytic), 63 is Argentina/Chile only
    assert coll["4"]["severity"] >= 4, coll.get("4")
    assert coll["50"]["severity"] >= 4, coll.get("50")
    # spelling variants stay low
    assert coll["26"]["severity"] == 1, coll.get("26")
    masq = {i["code"] for i in items if i["kind"] == "land_use_masquerade"}
    assert {"15", "30", "31", "9"} <= masq   # Pasture, Mining, Aquaculture, Forest Plantation
    top = items[:15]
    assert any(i["code"] == "4" and i["kind"] == "cross_system_collision" for i in top)


def test_argentina_chile_code_63_collision(okf_root):
    root, env = okf_root
    run(env, RUNNER, "critique", "--system", "mapbiomas_argentina", "--compare", "mapbiomas_chile")
    items = json.loads((root / "attention" / "mapbiomas_argentina.json").read_text(encoding="utf-8"))
    c63 = [i for i in items if i["kind"] == "cross_system_collision" and i["code"] == "63"]
    assert c63 and c63[0]["severity"] >= 4


def test_apply_decomposition_then_emit_and_package(okf_root):
    root, env = okf_root
    result = {
        "status": "proposed", "confidence": 0.9, "land_use_hint": "", "rationale": "test", "examples_note": "",
        "nearest_examples": [], "evidence": [{"row_path": "hp1/st1/el1", "quote": "test"}], "open_questions": [],
        "patterns": [{"cover": None, "occurrence": None, "strata": [
            {"presence": "fixed", "onTop": False, "elements": [
                {"ref": "LC_Tree", "presence": "fixed", "cover": [70, 100], "height": [5, 40], "properties": {"woodyLeafPhenology": "Evergreen"},
                 "characteristics": [{"ref": "LC_VegetationArtificialityCharacteristic", "fields": {"vegetationArtificiality": "Natural or Seminatural"}}],
                 "evidence": "test", "confidence": 0.9}]}]}]}
    rp = root / "result.json"
    rp.write_text(json.dumps(result), encoding="utf-8")
    rep = run(env, RUNNER, "apply", "decompose-class", "--system", "mapbiomas_brazil", "--code", "3", "--result", rp)
    assert rep["validator_errors"] == []
    node = (root / "systems" / "mapbiomas_brazil" / "classes" / "3.md").read_text(encoding="utf-8")
    assert "status: proposed" in node and "LC_Tree" in node
    sysdir = root / "systems" / "mapbiomas_brazil"
    rep = run(env, TOOLS / "convert.py", sysdir / "elements.csv", "--to", "lchs", "--out", sysdir / "x.LChS", "--system", "mapbiomas_brazil")
    assert rep["schema_errors"] == []
    rep = run(env, TOOLS / "convert.py", sysdir / "elements.csv", "--to", "lccs3", "--out", sysdir / "x.lccs", "--system", "mapbiomas_brazil")
    assert rep["schema_errors"] == [] and len(rep["omitted_classes"]) == 37
    rep = run(env, TOOLS / "submission_check.py", "--system", "mapbiomas_brazil", "--build")
    assert rep["ok"], rep
    assert (sysdir / "package" / "mapbiomas_brazil.csv").exists()


def test_okf_check_passes_in_temp_root(okf_root):
    root, env = okf_root
    rep = run(env, TOOLS / "okf_build.py")
    assert rep["ok"], rep
    rep = run(env, TOOLS / "okf_build.py", "--check")
    assert rep["ok"], rep
