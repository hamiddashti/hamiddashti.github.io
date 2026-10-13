"""Default paths for the helper scripts in scripts/.

Scripts take paths as arguments; these are only the defaults.
"""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "images"
