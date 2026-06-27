import os
import pickle
import numpy as np
import pandas as pd
import streamlit as st

# Set page configuration with a premium look
st.set_page_config(
    page_title="FinShield | Digital Banking Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Resolve paths relative to this script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")
FEATURE_COLS_PATH = os.path.join(BASE_DIR, "feature_columns.pkl")
NUMERIC_COLS_PATH = os.path.join(BASE_DIR, "numeric_columns.pkl")
CATEGORICAL_OPTS_PATH = os.path.join(BASE_DIR, "categorical_options.pkl")
STATE_CITY_MAP_PATH = os.path.join(BASE_DIR, "state_city_mapping.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "fraud_model.pkl")

# Inject premium custom CSS (Dark-themed glassmorphic UI)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #161a24 100%);
        color: #f0f2f6;
    }
    
    /* Premium Title Banner */
    .title-banner {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .title-banner h1 {
        color: #ffffff;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .title-banner p {
        color: #d1d8e0;
        font-size: 1.1rem;
        font-weight: 300;
    }
    
    /* Card containers */
    .section-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 1.8rem;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.2);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .section-card:hover {
        border-color: rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 30px 0 rgba(0, 0, 0, 0.3);
        transform: translateY(-2px);
    }
    
    .section-header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #4a90e2;
        margin-bottom: 1.2rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        padding-bottom: 0.5rem;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #4a90e2 0%, #357abd 100%);
        color: #ffffff !important;
        border: none;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        font-size: 1.1rem;
        border-radius: 8px;
        box-shadow: 0 4px 15px 0 rgba(74, 144, 226, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #357abd 0%, #2a5298 100%);
        box-shadow: 0 6px 20px 0 rgba(74, 144, 226, 0.4);
        transform: translateY(-1px);
    }
    
    /* Risk Cards styling */
    .risk-card {
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 25px 0 rgba(0,0,0,0.25);
        border: 1px solid;
    }
    
    .risk-high {
        background: rgba(235, 94, 85, 0.1);
        border-color: rgba(235, 94, 85, 0.4);
        color: #ff6b6b;
    }
    
    .risk-low {
        background: rgba(46, 213, 115, 0.1);
        border-color: rgba(46, 213, 115, 0.4);
        color: #2ed573;
    }
    
    .risk-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .factor-item {
        background: rgba(255, 255, 255, 0.02);
        padding: 0.6rem 1rem;
        border-radius: 6px;
        margin-bottom: 0.5rem;
        border-left: 3px solid #4a90e2;
        font-size: 0.95rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Helper function to safely load pickle files
def load_pickle(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    return None

# Load metadata files
scaler = load_pickle(SCALER_PATH)
feature_columns = load_pickle(FEATURE_COLS_PATH)
numeric_columns = load_pickle(NUMERIC_COLS_PATH)
categorical_options = load_pickle(CATEGORICAL_OPTS_PATH)
state_city_mapping = load_pickle(STATE_CITY_MAP_PATH)
model = load_pickle(MODEL_PATH)

# Main Dashboard Title
st.markdown(
    """
    <div class="title-banner">
        <h1>🛡️ FinShield Risk Engine</h1>
        <p>Real-Time Digital Banking Transaction Fraud Detection & Threat Assessment</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Check if model or scaling metadata is missing
if model is None or scaler is None or feature_columns is None or categorical_options is None:
    st.markdown(
        """
        <div class="section-card">
            <h2 style="color: #ffb300; font-weight: 600;">⚠️ Model Pipeline Not Fully Loaded</h2>
            <p>The machine learning model files were not found. This app requires the trained model and preprocessing scaler files to run predictions.</p>
            <p>Please execute the notebooks in <b>Google Colab</b> first to train the models and generate the required files, as described in the <b>Colab_Instructions.md</b> file in the workspace.</p>
            <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; border-left: 4px solid #ffb300;">
                <b>Expected files in <code>Streamlit-app/</code>:</b>
                <ul>
                    <li><code>fraud_model.pkl</code> (Trained Model)</li>
                    <li><code>scaler.pkl</code> (Standard Scaler)</li>
                    <li><code>feature_columns.pkl</code> (One-Hot Columns list)</li>
                    <li><code>numeric_columns.pkl</code> (Numerical Column list)</li>
                    <li><code>categorical_options.pkl</code> (Unique values for dropdowns)</li>
                </ul>
            </div>
            <br>
            <p>Once you run the pipeline in Colab, download these files from Colab's file explorer and save them in the <code>Streamlit-app/</code> directory of your local workspace, then refresh this page.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    # We are ready to accept inputs and predict!
    # Create input form inside layout columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div class="section-card"><div class="section-header">👤 Customer Profile</div>',
            unsafe_allow_html=True,
        )
        age = st.slider("Customer Age", min_value=18, max_value=70, value=35)
        gender = st.selectbox("Gender", options=categorical_options.get("Gender", ["Male", "Female"]))
        account_type = st.selectbox("Account Type", options=categorical_options.get("Account_Type", ["Savings", "Business"]))
        account_balance = st.number_input("Account Balance (INR)", min_value=0.0, value=50000.0, step=1000.0, format="%.2f")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="section-card"><div class="section-header">💸 Transaction Details</div>',
            unsafe_allow_html=True,
        )
        tx_amount = st.number_input("Transaction Amount (INR)", min_value=1.0, value=5000.0, step=100.0, format="%.2f")
        tx_type = st.selectbox("Transaction Type", options=categorical_options.get("Transaction_Type", []))
        merchant_category = st.selectbox("Merchant Category", options=categorical_options.get("Merchant_Category", []))
        tx_currency = st.selectbox("Transaction Currency", options=categorical_options.get("Transaction_Currency", []))
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            '<div class="section-card"><div class="section-header">📱 Device & Location</div>',
            unsafe_allow_html=True,
        )
        device = st.selectbox("Transaction Device", options=categorical_options.get("Transaction_Device", []))
        device_type = st.selectbox("Device Type", options=categorical_options.get("Device_Type", []))
        
        # State-City Dynamic Filtering
        state_list = categorical_options.get("State", [])
        selected_state = st.selectbox("State / Region", options=state_list)
        
        # Filter cities based on mapping, fallback to all cities if mapping load failed
        if state_city_mapping and selected_state in state_city_mapping:
            city_options = state_city_mapping[selected_state]
        else:
            city_options = categorical_options.get("City", [])
            
        selected_city = st.selectbox("City", options=city_options)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="section-card"><div class="section-header">📅 Date & Time Metadata</div>',
            unsafe_allow_html=True,
        )
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            hour = st.slider("Hour of Day (0-23)", min_value=0, max_value=23, value=12)
            day_of_month = st.slider("Day of Month", min_value=1, max_value=31, value=15)
        with t_col2:
            day_of_week = st.selectbox("Day of Week", options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
            month = st.selectbox("Month", options=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            
        # Map day of week and month names to integers matching the dataset encoding
        day_of_week_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
        month_map = {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
            "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
        }
        
        day_of_week_int = day_of_week_map[day_of_week]
        month_int = month_map[month]
        st.markdown("</div>", unsafe_allow_html=True)

    # Perform evaluation on submit
    if st.button("🔍 Assess Transaction Risk"):
        with st.spinner("Analyzing transaction telemetry and modeling features..."):
            # 1. Create a zero DataFrame matching the exact training columns
            input_df = pd.DataFrame(0, index=[0], columns=feature_columns)
            
            # 2. Fill Numeric Features
            input_df["Age"] = age
            input_df["Transaction_Amount"] = tx_amount
            input_df["Account_Balance"] = account_balance
            input_df["Transaction_Hour"] = hour
            input_df["Transaction_DayOfWeek"] = day_of_week_int
            input_df["Transaction_Month"] = month_int
            input_df["Transaction_DayOfMonth"] = day_of_month
            
            # 3. Fill Categorical One-Hot Features
            categorical_inputs = {
                "Gender": gender,
                "State": selected_state,
                "City": selected_city,
                "Account_Type": account_type,
                "Transaction_Type": tx_type,
                "Merchant_Category": merchant_category,
                "Transaction_Device": device,
                "Device_Type": device_type,
                "Transaction_Currency": tx_currency,
            }
            
            for col, val in categorical_inputs.items():
                dummy_col = f"{col}_{val}"
                if dummy_col in input_df.columns:
                    input_df[dummy_col] = 1
            
            # 4. Scale Numeric Columns using fit standard scaler
            # Verify order of numeric columns in scaler match this order
            input_df[numeric_columns] = scaler.transform(input_df[numeric_columns])
            
            # 5. Predict using loaded model
            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1]
            
            # Show Assessment Result
            st.markdown("---")
            res_col1, res_col2 = st.columns([1, 1])
            
            with res_col1:
                st.subheader("Analysis Summary")
                st.write(f"**Transaction Amount:** {tx_amount:,.2f} {tx_currency}")
                st.write(f"**Merchant Category:** {merchant_category}")
                st.write(f"**Device Type:** {device_type} (via {device})")
                st.write(f"**Location:** {selected_city}, {selected_state}")
                st.write(f"**Hour of Request:** {hour:02d}:00")
                
                st.markdown("<br><b>Detected Risk Indicators:</b>", unsafe_allow_html=True)
                # Dynamic feedback based on simple rules to enhance UI realism
                factors = []
                if tx_amount > account_balance * 0.8:
                    factors.append("Transaction amount represents a very high proportion of total balance (>80%)")
                if hour >= 23 or hour <= 4:
                    factors.append("Late night/early morning transaction activity")
                if tx_amount > 80000:
                    factors.append("High monetary value transaction")
                if device_type == "Mobile" and tx_type == "Transfer":
                    factors.append("Mobile-initiated direct bank transfer")
                
                if not factors:
                    factors.append("Telemetry inputs match normal transaction baseline profiles")
                    
                for factor in factors:
                    st.markdown(f'<div class="factor-item">{factor}</div>', unsafe_allow_html=True)

            with res_col2:
                st.subheader("Threat Level Assessment")
                if prediction == 1 or probability > 0.5:
                    st.markdown(
                        f"""
                        <div class="risk-card risk-high">
                            <div class="risk-title">High Risk</div>
                            <div style="font-size: 1.2rem; margin-bottom: 1rem;">Suspicion Score: {probability:.1%}</div>
                            <p style="font-size: 0.95rem; margin: 0;"><b>Warning:</b> This transaction shows high patterns matching banking fraud signatures. Manual administrative hold is recommended.</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    risk_label = "Low Risk" if probability < 0.15 else "Medium Risk"
                    risk_class = "risk-low" if probability < 0.15 else "risk-high" # Medium uses warmer tone
                    if probability >= 0.15:
                        border_color = "rgba(255, 179, 0, 0.4)"
                        bg_color = "rgba(255, 179, 0, 0.1)"
                        text_color = "#ffb300"
                    else:
                        border_color = "rgba(46, 213, 115, 0.4)"
                        bg_color = "rgba(46, 213, 115, 0.1)"
                        text_color = "#2ed573"
                        
                    st.markdown(
                        f"""
                        <div class="risk-card" style="background: {bg_color}; border-color: {border_color}; color: {text_color};">
                            <div class="risk-title">{risk_label}</div>
                            <div style="font-size: 1.2rem; margin-bottom: 1rem;">Suspicion Score: {probability:.1%}</div>
                            <p style="font-size: 0.95rem; margin: 0;">Transaction details align with normal account behavior patterns. Processing permitted.</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    
                # Display progress bar as threat probability
                st.markdown("<b>Security Confidence Index:</b>", unsafe_allow_html=True)
                st.progress(float(1.0 - probability))
                st.caption(f"Engine is {1.0 - probability:.1%} confident this transaction is safe.")
