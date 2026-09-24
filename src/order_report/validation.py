import pandas as pd
import logging

logger = logging.getLogger(__name__)


REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
    }
def validate_orders(orders: pd.DataFrame) -> None:
    missing_columns = REQUIRED_COLUMNS.difference(orders.columns)

    if missing_columns:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing_columns))}")
    if orders.empty:
        raise ValueError("The file has columns but no rows")
    logger.info("Validation successful: All %s required columns are present.", len(REQUIRED_COLUMNS))
