"""Summarize fictional sales records from a CSV file.

Run:
    python sales_summary.py

Uses only the Python standard library.
"""

import csv
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path(__file__).with_name("sales.csv")


def summarize_sales(csv_path):
    """Return total revenue, revenue by product, and row count."""
    totals_by_product = defaultdict(float)
    total_revenue = 0.0
    row_count = 0

    with csv_path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"product", "quantity", "unit_price"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(
                f"CSV must contain columns: {', '.join(sorted(required))}"
            )

        for line_number, row in enumerate(reader, start=2):
            try:
                quantity = int(row["quantity"])
                unit_price = float(row["unit_price"])
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"Invalid quantity or unit_price on line {line_number}"
                ) from exc

            if quantity < 0 or unit_price < 0:
                raise ValueError(f"Negative quantity or price on line {line_number}")

            revenue = quantity * unit_price
            totals_by_product[row["product"]] += revenue
            total_revenue += revenue
            row_count += 1

    return total_revenue, totals_by_product, row_count


def main():
    try:
        total, product_totals, rows = summarize_sales(DATA_FILE)
    except (OSError, ValueError) as error:
        print(f"Could not summarize sales: {error}")
        return

    print("SALES SUMMARY")
    print("-" * 36)
    print(f"Transactions: {rows}")
    print(f"Total revenue: {total:,.2f}")
    print("\nRevenue by product:")

    for product, revenue in sorted(
        product_totals.items(), key=lambda item: item[1], reverse=True
    ):
        print(f"  {product:15} {revenue:,.2f}")


if __name__ == "__main__":
    main()
