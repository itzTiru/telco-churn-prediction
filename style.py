css = """

<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Main background and fonts */
.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
    font-family: 'Inter', sans-serif;
}

/* Container width */
.block-container {
    max-width: 1400px !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
}

/* Header styling */
.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2.5rem 2rem;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}

.main-header h1 {
    color: white;
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.main-header p {
    color: #e0e7ff;
    font-size: 1.1rem;
    margin-top: 0.5rem;
}

/* Input sections */
.input-section {
    background: white;
    padding: 2rem;
    border-radius: 16px;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
}

.section-title {
    color: #667eea;
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 3px solid #667eea;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

/* Style all select boxes and inputs for light theme */
.stSelectbox > div > div {
    background-color: #f9fafb !important;
    border: 2px solid #e5e7eb !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
    color: #1f2937 !important;
}

.stSelectbox > div > div:hover {
    border-color: #667eea !important;
}

.stSelectbox > div > div:focus-within {
    border-color: #667eea !important;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
}

/* Fix select box text color */
.stSelectbox > div > div > div {
    color: #1f2937 !important;
}

/* Fix dropdown menu text color */
.stSelectbox [role="listbox"] {
    background-color: white !important;
}

.stSelectbox [role="option"] {
    color: #1f2937 !important;
    background-color: white !important;
}

.stSelectbox [role="option"]:hover {
    background-color: #f3f4f6 !important;
    color: #1f2937 !important;
}

/* Number input styling */
.stNumberInput > div > div > input {
    background-color: #f9fafb !important;
    border: 2px solid #e5e7eb !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
    color: #1f2937 !important;
}

.stNumberInput > div > div > input:hover {
    border-color: #667eea !important;
}

.stNumberInput > div > div > input:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
}

/* Labels for inputs */
.stSelectbox label, .stNumberInput label {
    color: #374151 !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    margin-bottom: 0.5rem !important;
}

/* Fix any remaining text color issues */
.stSelectbox div[data-baseweb="select"] > div {
    color: #1f2937 !important;
}

/* Currency display */
.currency-display {
    background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
    padding: 0.75rem 1rem;
    border-radius: 8px;
    text-align: center;
    font-weight: 700;
    font-size: 1.3rem;
    color: #667eea;
    margin-top: 0.5rem;
    border: 2px solid #667eea30;
}

/* Prediction result cards */
.prediction-card {
    padding: 2.5rem;
    border-radius: 20px;
    text-align: center;
    margin: 2.5rem 0;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
    animation: slideIn 0.5s ease-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.churn-high {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
}

.churn-low {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
}

.prediction-card h2 {
    font-size: 2.2rem;
    margin-bottom: 1rem;
    font-weight: 700;
}

.prediction-card .probability {
    font-size: 4rem;
    font-weight: 800;
    margin: 1.5rem 0;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

/* Button styling */
.stButton>button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-size: 1.3rem;
    font-weight: 700;
    padding: 1rem 2rem;
    border-radius: 12px;
    border: none;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    transition: all 0.3s ease;
    width: 100%;
    margin-top: 1.5rem;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
}

.stButton>button:active {
    transform: translateY(-1px);
}

/* Info boxes */
.info-box {
    background: linear-gradient(135deg, #e0e7ff 0%, #f0e7ff 100%);
    padding: 1.5rem;
    border-radius: 12px;
    border-left: 5px solid #667eea;
    margin: 1.5rem 0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.info-box strong {
    color: #667eea;
    font-size: 1.1rem;
}

.info-box ul {
    margin-top: 1rem;
    margin-bottom: 0;
}

.info-box li {
    margin: 0.5rem 0;
    color: #4b5563;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    height: 20px;
    border-radius: 10px;
}

/* Metrics styling */
[data-testid="stMetricValue"] {
    font-size: 1.8rem;
    font-weight: 700;
    color: #667eea;
}

[data-testid="stMetricLabel"] {
    font-size: 1rem;
    font-weight: 600;
    color: #6b7280;
}

/* Divider */
hr {
    margin: 2rem 0;
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, #667eea, transparent);
}

/* Footer */
.footer {
    text-align: center;
    color: #6b7280;
    padding: 2rem;
    margin-top: 3rem;
    font-size: 0.9rem;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #667eea !important;
}
</style>

"""