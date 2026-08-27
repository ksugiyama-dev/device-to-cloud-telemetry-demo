import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LAMBDA_ROOT = PROJECT_ROOT / "lambda_src" / "telemetry"

sys.path.insert(0, str(LAMBDA_ROOT))