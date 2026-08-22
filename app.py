import streamlit as st

st.set_page_config(
    page_title="BMW DealCheck",
    page_icon="🚗",
    layout="wide"
)

# =========================
# STYLE
# =========================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 50% 0%, rgba(35,115,255,0.16), transparent 35%),
        linear-gradient(180deg, #05070b 0%, #090d14 55%, #05070b 100%);
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 35px;
    padding-bottom: 60px;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

/* HERO */

.hero-title {
    text-align: center;
    font-size: 64px;
    font-weight: 800;
    letter-spacing: -3px;
    margin-bottom: 5px;
}

.hero-title span {
    color: #3d8bff;
}

.hero-subtitle {
    text-align: center;
    color: #8994a5;
    font-size: 17px;
    max-width: 650px;
    margin: 0 auto 35px auto;
}

/* LOGO */

.logo-circle {
    width: 78px;
    height: 78px;
    border-radius: 50%;
    margin: 0 auto 18px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(145deg, #111822, #070a0f);
    border: 1px solid rgba(75,145,255,0.4);
    box-shadow: 0 0 35px rgba(45,125,255,0.18);
    font-size: 25px;
    font-weight: 800;
    color: white;
}

/* CARDS */

.section {
    background: rgba(15,20,29,0.88);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
}

.section-title {
    font-size: 21px;
    font-weight: 750;
}

.section-subtitle {
    color: #7f8998;
    font-size: 14px;
    margin-top: 4px;
    margin-bottom: 20px;
}

/* INPUTS */

label {
    color: #d8dee8 !important;
    font-weight: 600 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: #10151d !important;
    border-color: #28313e !important;
    border-radius: 10px !important;
}

input {
    color: white !important;
}

/* BUTTON */

.stButton > button {
    height: 58px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(100deg, #1468ff, #4b92ff);
    color: white;
    font-size: 17px;
    font-weight: 800;
    box-shadow: 0 12px 30px rgba(20,105,255,0.22);
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* RESULT */

.result-box {
    background:
        radial-gradient(circle at 90% 10%, rgba(40,130,255,0.16), transparent 35%),
        linear-gradient(145deg, #151d2a, #080c12);
    border: 1px solid rgba(70,145,255,0.25);
    border-radius: 24px;
    padding: 30px;
    margin-top: 30px;
}

.small-label {
    color: #7e8999;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
}

.price {
    font-size: 38px;
    font-weight: 800;
    margin-top: 5px;
}

.score {
    font-size: 62px;
    font-weight: 800;
    color: #4b91ff;
}

.score-bar {
    width: 100%;
    height: 9px;
    background: #242c38;
    border-radius: 20px;
    overflow: hidden;
    margin-top: 10px;
}

.score-fill {
    height: 100%;
    background: linear-gradient(90deg, #1265ff, #5ca0ff);
    border-radius: 20px;
}

.good {
    color: #35d58b;
}

.fair {
    color: #ffc857;
}

.bad {
    color: #ff5c68;
}

.verdict {
    font-size: 26px;
    font-weight: 800;
    margin-top: 20px;
}

/* CHECKLIST */

.check {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 13px;
    padding: 16px;
    margin-bottom: 10px;
}

.check-title {
    font-weight: 700;
}

.check-text {
    color: #858f9e;
    font-size: 13px;
    margin-top: 3px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #555f6e;
    font-size: 11px;
    margin-top: 45px;
    line-height: 1.7;
}

@media (max-width: 700px) {
    .hero-title {
        font-size: 43px;
        letter-spacing: -2px;
    }

    .price {
        font-size: 29px;
    }

    .score {
        font-size: 52px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================
# HERO
# =========================

st.markdown(
    '<div class="logo-circle">BMW</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">BMW <span>DealCheck</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Find out whether a BMW listing looks like a great deal, '
    'a fair price, or one you should negotiate.'
    '</div>',
    unsafe_allow_html=True
)


# =========================
# VEHICLE DETAILS
# =========================

st.markdown(
    '<div class="section">'
    '<div class="section-title">Vehicle Details</div>'
    '<div class="section-subtitle">'
    'Enter the information from the BMW listing.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2, gap="large")

with left:

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

with right:

    asking = st.number_input(
        "Asking price ($)",
        min_value=1000,
        max_value=1000000,
        value=50000,
        step=500
    )

    condition = st.select_slider(
        "Overall condition",
        options=[
            "Poor",
            "Fair",
            "Good",
            "Excellent"
        ],
        value="Good"
    )

    accident = st.selectbox(
        "Accident history",
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


# =========================
# ANALYZE
# =========================

if st.button(
    "Analyze My BMW  →",
    use_container_width=True
):

    base_values = {
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
    }

    base = base_values[model]

    age = max(0, 2026 - year)

    estimated = base * (0.87 ** age)

    mileage_factor = max(
        0.65,
        min(
            1.10,
            1.05 - max(0, mileage - 12000) / 100000
        )
    )

    condition_factor = {
        "Poor": 0.82,
        "Fair": 0.92,
        "Good": 1.00,
        "Excellent": 1.06
    }[condition]

    accident_factor = {
        "None reported": 1.00,
        "One or more reported": 0.88,
        "Unknown": 0.96
    }[accident]

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

    if ratio <= 0.92:
        verdict = "GOOD DEAL"
        verdict_class = "good"
    elif ratio <= 1.05:
        verdict = "FAIR DEAL"
        verdict_class = "fair"
    else:
        verdict = "OVERPRICED"
        verdict_class = "bad"

    difference = asking - fair_value


    # =========================
    # VEHICLE SUMMARY
    # =========================

    st.markdown(
        '<div class="section">'
        '<div class="section-title">Your BMW</div>'
        '<div class="section-subtitle">'
        'What we analyzed'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:
        st.metric("Vehicle", f"{year} {model}")

    with b:
        st.metric("Mileage", f"{mileage:,} mi")

    with c:
        st.metric("Asking", f"${asking:,.0f}")


    # =========================
    # RESULTS
    # =========================

    st.markdown(
        '<div class="result-box">'
        '<div class="small-label">DealCheck Result</div>'
        '</div>',
        unsafe_allow_html=True
    )

    r1, r2 = st.columns(2)

    with r1:

        st.markdown(
            '<div class="small-label">Estimated Fair Value</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="price">'
            f'${fair_value * 0.93:,.0f} – '
            f'${fair_value * 1.07:,.0f}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.caption("Estimated market range")

    with r2:

        st.markdown(
            '<div class="small-label">Deal Score</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="score">{score}/100</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="score-bar">'
            f'<div class="score-fill" '
            f'style="width:{score}%"></div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div class="verdict {verdict_class}">'
        f'{verdict}'
        f'</div>',
        unsafe_allow_html=True
    )


    # =========================
    # PRICE DIFFERENCE
    # =========================

    if difference >= 0:

        st.warning(
            f"The asking price is approximately "
            f"${difference:,.0f} above the estimated fair value."
        )

    else:

        st.success(
            f"The asking price is approximately "
            f"${abs(difference):,.0f} below the estimated fair value."
        )


    # =========================
    # CHECKLIST
    # =========================

    st.markdown(
        '<div class="section">'
        '<div class="section-title">Before You Buy</div>'
        '<div class="section-subtitle">'
        'A good price does not automatically mean it is a good car.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    checklist = [
        (
            "Vehicle history",
            "Check accident history, title status and ownership."
        ),
        (
            "Pre-purchase inspection",
            "Have an independent mechanic inspect the vehicle."
        ),
        (
            "Service records",
            "Look for consistent maintenance and documented repairs."
        ),
        (
            "Tires & brakes",
            "Check remaining tread and brake condition."
        ),
        (
            "Options & packages",
            "Verify engine, drivetrain and major options."
        )
    ]

    for title, description in checklist:

        st.markdown(
            f'<div class="check">'
            f'<div class="check-title">✓ {title}</div>'
            f'<div class="check-text">{description}</div>'
            f'</div>',
            unsafe_allow_html=True
        )


# =========================
# FOOTER
# =========================

st.markdown(
    '<div class="footer">'
    'BMW DealCheck is an independent educational tool and is not '
    'affiliated with or endorsed by BMW AG.<br><br>'
    'Estimates are not professional appraisals. Actual values can '
    'vary based on location, options, condition, history and market demand.'
    '<br><br>'
    'BMW DealCheck • MVP'
    '</div>',
    unsafe_allow_html=True
)
