import streamlit as st
import plotly.express as px
from styles import load_css
from components import show_header, show_kpi_cards
from src.ai.schema import get_database_schema
from src.ai.sql_agent import create_sql_prompt
from src.ai.sql_agent import generate_sql, execute_sql
from src.ai.analyst_agent import analyze_data


from src.analytics import (
    get_total_customers,
    get_total_orders,
    get_total_sales,
    get_avg_review_score,
    get_monthly_sales,
    get_top_10_categories,
    get_payment_methods,
    get_review_score_distribution,
    get_orders_by_state,
)


st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)


load_css()
show_header()




total_customers = get_total_customers()
total_orders = get_total_orders()
total_sales = get_total_sales()
avg_review_score = get_avg_review_score()


# En Çok Satılan 10 Ürün Kategorisi

top_10_categories_df = get_top_10_categories()

top_10_categories_df["product_category_name"] = (
    top_10_categories_df["product_category_name"]
    .str.replace("_", " ")
    .str.title()
)

category_fig = px.bar(
    top_10_categories_df,
    x="order_count",
    y="product_category_name",
    orientation="h",
    text="order_count",
)

category_fig.update_layout(
    yaxis_title="Ürün Kategorisi",
    xaxis_title="Sipariş Sayısı",
    yaxis=dict(categoryorder="total ascending"),
)


# Ödeme Metotları

payment_methods_df = get_payment_methods()

payment_fig = px.pie(
    payment_methods_df,
    values="payment_count",
    names="payment_type",
    hole=0.45,
)


# Değerlendirme Puanı Dağılımı

review_score_df = get_review_score_distribution()

review_fig = px.bar(
    review_score_df,
    x="review_score",
    y="review_count",
    text="review_count",
)

review_fig.update_layout(
    xaxis_title="Değerlendirme Puanı",
    yaxis_title="Değerlendirme Sayısı",
)


# Eyaletlere Göre Sipariş Sayısı

orders_by_state_df = get_orders_by_state()

state_fig = px.bar(
    orders_by_state_df,
    x="order_count",
    y="customer_state",
    orientation="h",
    text="order_count",
)

state_fig.update_layout(
    yaxis_title="Eyaletler",
    xaxis_title="Sipariş Sayısı",
    yaxis=dict(categoryorder="total ascending"),
)


tab1, tab2, tab3 = st.tabs([
    "📊 Genel Bakış",
    "📈 Detaylı Analiz",
    "🤖 AI Insights",
])


with tab1:
    show_kpi_cards(
        total_customers,
        total_orders,
        total_sales,
        avg_review_score,
    )

    with st.container(border=True):
        st.subheader("📈 Aylık Satışlar")

        monthly_sales_df = get_monthly_sales()

        st.line_chart(
            monthly_sales_df,
            x="month",
            y="monthly_sales",
        )

    with st.container(border=True):
        st.subheader("🏆 En Çok Satılan 10 Ürün Kategorisi")
        st.plotly_chart(category_fig, width="stretch")


with tab2:
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("💳 Ödeme Yöntemi Dağılımı")
            st.plotly_chart(payment_fig, width="stretch")

    with col2:
        with st.container(border=True):
            st.subheader("⭐ Müşteri Değerlendirme Puanı Dağılımı")
            st.plotly_chart(review_fig, width="stretch")

    with st.container(border=True):
        st.subheader("📍 Eyaletlere Göre Sipariş Sayısı")
        st.plotly_chart(state_fig, width="stretch")


with tab3:
    st.subheader("🤖 AI Veri Analisti")

    question = st.text_input(
        "Sorunuzu yazın"
    )


    if st.button("Analiz Et"):

        if not question.strip():
            st.warning("Lütfen önce bir soru yazın.")

        else:
            try:
                with st.spinner("AI verileri analiz ediyor..."):

                    sql = generate_sql(question)

                    df = execute_sql(sql)

                    if df.empty:
                        analysis = None
                    else:
                        analysis = analyze_data(
                            question,
                            df
                        )

                with st.expander("📝 Oluşturulan SQL'i Göster"):
                    st.code(sql, language="sql")

                st.subheader("📊 Sorgu Sonucu")

                if df.empty:
                    st.info("Bu sorgu için herhangi bir sonuç bulunamadı.")
                else:
                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                    st.subheader("🤖 AI Analizi")
                    st.markdown(analysis)

            except Exception as error:
                st.error(
                    "Analiz sırasında bir hata oluştu."
                )

                with st.expander("Hata detayını göster"):
                    st.code(str(error))



