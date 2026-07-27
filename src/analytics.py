#SQL sorguları ve analizler

import pandas as pd
from src.database import engine


def get_total_customers():
    query="""
    SELECT COUNT(*)
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





if __name__ == "__main__":
    print(get_total_customers())
