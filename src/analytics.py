#SQL sorguları ve analizler

import pandas as pd
from src.database import engine


def get_total_customers():
    query="""
    SELECT COUNT(DISTINCT customer_unique_id)
    AS 
    total_customers
    FROM customers

    """
    df= pd.read_sql_query(query, con=engine)
    return df.loc[0, "total_customers"] 

# 0. satırdaki total_customers sütununun değerini alır.
# KPI kartında DataFrame yerine yalnızca sayı gerektiği için loc kullandık.
# loc olmasaydı çıktı tek satırlık bir DataFrame olurdu:
#    total_customers
# 0            96096



def get_total_orders():
    query="""
    SELECT COUNT(*)
    AS
    total_orders
    FROM orders

    """
    df=pd.read_sql_query(query,con=engine)
    return df.loc[0,"total_orders"]






def get_total_sales():
    query="""
    SELECT SUM(payment_value)
    AS
    total_sales
    FROM order_payments

    """
    df=pd.read_sql_query(query,con=engine)
    return df.loc[0,"total_sales"]





def get_avg_review_score():
    query="""
    SELECT ROUND(AVG(review_score),2)
    AS
    avg_review_score
    FROM order_reviews

    """
    df=pd.read_sql_query(query,con=engine)
    return df.loc[0,"avg_review_score"]




def get_monthly_sales():
    query="""

    SELECT DATE_TRUNC('month',o.order_purchase_timestamp) AS month,
    SUM (op.payment_value) AS monthly_sales
    FROM orders o
    JOIN order_payments op
    ON o.order_id=op.order_id
    WHERE o.order_purchase_timestamp < '2018-09-01'
    GROUP BY DATE_TRUNC('month',o.order_purchase_timestamp)
    ORDER BY month

    """

    df=pd.read_sql_query(query,con=engine)
    return df


def get_top_10_categories():
    query="""
    SELECT p.product_category_name, COUNT(*) AS order_count
    FROM order_items oi
    JOIN products p
    ON oi.product_id=p.product_id
    GROUP BY p.product_category_name
    ORDER BY order_count DESC
    LIMIT 10

    """

    df=pd.read_sql_query(query,con=engine)
    return df













if __name__ == "__main__":
    print("Toplam müşteri:", get_total_customers())
    print("Toplam sipariş:", get_total_orders())
    print("Toplam satış:", get_total_sales())
    print("Ortalama puan:", get_avg_review_score())
    print(get_monthly_sales().head())
    print(get_top_10_categories())

