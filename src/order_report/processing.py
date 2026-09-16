import logging
import pandas as pd

logger = logging.getLogger(__name__)

def prepare_orders(orders: pd.DataFrame) -> pd.DataFrame:
    prepared = orders.copy()
    prepared["region"] = prepared["region"].fillna("Unknown").astype(str).str.strip().str.title()
    prepared["product_category"] = (
        prepared["product_category"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    prepared["quantity"] = pd.to_numeric(
        prepared["quantity"], errors="coerce"
    ).fillna(1)

    prepared["unit_price"] = pd.to_numeric(
        prepared["unit_price"], errors="coerce"
    )
    prepared["unit_price"] = prepared["unit_price"].fillna(
        prepared["unit_price"].median()
    )

    prepared["discount"] = pd.to_numeric(
        prepared["discount"], errors="coerce"
    ).fillna(0)

    prepared["returned"] = (
        prepared["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )
    prepared["order_value"] = (
        prepared["quantity"] * prepared["unit_price"]
        )
    
    prepared["discounted_value"] = (
        prepared["order_value"] * (1 - prepared["discount"])
        )
    return prepared


def build_overview(orders: pd.DataFrame) -> pd.DataFrame:
    total_sales = round(
        orders["discounted_value"].sum(),
        2,
    )

    number_of_orders = orders["order_id"].nunique()
    number_of_returns = int(orders["returned"].sum())

    overview = pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )
    return overview


def summarize_sales(orders: pd.DataFrame, group_column: str) -> pd.DataFrame:
    summary = (
        orders.groupby(
            group_column,
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    summary["total_sales"] = (
        summary["total_sales"].round(2)
    )

    summary["return_rate"] = (
        summary["returns"]
        / summary["order_count"]
    ).round(3)

    summary = (
        summary
        .sort_values(
            "total_sales",
            ascending=False,
        )
        .reset_index(drop=True)
    )
    return summary


def summarize_returns(orders: pd.DataFrame, group_column: str) -> pd.DataFrame:
    returns_summary = (
        orders.groupby(
            group_column,
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    returns_summary["return_rate"] = (
        returns_summary["returns"]
        / returns_summary["order_count"]
    ).round(3)

    returns_summary = (
        returns_summary
        .sort_values(
            "return_rate",
            ascending=False,
        )
        .reset_index(drop=True)
    )
    return returns_summary