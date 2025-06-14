import streamlit as st

st.set_page_config(page_title="RxR Service Estimator")
st.title("🧼 RxR Interactive Pricing Calculator")

st.markdown("---")

# Vehicle type selection
vehicle_type = st.selectbox("Select your vehicle type:", [
    "Motorcycle", "2-door Car", "4-door Car", "Mid-size SUV", "SUV & Truck"
])

# Core Services Pricing
core_prices = {
    "Basic Detail": {
        "Motorcycle": 200, "2-door Car": 215, "4-door Car": 220, "Mid-size SUV": 225, "SUV & Truck": 230
    },
    "Full Detail": {
        "Motorcycle": 350, "2-door Car": 370, "4-door Car": 380, "Mid-size SUV": 390, "SUV & Truck": 400
    },
    "Clay & Iron Decon": {
        "Motorcycle": 130, "2-door Car": 135, "4-door Car": 140, "Mid-size SUV": 145, "SUV & Truck": 150
    },
    "Marble-Miracle": {
        "Motorcycle": 555, "2-door Car": 777, "4-door Car": 777, "Mid-size SUV": 888, "SUV & Truck": 999
    },
    "Golden-Ink Signature": {
        "Motorcycle": 450, "2-door Car": 500, "4-door Car": 500, "Mid-size SUV": 550, "SUV & Truck": 575
    }
}

st.subheader("Select Services")
selected_services = st.multiselect("Choose services to include in your estimate:", list(core_prices.keys()))

# Add-on pricing estimates
add_ons = {
    "Headlight Restoration": 60,
    "Engine Bay Cleaning": 75,
    "Leather Conditioning": 60,
    "Stain & Fabric Protection": 75,
    "Odor/Ozone Treatment": 100,
    "Trim & Tire Dressing": 50,
    "Pet Hair/Biohazard": 150
}

st.subheader("Optional Add-ons")
selected_addons = st.multiselect("Add optional extras:", list(add_ons.keys()))

# Estimate Calculation
subtotal = 0
for service in selected_services:
    subtotal += core_prices[service][vehicle_type]

for addon in selected_addons:
    subtotal += add_ons[addon]

st.markdown("---")
st.subheader("Estimated Total:")
st.markdown(f"### ~ ${subtotal:.2f}")

st.caption("*All prices are approximate and vary by soot level, surface condition, and time investment.*")
