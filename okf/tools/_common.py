"""Shared plumbing for the CLI tools: JSON in, JSON out, repo-relative paths.

Every tool is a small ``main()`` that parses arguments, calls the library,
prints one JSON object on stdout and exits non-zero on failure. Agents on any
platform call them as subprocesses; humans call them from a shell.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from rocky import OKF_ROOT, REPO_ROOT  # noqa: E402


def out(obj, code: int = 0) -> None:
    print(json.dumps(obj, indent=1, ensure_ascii=False, default=str))
    sys.exit(code)


def fail(msg: str, **extra) -> None:
    out({"ok": False, "error": msg, **extra}, 1)


def rel(p: Path) -> str:
    try:
        return Path(p).resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(p)
