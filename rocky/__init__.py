"""Rocky: land cover classification systems -> LCML atomic elements.

Library code shared by the CLI tools in ``okf/tools``. Every module here is
deterministic and makes no model calls; agent reasoning lives in
``okf/skills``.
"""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
# ROCKY_OKF_ROOT lets tests and other deployments point the tools at another knowledge-base folder.
OKF_ROOT = Path(os.environ.get("ROCKY_OKF_ROOT") or (REPO_ROOT / "okf")).resolve()

__all__ = ["REPO_ROOT", "OKF_ROOT"]
