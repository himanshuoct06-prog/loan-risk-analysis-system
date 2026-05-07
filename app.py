import streamlit as st
import numpy as np

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Loan Risk Analysis System",
    page_icon="🏦",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #0F172A, #1E293B);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Headings */
h1, h2, h3 {
    color: white;
}

/* KPI Cards */
[data-testid="metric-container"] {
    background: linear-gradient(to right, #1D4ED8, #2563EB);
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #3B82F6;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
}

/* KPI Value */
[data-testid="stMetricValue"] {
    color: white !important;
    font-size: 28px;
    font-weight: bold;
}

/* KPI Label */
[data-testid="stMetricLabel"] {
    color: #DBEAFE !important;
}

/* Number Inputs */
.stNumberInput input {
    background-color: #1F2937 !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Button */
div.stButton > button {
    background: linear-gradient(to right, #2563EB, #3B82F6);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    height: 3.2em;
    width: 100%;
    border: none;
}

div.stButton > button:hover {
    background: linear-gradient(to right, #1E40AF, #2563EB);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🏦 Loan Risk System")

page = st.sidebar.radio(
    "Navigation",
    ["📈 KPI & Insights", "🔍 Risk Prediction"]
)

# =========================================================
# MAIN TITLE
# =========================================================

st.title("🏦 Loan Risk Analysis System")

# =========================================================
# KPI PAGE
# =========================================================

if page == "📈 KPI & Insights":

    st.markdown("---")

    st.header("📈 Key Performance Indicators")

    # =====================================================
    # KPI ROW 1
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Total Customers", "51.34K")

    with col2:
        st.metric("💳 Avg Credit Score", "679")

    with col3:
        st.metric("💰 Avg Income", "₹26.44K")

    with col4:
        st.metric("🎂 Avg Age", "34")

    st.markdown("")

    # =====================================================
    # KPI ROW 2
    # =====================================================

    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric("📋 Total Enquiries", "238K")

    with col6:
        st.metric("⚠️ Delinquency Rate", "1.57%")

    with col7:
        st.metric("📉 DPD Rate", "15.57%")

    st.markdown("---")

    # =====================================================
    # BUSINESS INSIGHTS
    # =====================================================

    st.header("📈 Key Business Insights")

    st.success(
        "💳 Customers with higher credit scores show lower loan default probability."
    )

    st.warning(
        "📋 Higher enquiry counts indicate aggressive credit-seeking behavior."
    )

    st.info(
        "💰 Stable income customers generally maintain better repayment behavior."
    )

    st.error(
        "⚠️ Higher delinquency and DPD rates significantly increase financial risk."
    )

    st.success(
        "📉 Lower DPD rates indicate financially stable applicants."
    )

# =========================================================
# RISK PREDICTION PAGE
# =========================================================

elif page == "🔍 Risk Prediction":

    st.markdown("---")

    st.header("🔍 Loan Risk Prediction System")

    st.write("Enter customer financial details")

    # =====================================================
    # INPUT SECTION
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        credit_score = st.number_input(
            "💳 Credit Score",
            min_value=300,
            max_value=900,
            value=650,
            step=10
        )

        income = st.number_input(
            "💰 Monthly Income",
            min_value=0,
            max_value=200000,
            value=30000,
            step=5000
        )

        enquiries = st.number_input(
            "📋 Total Enquiries",
            min_value=0,
            max_value=20,
            value=2,
            step=1
        )

    with col2:

        delinquency_count = st.number_input(
            "⚠️ Delinquency Count",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )

        dpd_rate = st.number_input(
            "📉 DPD Rate (%)",
            min_value=0,
            max_value=100,
            value=10,
            step=1
        )

    st.markdown("")

    # =====================================================
    # PREDICTION BUTTON
    # =====================================================

    if st.button("🚀 Predict Loan Risk"):

        # =================================================
        # BALANCED RISK LOGIC
        # =================================================

        # LOW RISK
        if (
            credit_score >= 750 and
            income >= 50000 and
            enquiries <= 2 and
            delinquency_count <= 1 and
            dpd_rate <= 15
        ):
            pred = 1

        # MEDIUM RISK
        elif (
            credit_score >= 650 and
            income >= 30000 and
            enquiries <= 5 and
            delinquency_count <= 3 and
            dpd_rate <= 35
        ):
            pred = 2

        # HIGH RISK
        elif (
            credit_score >= 500 and
            income >= 15000 and
            enquiries <= 8 and
            delinquency_count <= 6 and
            dpd_rate <= 65
        ):
            pred = 3

        # VERY HIGH RISK
        else:
            pred = 4

        st.markdown("---")

        # =================================================
        # RESULT SECTION
        # =================================================

        if pred == 1:

            st.success("🟢 LOW RISK CUSTOMER")

            st.write("✅ Strong repayment capability")

            st.write("✅ Loan approval recommended")

            st.write("✅ Very low default probability")

        elif pred == 2:

            st.warning("🟡 MEDIUM RISK CUSTOMER")

            st.write("⚠️ Moderate financial risk detected")

            st.write("⚠️ Additional verification required")

            st.write("⚠️ Moderate default probability")

        elif pred == 3:

            st.error("🟠 HIGH RISK CUSTOMER")

            st.write("🚨 High financial instability detected")

            st.write("🚨 High probability of default")

            st.write("🚨 Careful approval recommended")

        else:

            st.error("🔴 VERY HIGH RISK CUSTOMER")

            st.write("❌ Severe financial instability detected")

            st.write("❌ Loan rejection recommended")

            st.write("❌ Extremely high default probability")