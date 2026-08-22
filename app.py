import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="BMW DealCheck",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Main page */
    .stApp {
        background:
            radial-gradient(circle at 50% -10%, rgba(30, 80, 180, 0.22), transparent 35%),
            linear-gradient(180deg, #080a0f 0%, #0d1017 45%, #080a0f 100%);
        color: #f5f7fa;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hero */
    .hero {
        text-align: center;
        padding: 35px 20px 30px 20px;
        margin-bottom: 25px;
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 15px;
        border: 1px solid rgba(75, 145, 255, 0.45);
        border-radius: 999px;
        color: #75aaff;
        background: rgba(30, 90, 180, 0.12);
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 1px;
        margin-bottom: 15px;
    }

    .hero-title {
        font-size: clamp(42px, 7vw, 76px);
        font-weight: 800;
        letter-spacing: -3px;
        margin: 0;
        line-height: 0.95;
        color: white;
    }

    .hero-title span {
        color: #4d91ff;
    }

    .hero-subtitle {
        color: #9ba5b5;
        font-size: 17px;
        max-width: 650px;
        margin: 18px auto 0 auto;
        line-height: 1.6;
    }

    /* Cards */
    .card {
        background: rgba(17, 21, 29, 0.86);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 18px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25);
    }

    .card-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 5px;
        color: #ffffff;
    }

    .card-subtitle {
        color: #7f8999;
        font-size: 14px;
        margin-bottom: 18px;
    }

    /* Inputs */
    label {
        color: #cbd2dc !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background-color: #11151d !important;
        border-color: rgba(255,255,255,0.10) !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="input"] input {
        color: white !important;
    }

    /* Analyze button */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        min-height: 54px;
        background: linear-gradient(90deg, #1769ff, #4d91ff);
        color: white;
        font-size: 17px;
        font-weight: 750;
        border: none;
        box-shadow: 0 8px 25px rgba(23, 105, 255, 0.25);
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 32px rgba(23, 105, 255, 0.4);
    }

    /* Result section */
    .result-card {
        background: linear-gradient(
            145deg,
            rgba(24, 31, 44, 0.98),
            rgba(12, 16, 23, 0.98)
        );
        border: 1px solid rgba(77, 145, 255, 0.25);
        border-radius: 22px;
        padding: 30px;
        margin-top: 25px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.35);
    }

    .result-title {
        color: #8995a8;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 12px;
        font-weight: 700;
    }

    .result-value {
        font-size: 38px;
        font-weight: 800;
        color: white;
        margin: 5px 0 15px 0;
    }

    .deal-score {
        font-size: 68px;
        font-weight: 850;
        line-height: 1;
        color: #4d91ff;
    }

    .score-label {
        color: #8e99aa;
        font-size: 13px;
        margin-top: 5px;
    }

    .good {
        color: #35d58a;
    }

    .fair {
        color: #ffc857;
    }

    .bad {
        color: #ff5d67;
    }

    .verdict {
        font-size: 25px;
        font-weight: 800;
        margin-top: 12px;
    }

    /* Info boxes */
    .info-box {
        background: rgba(255,255,255,0.035);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 14px;
        padding: 18px;
        margin-top: 15px;
    }

    .info-title {
        font-weight: 700;
        color: white;
        margin-bottom: 6px;
    }

    .info-text {
        color: #9ca6b5;
        font-size: 14px;
        line-height: 1.5;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #596273;
        font-size: 12px;
        margin-top: 45px;
        line-height: 1.6;
    }

    /* Mobile */
    @media (max-width: 700px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            padding-top: 20px;
        }

        .hero-title {
            letter-spacing: -2px;
        }

        .card,
        .result-card {
            padding: 20px;
        }

        .deal-score {
            font-size: 55px;
        }
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="hero-badge">BMW DEAL ANALYZER</div>

    <h1 class="hero-title">
        BMW <span>DealCheck</span>
    </h1>

    <p class="hero-subtitle">
        Find out whether a BMW asking price looks like a
        <strong>good deal, fair deal, or overpriced.</strong>
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# INPUT CARD
# ---------------------------------------------------------
st.markdown("""
<div class="card">
    <div class="card-title">Vehicle Details</div>
    <div class="card-subtitle">
        Enter the information from the BMW listing you're considering.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    year = st.number_input(
        "Model year",
        min_value=2000,
        max_value=2026,
        value=2022,
        step=1
    )

    mileage = st.number_input(
        "Mileage",
        min_value=0,
        max_value=500000,
        value=40000,
        step=1000
    )

    model = st.selectbox(
        "BMW model",
        [
            "3 Series",
            "5 Series",
            "7 Series",
            "X3",
            "X5",
            "X7",
            "M2",
            "M3",
            "M4",
            "M5"
        ]
    )

with col2:
    asking = st.number_input(
        "Asking price ($)",
        min_value=1000,
        max_value=1000000,
        value=50000,
        step=500
    )

    condition = st.select_slider(
        "Overall condition",
        options=["Poor", "Fair", "Good", "Excellent"],
        value="Good"
    )

    accident = st.selectbox(
        "Known accident history",
        [
            "None reported",
            "One or more reported",
            "Unknown"
        ]
    )

    service = st.selectbox(
        "Service history",
        [
            "Strong / documented",
            "Some records",
            "Unknown"
        ]
    )


# ---------------------------------------------------------
# ANALYSIS
# ---------------------------------------------------------
if st.button("Analyze This BMW  →", type="primary", use_container_width=True):

    # Base estimates for MVP
    base = {
        "3 Series": 32000,
        "5 Series": 43000,
        "7 Series": 58000,
        "X3": 38000,
        "X5": 50000,
        "X7": 65000,
        "M2": 50000,
        "M3": 62000,
        "M4": 65000,
        "M5": 78000
    }[model]

    # Vehicle age
    age = max(0, 2026 - year)

    estimated = base * (0.87 ** age)

    # Mileage adjustment
    mileage_factor = max(
        0.65,
        min(
            1.10,
            1.05 - max(0, mileage - 12000) / 100000
        )
    )

    # Condition adjustment
    condition_factor = {
        "Poor": 0.82,
        "Fair": 0.92,
        "Good": 1.00,
        "Excellent": 1.06
    }[condition]

    # Accident adjustment
    accident_factor = {
        "None reported": 1.00,
        "One or more reported": 0.88,
        "Unknown": 0.96
    }[accident]

    # Service adjustment
    service_factor = {
        "Strong / documented": 1.03,
        "Some records": 1.00,
        "Unknown": 0.95
    }[service]

    fair_value = (
        estimated
        * mileage_factor
        * condition_factor
        * accident_factor
        * service_factor
    )

    ratio = asking / fair_value

    score = max(
        0,
        min(
            100,
            round(100 - (ratio - 0.85) * 180)
        )
    )

    # Verdict
    if ratio <= 0.92:
        label = "Looks like a good deal"
        css_class = "good"
        emoji = "🟢"
    elif ratio <= 1.05:
        label = "Looks roughly fair"
        css_class = "fair"
        emoji = "🟡"
    else:
        label = "Looks expensive"
        css_class = "bad"
        emoji = "🔴"

    difference = asking - fair_value

    # -----------------------------------------------------
    # RESULTS
    # -----------------------------------------------------
    st.markdown("""
    <div class="result-card">
        <div class="result-title">Your BMW Deal Analysis</div>
    </div>
    """, unsafe_allow_html=True)

    r1, r2 = st.columns(2, gap="large")

    with r1:
        st.markdown(
            '<div class="result-title">Estimated Fair Value</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="result-value">'
            f'${fair_value * 0.93:,.0f} – ${fair_value * 1.07:,.0f}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.caption(
            f"Estimated value based on a {year} {model} with "
            f"{mileage:,} miles."
        )

    with r2:
        st.markdown(
            '<div class="result-title">Deal Score</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="deal-score">{score}/100</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="score-label">Overall deal rating</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div class="verdict {css_class}">'
        f'{emoji} {label}'
        f'</div>',
        unsafe_allow_html=True
    )

    # Price difference
    if difference >= 0:
        st.markdown(
            f"""
            <div class="info-box">
                <div class="info-title">Price Check</div>
                <div class="info-text">
                    The asking price is approximately
                    <strong>${difference:,.0f} above</strong>
                    this MVP estimate.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="info-box">
                <div class="info-title">Price Check</div>
                <div class="info-text">
                    The asking price is approximately
                    <strong>${abs(difference):,.0f} below</strong>
                    this MVP estimate.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # BUYER CHECKLIST
    # -----------------------------------------------------
    st.markdown("""
    <div class="card" style="margin-top:25px;">
        <div class="card-title">Before You Buy</div>
        <div class="card-subtitle">
            A good price doesn't automatically mean it's a good car.
        </div>
    </div>
    """, unsafe_allow_html=True)

    checks = [
        ("Vehicle history", "Check accident history, title status, and previous ownership."),
        ("Pre-purchase inspection", "Have an independent mechanic inspect the vehicle."),
        ("Service records", "Look for consistent maintenance and documented repairs."),
        ("Tires & brakes", "Check remaining tread and brake condition."),
        ("Options & configuration", "Verify packages, engine, drivetrain, and major options.")
    ]

    for title, text in checks:
        st.markdown(
            f"""
            <div class="info-box">
                <div class="info-title">✓ {title}</div>
                <div class="info-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    BMW DealCheck is an educational estimate and is not a professional
    appraisal or guarantee of a vehicle's market value.<br>
    Actual pricing can vary based on location, options, condition,
    history, dealer pricing, and current market conditions.
    <br><br>
    BMW DealCheck • MVP
</div>
""", unsafe_allow_html=True)
