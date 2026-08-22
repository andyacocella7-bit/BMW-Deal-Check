import streamlit as st

st.set_page_config(
    page_title="BMW DealCheck",
    page_icon="🚗",
    layout="wide"
)

# =========================================================
# PREMIUM DESIGN
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 50% 0%, rgba(30,110,255,.18), transparent 35%),
        linear-gradient(180deg, #05070b 0%, #090d14 55%, #05070b 100%);
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 35px;
    padding-bottom: 60px;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.hero {
    text-align: center;
    margin-bottom: 35px;
}

.logo {
    width: 78px;
    height: 78px;
    margin: auto;
    border-radius: 50%;
    background: linear-gradient(145deg, #182131, #070a0f);
    border: 1px solid rgba(70,145,255,.45);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 20px;
    box-shadow: 0 0 40px rgba(40,120,255,.18);
}

.hero h1 {
    font-size: 62px;
    letter-spacing: -3px;
    margin: 16px 0 5px;
    font-weight: 800;
}

.blue {
    color: #3d8cff;
}

.hero p {
    color: #8994a5;
    font-size: 17px;
    max-width: 680px;
    margin: auto;
}

.card {
    background: rgba(15,20,29,.9);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
}

.card-title {
    font-size: 21px;
    font-weight: 800;
}

.card-sub {
    color: #7f8998;
    font-size: 14px;
    margin-top: 4px;
    margin-bottom: 20px;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: #10151d !important;
    border-color: #293341 !important;
    border-radius: 10px !important;
}

input {
    color: white !important;
}

label {
    color: #d8dee8 !important;
    font-weight: 600 !important;
}

.stButton > button {
    height: 58px;
    border-radius: 13px;
    border: 0;
    background: linear-gradient(100deg,#1265ff,#4c93ff);
    color: white;
    font-size: 17px;
    font-weight: 800;
    box-shadow: 0 12px 30px rgba(20,105,255,.22);
}

.stButton > button:hover {
    transform: translateY(-2px);
}

.result {
    background:
        radial-gradient(circle at 90% 5%,rgba(50,130,255,.18),transparent 35%),
        linear-gradient(145deg,#151d2a,#080c12);
    border: 1px solid rgba(70,145,255,.25);
    border-radius: 24px;
    padding: 30px;
    margin-top: 25px;
}

.label {
    color: #7e8999;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
}

.price {
    font-size: 36px;
    font-weight: 800;
}

.score {
    font-size: 60px;
    font-weight: 800;
    color: #4b91ff;
}

.bar {
    height: 9px;
    background: #242c38;
    border-radius: 20px;
    overflow: hidden;
    margin-top: 8px;
}

.fill {
    height: 100%;
    background: linear-gradient(90deg,#1265ff,#65a5ff);
}

.good { color: #35d58b; }
.fair { color: #ffc857; }
.bad { color: #ff5c68; }

.verdict {
    font-size: 27px;
    font-weight: 800;
    margin-top: 20px;
}

.info-box {
    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.06);
    border-radius: 13px;
    padding: 16px;
    margin-bottom: 10px;
}

.info-title {
    font-weight: 700;
}

.info-text {
    color: #858f9e;
    font-size: 13px;
    margin-top: 4px;
}

.footer {
    text-align: center;
    color: #555f6e;
    font-size: 11px;
    line-height: 1.7;
    margin-top: 45px;
}

@media(max-width:700px) {
    .hero h1 {
        font-size: 43px;
    }

    .score {
        font-size: 50px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# BMW DATA
# =========================================================

TRIMS = {
    "2 Series": {
        "230i": 42000,
        "230i xDrive": 44200,
        "M240i": 53600,
        "M240i xDrive": 55600,
    },

    "3 Series": {
        "330i": 48000,
        "330i xDrive": 50000,
        "M340i": 62300,
        "M340i xDrive": 64300,
    },

    "4 Series": {
        "430i": 53300,
        "430i xDrive": 55300,
        "M440i": 67100,
        "M440i xDrive": 69100,
    },

    "5 Series": {
        "530i": 60500,
        "530i xDrive": 62800,
        "540i xDrive": 67700,
        "550e xDrive": 75500,
    },

    "7 Series": {
        "740i": 99800,
        "740i xDrive": 102800,
        "760i xDrive": 125000,
        "750e xDrive": 120000,
    },

    "X1": {
        "X1 xDrive28i": 43200,
        "X1 M35i": 52400,
    },

    "X2": {
        "X2 xDrive28i": 44700,
        "X2 M35i": 53900,
    },

    "X3": {
        "X3 30 xDrive": 51300,
        "X3 M50 xDrive": 66500,
    },

    "X5": {
        "X5 sDrive40i": 68300,
        "X5 xDrive40i": 72100,
        "X5 xDrive50e": 76000,
        "X5 M60i": 93600,
    },

    "X6": {
        "X6 xDrive40i": 77300,
        "X6 M60i": 98000,
    },

    "X7": {
        "X7 xDrive40i": 87500,
        "X7 M60i": 115000,
        "ALPINA XB7": 156000,
    },

    "M2": {
        "M2": 69500,
    },

    "M3": {
        "M3": 79300,
        "M3 Competition": 83500,
        "M3 Competition xDrive": 88600,
    },

    "M4": {
        "M4": 82200,
        "M4 Competition": 86600,
        "M4 Competition xDrive": 91700,
    },

    "M5": {
        "M5": 123300,
    }
}


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">
    <div class="logo">BMW</div>
    <h1>BMW <span class="blue">DealCheck</span></h1>
    <p>
        Analyze a BMW listing and see whether you're looking at
        a great deal, a fair price, or an overpriced car.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# VEHICLE
# =========================================================

st.markdown("""
<div class="card">
<div class="card-title">🚘 Vehicle Details</div>
<div class="card-sub">
Enter the information from the BMW listing.
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

    model = st.selectbox(
        "BMW model",
        list(TRIMS.keys())
    )

    trim = st.selectbox(
        "Trim",
        list(TRIMS[model].keys())
    )

    mileage = st.number_input(
        "Mileage",
        min_value=0,
        max_value=500000,
        value=40000,
        step=1000
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


# =========================================================
# OWNERS + OPTIONS
# =========================================================

st.markdown("""
<div class="card">
<div class="card-title">🔧 Vehicle History & Options</div>
<div class="card-sub">
These details can meaningfully affect what a used BMW is worth.
</div>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")

with c1:

    owners = st.selectbox(
        "Number of previous owners",
        ["1 owner", "2 owners", "3 owners", "4+ owners", "Unknown"]
    )

    seller = st.selectbox(
        "Seller type",
        ["Franchise BMW dealer", "Independent dealer", "Private seller"]
    )

with c2:

    options = st.multiselect(
        "Important options",
        [
            "M Sport Package",
            "Premium Package",
            "Executive Package",
            "Driving Assistance Package",
            "Harman Kardon Audio",
            "Merino Leather",
            "Panoramic Roof",
            "Adaptive M Suspension"
        ]
    )


# =========================================================
# ANALYSIS
# =========================================================

if st.button("Analyze My BMW  →", use_container_width=True):

    msrp = TRIMS[model][trim]

    # -----------------------------------------------------
    # AGE
    # -----------------------------------------------------

    age = max(0, 2026 - year)

    # Rough depreciation model.
    # This is intentionally an estimate until real listing
    # data is connected.
    depreciation = 0.84 ** age

    estimated = msrp * depreciation


    # -----------------------------------------------------
    # MILEAGE
    # -----------------------------------------------------

    expected_miles = max(5000, age * 12000)

    mileage_difference = mileage - expected_miles

    mileage_factor = 1.0 - (
        mileage_difference / 250000
    )

    mileage_factor = max(
        0.72,
        min(1.08, mileage_factor)
    )


    # -----------------------------------------------------
    # CONDITION
    # -----------------------------------------------------

    condition_factor = {
        "Poor": 0.82,
        "Fair": 0.92,
        "Good": 1.00,
        "Excellent": 1.07
    }[condition]


    # -----------------------------------------------------
    # ACCIDENTS
    # -----------------------------------------------------

    accident_factor = {
        "None reported": 1.00,
        "One or more reported": 0.87,
        "Unknown": 0.95
    }[accident]


    # -----------------------------------------------------
    # SERVICE
    # -----------------------------------------------------

    service_factor = {
        "Strong / documented": 1.04,
        "Some records": 1.00,
        "Unknown": 0.94
    }[service]


    # -----------------------------------------------------
    # OWNERS
    # -----------------------------------------------------

    owner_factor = {
        "1 owner": 1.02,
        "2 owners": 1.00,
        "3 owners": 0.98,
        "4+ owners": 0.94,
        "Unknown": 0.97
    }[owners]


    # -----------------------------------------------------
    # SELLER
    # -----------------------------------------------------

    seller_factor = {
        "Franchise BMW dealer": 1.04,
        "Independent dealer": 1.00,
        "Private seller": 0.96
    }[seller]


    # -----------------------------------------------------
    # OPTIONS
    # -----------------------------------------------------

    option_bonus = min(
        0.08,
        len(options) * 0.012
    )


    # -----------------------------------------------------
    # FINAL ESTIMATE
    # -----------------------------------------------------

    fair_value = (
        estimated
        * mileage_factor
        * condition_factor
        * accident_factor
        * service_factor
        * owner_factor
        * seller_factor
        * (1 + option_bonus)
    )

    low_value = fair_value * 0.93
    high_value = fair_value * 1.07


    # -----------------------------------------------------
    # DEAL SCORE
    # -----------------------------------------------------

    ratio = asking / fair_value

    score = round(
        100 - ((ratio - 0.80) * 200)
    )

    score = max(0, min(100, score))


    # -----------------------------------------------------
    # VERDICT
    # -----------------------------------------------------

    if ratio <= 0.90:

        verdict = "GREAT DEAL"
        verdict_class = "good"

    elif ratio <= 1.05:

        verdict = "FAIR DEAL"
        verdict_class = "fair"

    else:

        verdict = "OVERPRICED"
        verdict_class = "bad"


    difference = asking - fair_value


    # =====================================================
    # SUMMARY
    # =====================================================

    st.markdown("""
    <div class="card">
    <div class="card-title">📊 Analysis</div>
    <div class="card-sub">
    Here's what DealCheck estimates for this BMW.
    </div>
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)

    with a:
        st.metric(
            "Vehicle",
            f"{year} {trim}"
        )

    with b:
        st.metric(
            "Mileage",
            f"{mileage:,} mi"
        )

    with c:
        st.metric(
            "Asking Price",
            f"${asking:,.0f}"
        )


    # =====================================================
    # RESULT
    # =====================================================

    st.markdown(
        f"""
        <div class="result">

        <div class="label">
        Estimated Fair Value
        </div>

        <div class="price">
        ${low_value:,.0f} – ${high_value:,.0f}
        </div>

        <br>

        <div class="label">
        Deal Score
        </div>

        <div class="score">
        {score}/100
        </div>

        <div class="bar">
            <div class="fill" style="width:{score}%"></div>
        </div>

        <div class="verdict {verdict_class}">
        {verdict}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # PRICE EXPLANATION
    # =====================================================

    if difference > 0:

        st.warning(
            f"⚠️ You're approximately "
            f"**${difference:,.0f} above** the current DealCheck estimate."
        )

    else:

        st.success(
            f"💰 You're approximately "
            f"**${abs(difference):,.0f} below** the current DealCheck estimate."
        )


    # =====================================================
    # WHY?
    # =====================================================

    st.markdown("""
    <div class="card">
    <div class="card-title">🧠 Why DealCheck scored it this way</div>
    </div>
    """, unsafe_allow_html=True)

    explanations = []

    if mileage_factor >= 1:
        explanations.append(
            ("Mileage", "Mileage is at or below the estimated average.")
        )
    else:
        explanations.append(
            ("Mileage", "Mileage is above the estimated average.")
        )

    if condition == "Excellent":
        explanations.append(
            ("Condition", "Excellent condition adds value.")
        )
    elif condition == "Poor":
        explanations.append(
            ("Condition", "Poor condition significantly reduces estimated value.")
        )

    if accident == "One or more reported":
        explanations.append(
            ("History", "Reported accidents reduce the estimate.")
        )

    if service == "Strong / documented":
        explanations.append(
            ("Service", "Strong service documentation improves confidence.")
        )

    if len(options) >= 3:
        explanations.append(
            ("Options", "Multiple desirable options increase the estimate.")
        )

    for title, text in explanations:

        st.markdown(
            f"""
            <div class="info-box">
                <div class="info-title">{title}</div>
                <div class="info-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # BUYING CHECKLIST
    # =====================================================

    st.markdown("""
    <div class="card">
    <div class="card-title">🔍 Before You Buy</div>
    <div class="card-sub">
    A good price doesn't automatically mean it's a good BMW.
    </div>
    </div>
    """, unsafe_allow_html=True)

    checks = [
        (
            "Vehicle history",
            "Verify title, accidents, ownership and mileage."
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
            "Check remaining tire tread and brake condition."
        ),
        (
            "Options",
            "Confirm that the listed packages and features are actually installed."
        ),
        (
            "Test drive",
            "Listen for unusual noises and verify that all major systems work."
        )
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


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
BMW DealCheck is an independent educational tool and is not
affiliated with or endorsed by BMW AG.<br><br>
DealCheck estimates are not professional appraisals.
Actual vehicle values vary based on location, configuration,
condition, history, options and current market demand.
<br><br>
BMW DealCheck • V2
</div>
""", unsafe_allow_html=True)
