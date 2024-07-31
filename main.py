import duckdb


def main():
    with duckdb.connect() as conn:
        conn.sql("CREATE TEMPORARY TABLE orders AS SELECT * FROM READ_CSV('orders.csv')")

        # revenue per month
        data = conn.sql(
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
        print(data)

        # revenue per product
        data = conn.sql(
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
        print(data)

        # revenue per customer
        data = conn.sql(
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
        print(data)

        # top 10 customers
        data = conn.sql(
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
        print(data)

if __name__ == '__main__':
    main()
