"""Fetch the FAO Land Cover Legend Registry (LCLR) into a local raw cache.

The registry is a static site over one JSON endpoint and one public bucket.
This module downloads the index and every legend file it names, records a
sha256 and fetch date per file, and never modifies what it fetched.

Raw cache layout (``okf/registry/_raw``)::

    index.json                 the endpoint response, verbatim
    manifest.json              {file: {url, sha256, bytes, fetched}}
    L16/L16.lccs, L16.csv ...  one folder per legend, files verbatim
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

INDEX_URL = "https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend"
BUCKET = "https://storage.googleapis.com/fao-hih-gs-website-review/resources/lclr"
FILE_KEYS = (".lccs", ".lchs", ".csv", ".xsd", ".eapx", ".htm", ".sho", ".shelf")
TIMEOUT = 60


def _sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fetch_index(session: requests.Session | None = None) -> list[dict]:
    s = session or requests.Session()
    r = s.get(INDEX_URL, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def legend_files(entry: dict) -> dict[str, str]:
    """Map local file name -> bucket URL for one index entry."""
    out = {}
    for k in FILE_KEYS:
        v = (entry.get(k) or "").strip()
        if v and v != "-":
            out[v] = f"{BUCKET}/legend/{v}"
    return out


def fetch_all(raw_dir: Path, refresh: bool = False, log=print) -> dict:
    raw_dir = Path(raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    index = fetch_index(s)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (raw_dir / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False), encoding="utf-8")

    manifest_path = raw_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    manifest["_index"] = {"url": INDEX_URL, "fetched": now, "entries": len(index)}

    problems = []
    for entry in index:
        code = entry.get("alphaCode") or f"id{entry.get('itemIdentifier')}"
        files = legend_files(entry)
        if not files:
            continue
        d = raw_dir / code
        d.mkdir(exist_ok=True)
        for fname, url in files.items():
            dest = d / fname
            key = f"{code}/{fname}"
            if dest.exists() and not refresh and key in manifest:
                continue
            try:
                r = s.get(url, timeout=TIMEOUT)
                if r.status_code != 200:
                    problems.append({"file": key, "url": url, "status": r.status_code})
                    log(f"  {key}: HTTP {r.status_code}")
                    continue
                dest.write_bytes(r.content)
                manifest[key] = {"url": url, "sha256": _sha(r.content), "bytes": len(r.content), "fetched": now}
                log(f"  {key}: {len(r.content)} bytes")
            except requests.RequestException as e:  # keep going; record it
                problems.append({"file": key, "url": url, "error": str(e)})
                log(f"  {key}: {e}")
    manifest["_problems"] = problems
    manifest_path.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    return {"entries": len(index), "files": sum(1 for k in manifest if not k.startswith("_")),
            "problems": problems}


def load_index(raw_dir: Path) -> list[dict]:
    return json.loads((Path(raw_dir) / "index.json").read_text(encoding="utf-8"))


def legend_format(entry: dict) -> str:
    """'lchs' | 'lccs3' | 'none' based on which file the entry actually ships."""
    if (entry.get(".lchs") or "").strip():
        return "lchs"
    if (entry.get(".lccs") or "").strip():
        return "lccs3"
    return "none"
