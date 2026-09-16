import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

def load_orders(path: Path) -> pd.DataFrame:
    orders = pd.read_csv(path)
    logger.info(f"Loaded {len(orders)} orders from {path}")
    return orders
