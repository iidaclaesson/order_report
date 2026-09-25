import pandas as pd
import pytest

from order_report.processing import prepare_orders

def test_order_values_are_calculated():
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

    result = prepare_orders(orders)

    assert result["order_value"].tolist() == [1598]
    assert result["discounted_value"].tolist() == pytest.approx([1358.3])


def test_returned_becomes_true_or_false():
    orders = pd.DataFrame(
        {
            "order_id": [1, 2],
            "order_date": ["2026-01-01", "2026-02-01"],
            "customer_id": [1, 2],
            "region": ["South", "North"],
            "product_category": ["Electronics", "Home"],
            "quantity": [2, 1],
            "unit_price": [799, 199],
            "discount": [0.15, 0.1],
            "returned": ["yes", "no"],
            }
    )
    result = prepare_orders(orders)

    assert result["returned"].tolist() == [True, False]