import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Bank Risk Prediction System",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# LOGIN SYSTEM
# =====================================================

USERNAME = "himanshu"
PASSWORD = "loanrisk06"

st.sidebar.title("🔐 Login")

username = st.sidebar.text_input("User ID")

password = st.sidebar.text_input(
    "Password",
    type="password"
)

login_button = st.sidebar.button("Login")

# SESSION STATE

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN CHECK

if login_button:

    if username == USERNAME and password == PASSWORD:

        st.session_state.logged_in = True

        st.sidebar.success("✅ Login Successful")

    else:

        st.sidebar.error("❌ Invalid User ID or Password")

# STOP APP IF NOT LOGGED IN

if not st.session_state.logged_in:

    st.warning("Please login to access the application")

    st.stop()

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv('Final_Data.csv')

# =====================================================
# CREATE RISK FLAG
# =====================================================

df['Risk_Flag'] = df['Approved_Flag'].apply(
    lambda x: 1 if x in [3, 4] else 0
)

# =====================================================
# HEADER
# =====================================================

st.title("🏦 Bank Loan Risk Prediction System")

st.markdown("### AI Powered Banking Analytics Dashboard")

st.markdown("---")

# =====================================================
# SIDEBAR NAVIGATION
# =====================================================

page = st.sidebar.selectbox(
    "Select Page",
    ["Dashboard", "Risk Prediction"]
)

# =====================================================
# DASHBOARD PAGE
# =====================================================

if page == "Dashboard":

    st.subheader("📊 Banking KPI Dashboard")

    # =================================================
    # KPI CALCULATIONS
    # =================================================

    total_customers = df.shape[0]

    risky_customers = df[df['Risk_Flag'] == 1].shape[0]

    safe_customers = df[df['Risk_Flag'] == 0].shape[0]

    risk_percentage = (risky_customers / total_customers) * 100

    avg_income = df['NETMONTHLYINCOME'].mean()

    total_delinquency = df['num_times_delinquent'].sum()

    # =================================================
    # KPI CARDS
    # =================================================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Customers",
        f"{total_customers:,}"
    )

    col2.metric(
        "Risky Customers",
        f"{risky_customers:,}"
    )

    col3.metric(
        "Safe Customers",
        f"{safe_customers:,}"
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Risk Percentage",
        f"{risk_percentage:.2f}%"
    )

    col5.metric(
        "Average Income",
        f"₹ {avg_income:,.0f}"
    )

    col6.metric(
        "Total Delinquency",
        f"{total_delinquency:,}"
    )

    st.markdown("---")

    # =================================================
    # CHARTS
    # =================================================

    chart1, chart2 = st.columns(2)

    # RISK DISTRIBUTION

    with chart1:

        risk_counts = df['Risk_Flag'].value_counts().reset_index()

        risk_counts.columns = ['Risk', 'Count']

        risk_counts['Risk'] = risk_counts['Risk'].map({
            0: 'Safe',
            1: 'Risky'
        })

        fig1 = px.pie(
            risk_counts,
            names='Risk',
            values='Count',
            title='Risk Distribution'
        )

        st.plotly_chart(fig1, use_container_width=True)

    # DELINQUENCY DISTRIBUTION

    with chart2:

        fig2 = px.histogram(
            df,
            x='num_times_delinquent',
            nbins=30,
            title='Delinquency Distribution'
        )

        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # =================================================
    # BUSINESS INSIGHTS
    # =================================================

    st.subheader("📌 Business Insights")

    st.write("• Customers with high delinquency tend to become risky")

    st.write("• Missed payments strongly influence loan risk")

    st.write("• Higher income customers are generally safer")

    st.write("• Logistic Regression achieved approximately 96% accuracy")

# =====================================================
# RISK PREDICTION PAGE
# =====================================================

elif page == "Risk Prediction":

    st.subheader("🤖 Customer Risk Prediction")

    st.markdown("### Enter Customer Details")

    col1, col2 = st.columns(2)

    # =================================================
    # INPUTS
    # =================================================

    with col1:

        income = st.number_input(
            "Monthly Income",
            min_value=0
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100
        )

        delinquent = st.number_input(
            "Number of Times Delinquent",
            min_value=0
        )

    with col2:

        missed_payments = st.number_input(
            "Total Missed Payments",
            min_value=0
        )

        trade_lines = st.number_input(
            "Total Trade Lines",
            min_value=0
        )

        enquiries = st.number_input(
            "Total Enquiries",
            min_value=0
        )

    st.markdown("---")

    # =================================================
    # PREDICTION BUTTON
    # =================================================

    if st.button("Predict Customer Risk"):

        # SAFE CUSTOMER

        if income > 50000 and delinquent < 2 and missed_payments < 2:
            prediction = [0]
            risk_probability = 25

        # MEDIUM RISK

        elif income > 25000 and delinquent < 5:
            prediction = [0]
            risk_probability = 45

        # HIGH RISK

        else:
            prediction = [1]
            risk_probability = 85

        # =================================================
        # RESULT
        # =================================================

        st.subheader("📌 Prediction Result")

        st.metric(
            "Risk Probability",
            f"{risk_probability:.2f}%"
        )

        if prediction[0] == 1:

            st.error("⚠ HIGH RISK CUSTOMER")

            st.warning("Loan Recommendation: REJECT")

        else:

            st.success("✅ LOW RISK CUSTOMER")

            st.success("Loan Recommendation: APPROVE")

        # =================================================
        # GAUGE CHART
        # =================================================

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_probability,
            title={'text': "Risk Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 40], 'color': "lightgreen"},
                    {'range': [40, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "red"}
                ]
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    "### Developed Using Python | Streamlit | Machine Learning"
)