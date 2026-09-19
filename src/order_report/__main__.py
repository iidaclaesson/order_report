
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


def main() -> None:
    configure_logging()
    config = ReportConfig()

    try:
        orders = load_orders(config.input_file)
        validate_orders(orders)
        prepared = prepare_orders(orders)

        save_report(
            build_overview(prepared),
            config.output_folder / config.overview_file,
        )

        save_report(
            summarize_sales(prepared, "product_category"),
            config.output_folder / config.sales_by_category_file,
        )

        save_report(
            summarize_sales(prepared, "region"),
            config.output_folder / config.sales_by_region_file,
        )

        save_report(
            summarize_returns(prepared, "product_category"),
            config.output_folder / config.returns_by_category_file,
        )
        logger.info("Report finished")
    except FileNotFoundError:
        logger.error("Input file not found: %s", config.input_file)
        raise SystemExit(1)

    except ValueError as error:
        logger.error("Validation failed: %s", error)
        raise SystemExit(1)

    except Exception:
        logger.exception("Unexpected error building the report")
        raise


if __name__ == "__main__":
    main()
