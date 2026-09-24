import pandas as pd
import pytest

from order_report.validation import validate_orders


def test_valid_orders_pass():
    orders = pd.DataFrame(
        {
            "order_id": [1],
            "order_date": ["2026-01-01"],
            "customer_id": [1],
            "region": ["South"],
            "product_category": ["Electronics"],
            "quantity": [2],
            "unit_price": [799],
            "discount": [0.15],
            "returned": ["yes"],
         }
    )

    validate_orders(orders)


def test_missing_column_raises():
    orders = pd.DataFrame({"order_id": [1], "region": ["South"]})

    with pytest.raises(ValueError, match="Missing columns"):
        validate_orders(orders)


def test_empty_orders_raise():
    orders = pd.DataFrame(
        columns=[
            "order_id",
            "order_date",
            "customer_id",
            "region",
            "product_category",
            "quantity",
            "unit_price",
            "discount",
            "returned",
        ]
    )
    with pytest.raises(ValueError, match="no rows"):
        validate_orders(orders)