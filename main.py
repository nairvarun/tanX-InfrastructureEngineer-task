import duckdb


def main():
    with duckdb.connect() as conn:
        conn.sql("CREATE TEMPORARY TABLE orders AS SELECT * FROM READ_CSV('orders.csv')")

        revenue_per_month =  conn.sql(
            """
            SELECT
                MONTH(order_date) as month,
                ROUND(SUM(product_price), 2) as revenue
            FROM
                orders
            GROUP BY
                MONTH(order_date)
            ORDER BY
                month
            """
        )
        print(revenue_per_month)

        revenue_per_product = conn.sql(
            """
            SELECT
                product_id,
                ROUND(SUM(product_price), 2) as revenue
            FROM
                orders
            GROUP BY
                product_id
            """
        )
        print(revenue_per_product)

        revenue_per_customer = conn.sql(
            """
            SELECT
                customer_id,
                ROUND(SUM(product_price), 2) as revenue
            FROM
                orders
            GROUP BY
                customer_id
            """
        )
        print(revenue_per_customer)

        top_10_customers = conn.sql(
            """
            SELECT
                customer_id,
                ROUND(SUM(product_price), 2) as revenue
            FROM
                orders
            GROUP BY
                customer_id
            ORDER BY
                revenue DESC
            LIMIT
                10
            """
        )
        print(top_10_customers)

if __name__ == '__main__':
    main()
