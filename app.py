import streamlit as st

st.set_page_config(page_title="BMW DealCheck", page_icon="🚗", layout="centered")

st.title("🚗 BMW DealCheck")
st.caption("A simple educational tool for estimating whether a BMW asking price looks reasonable.")

st.info("This MVP is an estimate, not an appraisal or a guarantee of a vehicle's value.")

col1, col2 = st.columns(2)
with col1:
    year = st.number_input("Model year", min_value=2000, max_value=2026, value=2022, step=1)
    mileage = st.number_input("Mileage", min_value=0, max_value=500000, value=40000, step=1000)
with col2:
    model = st.selectbox("BMW model", [
        "3 Series", "5 Series", "7 Series", "X3", "X5", "X7",
        "M2", "M3", "M4", "M5"
    ])
    asking = st.number_input("Asking price ($)", min_value=1000, max_value=1000000, value=50000, step=500)

condition = st.select_slider("Overall condition", options=["Poor", "Fair", "Good", "Excellent"], value="Good")
accident = st.selectbox("Known accident history", ["None reported", "One or more reported", "Unknown"])
service = st.selectbox("Service history", ["Strong / documented", "Some records", "Unknown"])

if st.button("Analyze Deal", type="primary", use_container_width=True):
    # Deliberately simple MVP heuristic. Replace with real market-data modeling later.
    base = {
        "3 Series": 32000, "5 Series": 43000, "7 Series": 58000,
        "X3": 38000, "X5": 50000, "X7": 65000,
        "M2": 50000, "M3": 62000, "M4": 65000, "M5": 78000
    }[model]

    age = max(0, 2026 - year)
    estimated = base * (0.87 ** age)

    mileage_factor = max(0.65, min(1.10, 1.05 - max(0, mileage - 12000) / 100000))
    condition_factor = {"Poor": .82, "Fair": .92, "Good": 1.0, "Excellent": 1.06}[condition]
    accident_factor = {"None reported": 1.0, "One or more reported": .88, "Unknown": .96}[accident]
    service_factor = {"Strong / documented": 1.03, "Some records": 1.0, "Unknown": .95}[service]

    fair_value = estimated * mileage_factor * condition_factor * accident_factor * service_factor
    ratio = asking / fair_value
    score = max(0, min(100, round(100 - (ratio - 0.85) * 180)))

    if ratio <= .92:
        label = "🟢 Looks like a good deal"
    elif ratio <= 1.05:
        label = "🟡 Looks roughly fair"
    else:
        label = "🔴 Looks expensive"

    st.divider()
    st.metric("Estimated fair-value range", f"${fair_value * .93:,.0f} – ${fair_value * 1.07:,.0f}")
    st.metric("Deal score", f"{score}/100")
    st.subheader(label)

    difference = asking - fair_value
    if difference >= 0:
        st.write(f"The asking price is approximately **${difference:,.0f} above** this MVP estimate.")
    else:
        st.write(f"The asking price is approximately **${abs(difference):,.0f} below** this MVP estimate.")

    st.write("### Things to verify before buying")
    st.write("- Vehicle history and title status")
    st.write("- Independent pre-purchase inspection")
    st.write("- Service records")
    st.write("- Tire and brake condition")
    st.write("- Exact options/packages and vehicle configuration")

st.divider()
st.caption("The model is intentionally a rough MVP. BMW's official site lists current models and MSRP, but used-car values require real market/listing data. BMW also notes MSRP does not necessarily represent a dealer's actual sale price.")
