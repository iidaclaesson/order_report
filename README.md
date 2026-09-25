# Order Report

A refactored version that reads order data from a CSV file, which creates reports on sales and returns per product category and region.

## Setup

Requires Python 3.11 or later.

Create and activate a virtual environment.

```
pip install -r requirements.txt
pip install -e .
```
Installs pandas, pytest and makes `order_report` importable.

## Usage

```
python -m order_report
```
Creates four CSV reports in output/: overview, returns per category, sales by category and sales by region

Run tests:
```
python -m pytest
```

## Structure

```

order_report/
    README.md
    code_review.md
    pyproject.toml
    reflection.md
    requirements.txt
    data/
        orders.csv
    output/
        overview.csv
        returns_by_category.csv
        sales_by_category.csv
        sales_by_region.csv
    src/order_report/
        __init__.py
        __main__.py
        config.py
        loading.py
        processing.py
        reporting.py
        validation.py
    tests/
        test_processing.py
        test_validation.py
    
```