# Order Report

A refactored version that reads order data from a CSV file, which creates reports on sales and returns per product category and region.

## Setup

Requires Python 3.11 or later.

Create and activate a virtual environment.

```
pip install -r requirements.txt
pip install -e.
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