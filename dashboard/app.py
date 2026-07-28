import streamlit as st
import plotly.express as px


from src.analytics import (
    get_total_customers,
    get_total_orders,
    get_total_sales,
    get_avg_review_score,
    get_monthly_sales,
    get_top_10_categories,
)


st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("E-Commerce Analytics Dashboard")
st.write("E-ticaret verilerinin genel performans özeti")


total_customers=get_total_customers()
total_orders=get_total_orders()
total_sales=get_total_sales()
avg_review_score=get_avg_review_score()



col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric(
        label="Toplam Müşteri",
        value=f"{total_customers:,}",
    )

with col2:
    st.metric(
        label="Toplam Sipariş",
        value=f"{total_orders:,}",
    )

with col3:
    st.metric(
        label="Toplam Satış",
        value=f"R$ {total_sales:,.2f}",
    )

with col4:
    st.metric(
        label="Ortalama Puan",
        value=f"{avg_review_score:.2f} ⭐",
    )


st.subheader("Aylık Satışlar")
monthly_sales_df=get_monthly_sales()


st.line_chart(
monthly_sales_df,
x="month",
y="monthly_sales"

)



st.subheader("En Çok Satılan 10 Ürün Kategorisi")

top_10_categories_df=get_top_10_categories()

top_10_categories_df["product_category_name"] = (
    top_10_categories_df["product_category_name"]
    .str.replace("_", " ")
    .str.title()
)

fig = px.bar(
    top_10_categories_df,
    x="order_count",
    y="product_category_name",
    orientation="h",
    text="order_count"
)

fig.update_layout(
    yaxis_title="Ürün Kategorisi",
    xaxis_title="Sipariş Sayısı",
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, use_container_width="stretch")