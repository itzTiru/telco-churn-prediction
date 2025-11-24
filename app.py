import streamlit as st
from style import css
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(css, unsafe_allow_html=True)

@st.cache_resource
def load_model_and_scaler(model_path='Data/churn_model.pkl', scaler_path='Data/scaler.pkl'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

EXPECTED_COLUMNS = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'PaperlessBilling',
    'MonthlyCharges', 'TotalCharges',
    'MultipleLines_No phone service', 'MultipleLines_Yes',
    'InternetService_Fiber optic', 'InternetService_No',
    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
    'OnlineBackup_No internet service', 'OnlineBackup_Yes',
    'DeviceProtection_No internet service', 'DeviceProtection_Yes',
    'TechSupport_No internet service', 'TechSupport_Yes',
    'StreamingTV_No internet service', 'StreamingTV_Yes',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes',
    'Contract_One year', 'Contract_Two year',
    'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
]

def preprocess_input(input_dict: dict, scaler) -> pd.DataFrame:
    df = pd.DataFrame([input_dict])

    #label encoding
    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    le = LabelEncoder()
    for col in binary_cols:
        if col in df.columns:
            df[col] = le.fit_transform(df[col].astype(str))

    #one hot encoding
    multi_cols = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                  'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                  'Contract', 'PaymentMethod']
    df = pd.get_dummies(df, columns=[c for c in multi_cols if c in df.columns], drop_first=True)

    for col in EXPECTED_COLUMNS:
        if col not in df.columns:
            df[col] = 0

    df = df[EXPECTED_COLUMNS].copy()

    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    try:
        df[numeric_cols] = scaler.transform(df[numeric_cols])
    except Exception:
        df[numeric_cols] = scaler.transform(df[numeric_cols].values.reshape(1, -1))

    return df


def main():
    st.markdown("""
        <div class="main-header">
            <h1> Customer Churn Prediction</h1>
        </div>
    """, unsafe_allow_html=True)

    try:
        model, scaler = load_model_and_scaler()
    except FileNotFoundError:
        st.error(" Model or scaler files not found")
        return
    except Exception as e:
        st.error(f"Error loading model/scaler: {e}")
        return

    #Customer Info
    st.markdown('<div class="section-title"> Customer Information</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox('Gender', ["Male", "Female"], help="Select customer's gender")
    with col2:
        SeniorCitizen = st.selectbox('Senior Citizen', 
                                     options=[0, 1], 
                                     format_func=lambda x: "Yes" if x == 1 else "No",
                                     help="Is the customer 65 years or older?")
    with col3:
        tenure = st.number_input('Tenure (Months)', 
                                min_value=0, 
                                max_value=72, 
                                value=12, 
                                help="How long has the customer been with us?")
    
    col4, col5 = st.columns(2)
    with col4:
        Partner = st.selectbox('Has Partner', ["Yes", "No"], help="Does customer have a partner?")
    with col5:
        Dependents = st.selectbox('Has Dependents', ["Yes", "No"], help="Does customer have dependents?")

    #service
    st.markdown('<div class="section-title"> Service Details</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#####  Phone Services")
        PhoneService = st.selectbox('Phone Service', ["Yes", "No"], key="phone")
        MultipleLines = st.selectbox('Multiple Lines', ["Yes", "No", "No phone service"], key="lines")
        
        st.markdown("#####  Internet Services")
        InternetService = st.selectbox('Internet Service Type', ["DSL", "Fiber optic", "No"], key="internet")
        OnlineSecurity = st.selectbox('Online Security', ["Yes", "No", "No internet service"], key="security")
        OnlineBackup = st.selectbox('Online Backup', ["Yes", "No", "No internet service"], key="backup")
    
    with col2:
        st.markdown("#####  Additional Services")
        DeviceProtection = st.selectbox('Device Protection', ["Yes", "No", "No internet service"], key="device")
        TechSupport = st.selectbox('Tech Support', ["Yes", "No", "No internet service"], key="tech")
        
        st.markdown("#####  Streaming Services")
        StreamingTV = st.selectbox('Streaming TV', ["Yes", "No", "No internet service"], key="tv")
        StreamingMovies = st.selectbox('Streaming Movies', ["Yes", "No", "No internet service"], key="movies")

    # Billing
    st.markdown('<div class="section-title"> Billing Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        Contract = st.selectbox('Contract Type', 
                               ["Month-to-month", "One year", "Two year"], 
                               help="Type of customer contract")
        PaperlessBilling = st.selectbox('Paperless Billing', 
                                       ["Yes", "No"], 
                                       help="Does customer use paperless billing?")
        PaymentMethod = st.selectbox('Payment Method', 
            ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
            help="How does the customer pay?")
    
    with col2:
        MonthlyCharges = st.number_input('Monthly Charges ($)', 
                                        min_value=0.0, 
                                        max_value=150.0, 
                                        value=50.0, 
                                        step=0.50,
                                        format="%.2f", 
                                        help="Monthly charges in US Dollars")
        st.markdown(f'<div class="currency-display">${MonthlyCharges:.2f} / month</div>', unsafe_allow_html=True)
        
        TotalCharges = st.number_input('Total Charges ($)', 
                                      min_value=0.0, 
                                      max_value=10000.0, 
                                      value=600.0,
                                      step=10.0,
                                      format="%.2f", 
                                      help="Total charges to date in US Dollars")
        st.markdown(f'<div class="currency-display">${TotalCharges:.2f} total</div>', unsafe_allow_html=True)

    #collect inputs
    user_input = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }

    #pred button
    if st.button(' Predict Churn Probability'):
        try:
            with st.spinner(' Analyzing customer data...'):
                processed = preprocess_input(user_input, scaler)
                pred = model.predict(processed)[0]
                prob = model.predict_proba(processed)[0][1]

            #Display results
            if pred == 1:
                st.markdown(f"""
                    <div class="prediction-card churn-high">
                        <h2> High Churn Risk</h2>
                        <div class="probability">{prob:.1%}</div>
                        <p style="font-size: 1.2rem; font-weight: 500;">This customer is likely to churn. Immediate action recommended!</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="prediction-card churn-low">
                        <h2> Low Churn Risk</h2>
                        <div class="probability">{prob:.1%}</div>
                        <p style="font-size: 1.2rem; font-weight: 500;">This customer is likely to stay. Keep up the great service!</p>
                    </div>
                """, unsafe_allow_html=True)

            # visualization
            st.markdown("---")
            st.markdown("###  Detailed Analysis")
            st.progress(prob, text=f"Churn Probability: {prob:.1%}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(" Churn Risk", 
                         f"{prob:.1%}", 
                         delta=f"{prob - 0.5:.1%}" if prob > 0.5 else f"{0.5 - prob:.1%}",
                         delta_color="inverse")
            with col2:
                risk_level = " High" if prob > 0.7 else " Medium" if prob > 0.3 else " Low"
                st.metric(" Risk Level", risk_level)
            with col3:
                confidence = max(prob, 1-prob)
                st.metric(" Confidence", f"{confidence:.1%}")

            # Recommendations
            if pred == 1:
                st.markdown("---")
                st.markdown("""
                    <div class="info-box">
                        <strong> Recommended Retention Actions:</strong>
                        <ul>
                            <li><strong>Immediate Outreach:</strong> Contact customer within 24-48 hours</li>
                            <li><strong>Personalized Offers:</strong> Provide targeted discounts or upgrade incentives</li>
                            <li><strong>Service Review:</strong> Schedule a service quality assessment call</li>
                            <li><strong>Contract Upgrade:</strong> Offer benefits for longer-term contracts</li>
                            <li><strong>Loyalty Rewards:</strong> Enroll in VIP or loyalty programs</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("---")
                st.markdown("""
                    <div class="info-box">
                        <strong> Customer Retention Tips:</strong>
                        <ul>
                            <li><strong>Maintain Quality:</strong> Continue providing excellent service</li>
                            <li><strong>Engagement:</strong> Send periodic satisfaction surveys</li>
                            <li><strong>Upsell Opportunities:</strong> Introduce new services or features</li>
                            <li><strong>Appreciation:</strong> Consider loyalty appreciation messages</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f" Error during prediction: {str(e)}")
            st.info("ℹ Please check that all inputs are valid and try again.")
            st.exception(e)

    # Footer
    st.markdown("""
        <div class="footer">
            Built with using Streamlit<br>
            <small>© 2025 Customer Analytics Platform</small>
        </div>
    """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()