import duckdb


def get_revenue_per_month() -> duckdb.duckdb.DuckDBPyRelation:
    with duckdb.connect() as conn:
        return conn.sql(
            """
            SELECT
                MONTH(order_date) as month,
                ROUND(SUM(product_price), 2) as revenue
            FROM
                READ_CSV('orders.csv')
            GROUP BY
                MONTH(order_date)
            ORDER BY
                month
            """
        )

def get_revenue_per_product() -> duckdb.duckdb.DuckDBPyRelation:
    with duckdb.connect() as conn:
        return conn.sql(
            """
            SELECT
                product_id,
                ROUND(SUM(product_price), 2) as revenue
            FROM
                READ_CSV('orders.csv')
            GROUP BY
                product_id
            """
        )

def get_revenue_per_customer() -> duckdb.duckdb.DuckDBPyRelation:
    with duckdb.connect() as conn:
        return conn.sql(
            """
            SELECT
                customer_id,
                ROUND(SUM(product_price), 2) as revenue
            FROM
                READ_CSV('orders.csv')
            GROUP BY
                customer_id
            """
        )

def get_top_10_customers() -> duckdb.duckdb.DuckDBPyRelation:
    with duckdb.connect() as conn:
        return conn.sql(
            """
            SELECT
                customer_id,
                ROUND(SUM(product_price), 2) as revenue
            FROM
                READ_CSV('orders.csv')
            GROUP BY
                customer_id
            ORDER BY
                revenue DESC
            LIMIT
                10
            """
        )

def main():
    print(get_revenue_per_month())
    # print(get_revenue_per_customer())
    # print(get_revenue_per_product)
    # print(get_top_10_customers())

if __name__ == '__main__':
    main()
