
import pandas as pd
import logging

from order_report.config import ReportConfig
from order_report.loading import load_orders
from order_report.processing import (
  build_overview,
  prepare_orders,
  summarize_returns,
  summarize_sales  
)
from order_report.reporting import save_report
from order_report.validation import validate_orders

logger = logging.getLogger(__name__)

def configure_logging() -> None:
    logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
)

config = ReportConfig()

orders = load_orders()