import streamlit as st


def load_css():
    st.html("""
    <style>
        .stApp {
            background:
                radial-gradient(
                    circle at top left,
                    rgba(99, 102, 241, 0.12),
                    transparent 32%
                ),
                radial-gradient(
                    circle at top right,
                    rgba(14, 165, 233, 0.10),
                    transparent 28%
                ),
                #f5f7fb;
        }

        .block-container {
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 4rem;
            animation: pageFade 0.7s ease-in-out;
        }

        h1 {
            color: #172554;
            font-weight: 800;
            letter-spacing: -0.8px;
        }

        h2, h3 {
            color: #1e293b;
            font-weight: 700;
        }

        p {
            color: #64748b;
        }

        .dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 28px 32px;
            margin-bottom: 24px;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(148, 163, 184, 0.20);
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(15, 23, 42, 0.08);
            animation: headerSlide 0.8s ease;
        }

        .header-label {
            margin: 0 0 8px 0;
            color: #6366f1;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 2px;
        }

        .dashboard-title {
            margin: 0;
            color: #172554;
            font-size: 42px;
            font-weight: 850;
        }

        .dashboard-description {
            margin: 10px 0 0 0;
            color: #64748b;
            font-size: 16px;
        }

        .header-icon {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 76px;
            height: 76px;
            font-size: 35px;
            background: linear-gradient(135deg, #6366f1, #0ea5e9);
            border-radius: 22px;
            box-shadow: 0 12px 25px rgba(99, 102, 241, 0.28);
        }

        div[data-baseweb="tab-list"] {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 16px;
            padding: 8px;
            background: rgba(255, 255, 255, 0.75);
            border: 1px solid rgba(148, 163, 184, 0.20);
            border-radius: 16px;
            margin-bottom: 20px;
        }

        button[data-baseweb="tab"] {
            height: 50px;
            padding: 0 24px;
            color: #64748b;
            background: transparent;
            border-radius: 12px;
            transition:
                background 0.25s ease,
                color 0.25s ease,
                transform 0.25s ease;
        }

        button[data-baseweb="tab"] p {
            font-size: 17px !important;
            font-weight: 700 !important;
        }

        button[data-baseweb="tab"]:hover {
            background: #eef2ff;
            transform: translateY(-2px);
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(135deg, #6366f1, #0ea5e9);
            box-shadow: 0 8px 20px rgba(99, 102, 241, 0.25);
        }

        button[data-baseweb="tab"][aria-selected="true"] p {
            color: white !important;
        }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin: 24px 0 30px 0;
        }

        .kpi-card {
            position: relative;
            overflow: hidden;
            padding: 22px;
            min-height: 135px;
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(148, 163, 184, 0.20);
            border-radius: 20px;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.07);
            transition:
                transform 0.30s ease,
                box-shadow 0.30s ease,
                border-color 0.30s ease;
            animation: kpiFadeUp 0.60s ease both;
        }

        .kpi-card:nth-child(2) {
            animation-delay: 0.10s;
        }

        .kpi-card:nth-child(3) {
            animation-delay: 0.20s;
        }

        .kpi-card:nth-child(4) {
            animation-delay: 0.30s;
        }

        .kpi-card:hover {
            transform: translateY(-7px);
            box-shadow: 0 20px 42px rgba(99, 102, 241, 0.18);
            border-color: rgba(99, 102, 241, 0.35);
        }

        .kpi-card::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, #6366f1, #0ea5e9);
        }

        .kpi-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }

        .kpi-label {
            color: #64748b;
            font-size: 14px;
            font-weight: 650;
        }

        .kpi-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 42px;
            height: 42px;
            font-size: 20px;
            background: linear-gradient(
                135deg,
                rgba(99, 102, 241, 0.15),
                rgba(14, 165, 233, 0.15)
            );
            border-radius: 13px;
        }

        .kpi-value {
            color: #172554;
            font-size: 27px;
            font-weight: 800;
        }

        .kpi-note {
            margin-top: 8px;
            color: #94a3b8;
            font-size: 12px;
        }

        @keyframes pageFade {
            from {
                opacity: 0;
                transform: translateY(12px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes headerSlide {
            from {
                opacity: 0;
                transform: translateY(-15px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes kpiFadeUp {
            from {
                opacity: 0;
                transform: translateY(18px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 1000px) {
            .kpi-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 600px) {
            .kpi-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """)