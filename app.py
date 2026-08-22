import streamlit as st

st.set_page_config(
    page_title="BMW DealCheck",
    page_icon="🚗",
    layout="wide"
)

# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, rgba(35,110,255,.20), transparent 35%),
        linear-gradient(180deg, #05070b 0%, #0a0e15 50%, #05070b 100%);
    color: white;
}

.block-container {
    max-width: 1150px;
    padding-top: 25px;
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

/* ================= HERO ================= */

.hero {
    text-align: center;
    padding: 25px 10px 35px;
}

.logo {
    width: 82px;
    height: 82px;
    border-radius: 50%;
    margin-bottom: 18px;
    box-shadow: 0 0 35px rgba(40,120,255,.25);
}

.badge {
    display: inline-block;
    padding: 7px 15px;
    border-radius: 30px;
    border: 1px solid rgba(65,140,255,.5);
    background: rgba(30,90,190,.10);
    color: #75aaff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.hero h1 {
    font-size: clamp(45px, 7vw, 76px);
    font-weight: 850;
    letter-spacing: -4px;
    margin: 12px 0 0;
    line-height: 1;
}

.blue {
    color: #4b91ff;
}

.hero p {
    max-width: 650px;
    margin: 18px auto 0;
    color: #929cab;
    font-size: 16px;
    line-height: 1.6;
}

/* ================= CARDS ================= */

.card {
    background: rgba(15,20,29,.88);
    border: 1px solid rgba(255,255,255,.075);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 18px 50px rgba(0,0,0,.22);
}

.card-title {
    font-size: 21px;
    font-weight: 750;
}

.card-subtitle {
    color: #7e899a;
    font-size: 14px;
    margin-top: 5px;
}

/* ================= INPUTS ================= */

label {
    color: #d5dbe5 !important;
    font-weight: 650 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: #10151e !important;
    border-color: #28313e !important;
    border-radius: 11px !important;
}

div[data-baseweb="input"] input {
    color: white !important;
}

/* ================= BUTTON ================= */

.stButton > button {
    height: 58px;
    border-radius: 13px;
    border: none;
    background: linear-gradient(100deg,#1468ff,#4b91ff);
    color: white;
    font-size: 17px;
    font-weight: 800;
    box-shadow: 0 10px 30px rgba(30,110,255,.25);
    transition: .2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 35px rgba(30,110,255,.38);
}

/* ================= RESULT ================= */

.result-card {
    background:
        radial-gradient(circle at 90% 10%, rgba(45,130,255,.15), transparent 35%),
        linear-gradient(145deg,#151d2a,#080c13);
    border: 1px solid rgba(70,145,255,.25);
    border-radius: 24px;
    padding: 30px;
    margin-top: 30px;
    box-shadow: 0 25px 70px rgba(0,0,0,.35);
}

.result-label {
    color: #7f8b9d;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-size: 11px;
    font-weight: 800;
}

.big-price {
    font-size: 40px;
    font-weight: 850;
    margin-top: 5px;
}

.score-number {
    font-size: 68px;
    font-weight: 900;
    color: #4d91ff;
    line-height: 1;
}

.good {
    color: #36d58b;
}

.fair {
    color: #ffc857;
}

.bad {
    color: #ff5c68;
}

.verdict {
    font-size: 27px;
    font-weight: 850;
    margin-top: 15px;
}

/* ================= SCORE BAR ================= */

.score-bar {
    height: 10px;
    width: 100%;
    background: #222a35;
    border-radius: 20px;
    overflow: hidden;
    margin-top: 15px;
}

.score-fill {
    height: 100%;
    background: linear-gradient(90deg,#1265ff,#54a0ff);
    border-radius: 20px;
}

/* ================= INFO ================= */

.info {
    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.065);
    border-radius: 14px;
    padding: 18px;
    margin-top: 14px;
}

.info-title {
    font-weight: 750;
    color: white;
}

.info-text {
    color: #929dac;
    font-size: 14px;
    margin-top: 5px;
    line-height: 1.5;
}

/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #596373;
    font-size: 11px;
    margin-top: 50px;
    line-height: 1.7;
}

/* ================= MOBILE ================= */

@media(max-width:700px) {

    .hero {
        padding-top: 10px;
    }

    .hero h1 {
        font-size: 45px;
        letter-spacing: -2px;
    }

    .logo {
        width: 70px;
        height: 70px;
    }

    .card,
    .result-card {
        padding: 20px;
    }

    .score-number {
        font-size: 55px;
    }

    .big-price {
        font-size: 30px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <img
        class="logo"
        src="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg"
    >

    <div class="badge">
        INDEPENDENT BMW DEAL ANALYZER
    </div>

    <h1>
        BMW <span class="blue">DealCheck</span>
    </h1>

    <p>
        Analyze a BMW listing in seconds and see whether the asking price
        looks like a <strong>good deal, fair deal, or overpriced.</strong>
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# VEHICLE INFORMATION
# =========================================================

st.markdown("""
<div class="card">
    <div class="card-title">Vehicle Details</div>
    <div class="card-subtitle">
        Enter the information from the listing you're considering.
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
        options=[
            "Poor",
            "Fair",
            "Good",
            "Excellent"
        ],
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


# =========================================================
# ANALYSIS
# =========================================================

if st.button("Analyze BMW Deal  →", use_container_width=True):

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

    age = max(0, 2026 - year)

    estimated = base * (0.87 ** age)

    mileage_factor = max(
        .65,
        min(
            1.10,
            1.05 - max(0, mileage - 12000) / 100000
        )
    )

    condition_factor = {
        "Poor": .82,
        "Fair": .92,
        "Good": 1.00,
        "Excellent": 1.06
    }[condition]

    accident_factor = {
        "None reported": 1.00,
        "One or more reported": .88,
        "Unknown": .96
    }[accident]

    service_factor = {
        "Strong / documented": 1.03,
        "Some records": 1.00,
        "Unknown": .95
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
            round(100 - (ratio - .85) * 180)
        )
    )

    if ratio <= .92:
        verdict = "🟢 GOOD DEAL"
        verdict_class = "good"
    elif ratio <= 1.05:
        verdict = "🟡 FAIR DEAL"
        verdict_class = "fair"
    else:
        verdict = "🔴 OVERPRICED"
        verdict_class = "bad"

    difference = asking - fair_value


    # =====================================================
    # VEHICLE SUMMARY
    # =====================================================

    st.markdown("""
    <div class="card">
        <div class="card-title">Your BMW</div>
        <div class="card-subtitle">
            Vehicle information used in the analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    v1, v2, v3 = st.columns(3)

    with v1:
        st.metric("Model", f"{year} {model}")

    with v2:
        st.metric("Mileage", f"{mileage:,} mi")

    with v3:
        st.metric("Asking Price", f"${asking:,.0f}")


    # =====================================================
    # RESULT
    # =====================================================

    st.markdown("""
    <div class="result-card">
        <div class="result-label">
            DealCheck Result
        </div>
    </div>
    """, unsafe_allow_html=True)

    r1, r2 = st.columns(2, gap="large")

    with r1:

        st.markdown(
            '<div class="result-label">Estimated Fair Value</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="big-price">'
            f'${fair_value*.93:,.0f} – ${fair_value*1.07:,.0f}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "Estimated range based on the information provided."
        )

    with r2:

        st.markdown(
            '<div class="result-label">Deal Score</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="score-number">{score}/100</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="score-bar">
                <div class="score-fill" style="width:{score}%"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div class="verdict {verdict_class}">{verdict}</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # PRICE DIFFERENCE
    # =====================================================

    if difference >= 0:

        message = (
            f"The asking price is approximately "
            f"<strong>${difference:,.0f} above</strong> "
            f"the estimated fair value."
        )

    else:

        message = (
            f"The asking price is approximately "
            f"<strong>${abs(difference):,.0f} below</strong> "
            f"the estimated fair value."
        )

    st.markdown(
        f"""
        <div class="info">
            <div class="info-title">
                💰 Price Analysis
            </div>
            <div class="info-text">
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # BUYER CHECKLIST
    # =====================================================

    st.markdown("""
    <div class="card" style="margin-top:30px;">
        <div class="card-title">
            Before You Buy
        </div>

        <div class="card-subtitle">
            Price is only one part of the deal.
        </div>
    </div>
    """, unsafe_allow_html=True)

    checks = [
        ("Vehicle history", "Check accident history, title status and ownership."),
        ("Pre-purchase inspection", "Have an independent mechanic inspect the vehicle."),
        ("Service records", "Look for consistent maintenance and documented repairs."),
        ("Tires & brakes", "Check remaining tread and brake condition."),
        ("Options", "Verify engine, drivetrain, packages and major options.")
    ]

    for title, description in checks:

        st.markdown(
            f"""
            <div class="info">
                <div class="info-title">
                    ✓ {title}
                </div>

                <div class="info-text">
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

BMW DealCheck is an independent educational tool and is
not affiliated with or endorsed by BMW AG.

<br><br>

Estimates are not professional appraisals and actual vehicle
values can vary based on location, options, condition,
history, market demand and other factors.

<br><br>

BMW DealCheck • MVP

</div>
""", unsafe_allow_html=True)
