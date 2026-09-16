import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)


def save_report(report: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(
        path,
        index=False,
    )
    logger.info(f"Saved report to {path}")
