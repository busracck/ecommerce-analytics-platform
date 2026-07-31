import streamlit as st


def show_header():
    st.html("""
    <div class="dashboard-header">
        <div>
            <p class="header-label">E-COMMERCE INTELLIGENCE</p>

            <h1 class="dashboard-title">
                E-Commerce Analytics
            </h1>

            <p class="dashboard-description">
                Satış, müşteri davranışları ve sipariş performansını
                tek ekrandan inceleyin.
            </p>
        </div>

        <div class="header-icon">
            📊
        </div>
    </div>
    """)


def show_kpi_cards(
    total_customers,
    total_orders,
    total_sales,
    avg_review_score,
):
    st.html(f"""
    <div class="kpi-grid">

        <div class="kpi-card">
            <div class="kpi-top">
                <span class="kpi-label">Toplam Müşteri</span>
                <span class="kpi-icon">👥</span>
            </div>

            <div class="kpi-value">
                {total_customers:,}
            </div>

            <div class="kpi-note">
                Sistemdeki toplam müşteri
            </div>
        </div>

        <div class="kpi-card">
            <div class="kpi-top">
                <span class="kpi-label">Toplam Sipariş</span>
                <span class="kpi-icon">📦</span>
            </div>

            <div class="kpi-value">
                {total_orders:,}
            </div>

            <div class="kpi-note">
                Tamamlanan toplam sipariş
            </div>
        </div>

        <div class="kpi-card">
            <div class="kpi-top">
                <span class="kpi-label">Toplam Satış</span>
                <span class="kpi-icon">💰</span>
            </div>

            <div class="kpi-value">
                R$ {total_sales:,.2f}
            </div>

            <div class="kpi-note">
                Toplam satış geliri
            </div>
        </div>

        <div class="kpi-card">
            <div class="kpi-top">
                <span class="kpi-label">Ortalama Puan</span>
                <span class="kpi-icon">⭐</span>
            </div>

            <div class="kpi-value">
                {avg_review_score:.2f}
            </div>

            <div class="kpi-note">
                Müşteri değerlendirme ortalaması
            </div>
        </div>

    </div>
    """)