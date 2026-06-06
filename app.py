"""HF Spaces entry point — imports and runs the backend FastAPI app on port 7860."""

import sys
from pathlib import Path

# Make backend package importable
sys.path.insert(0, str(Path(__file__).parent / "backend"))

from app import app  # noqa: F401  (re-exported for uvicorn)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
