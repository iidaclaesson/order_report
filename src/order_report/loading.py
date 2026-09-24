import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

def load_orders(path: Path) -> pd.DataFrame:
    try:
        orders = pd.read_csv(path)
    except pd.errors.EmptyDataError as error:
        raise ValueError(f"Data file is empty: {path}") from error
    logger.info(f"Loaded {len(orders)} orders from {path}")
    return orders

