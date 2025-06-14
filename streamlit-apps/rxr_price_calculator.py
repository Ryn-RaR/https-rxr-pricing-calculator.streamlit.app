import streamlit as st

st.set_page_config(page_title="RxR Service Estimator")
st.title("🧼 RxR Interactive Pricing Calculator")

st.markdown("---")

# Vehicle type selection
vehicle_type = st.selectbox("Select your vehicle type:", [
    "Motorcycle", "2-door Car", "4-door Car", "Mid-size SUV", "SUV & Truck"
])

# Condensed service pricing structure
service_matrix = {
    "Bright & Bold Interior OR Exterior": {"Motorcycle": 200, "2-door Car": 215, "4-door Car": 220, "Mid-size SUV": 225, "SUV & Truck": 230},
    "Full Interior + Exterior": {
        "Motorcycle": 350, "2-door Car": 370, "4-door Car": 380, "Mid-size SUV": 390, "SUV & Truck": 400
    },
    "Marbled Clay Buff/Polish/Sealed": {
        "Motorcycle": 555, "2-door Car": 777, "4-door Car": 777, "Mid-size SUV": 888, "SUV & Truck": 999
    },
    "Golden-Ink Signature": {
        "Motorcycle": 450, "2-door Car": 500, "4-door Car": 500, "Mid-size SUV": 550, "SUV & Truck": 575
    }
}

# Tier groupings for subscriptions
subscription_tiers = ["Marbled Clay Buff/Polish/Sealed", "Golden-Ink Signature"]

st.subheader("Select Services")
filtered_services = [service for service in service_matrix.keys() if service not in ["Clay Bar & Iron Decon"]]
selected_services = st.multiselect("Choose services to include in your estimate:", filtered_services, default=[], key="service_selector")

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
selected_addons = st.multiselect("Add optional extras:", list(add_ons.keys()), default=[], key="addon_selector")

# Maintenance detail info
st.markdown("---")
st.subheader("🛠️ Maintenance Detail")
st.markdown("""
Before we can offer a subscription or advanced polishing estimate, your vehicle must receive a maintenance detail.

**Maintenance Includes:**
- 2-Bucket Wash
- Buff/Polish
- Tire & Trim Dressing
- Carpet & Leather Extraction
- Dashboard Cleaning

**Prices (Starting at):**
- Car: ~$300
- Mid-size SUV: ~$350
- Truck/SUV: ~$400

After this service, custom packages and subscriptions may be unlocked.
""")

# Estimate Calculation
subtotal = 0
for service in selected_services:
    subtotal += service_matrix[service][vehicle_type]

for addon in selected_addons:
    subtotal += add_ons[addon]

st.markdown("---")
st.subheader("Estimated Total:")
st.markdown(f"### ~ ${subtotal:.2f}")

st.caption("*All prices are approximate and vary by soot level, surface condition, and time investment.*")

if "Bright & Bold Interior OR Exterior" in selected_services:
    st.markdown("---")
    st.subheader("What's Included in Bright & Bold Interior OR Exterior:")
    st.markdown("""
    - Choose either Interior OR Exterior Focus
    - Interior: dashboard, console, door panels deep-cleaned with microfiber and detailing brushes (Steamo-Vac: for deeper cleaning ~$15)+(Extracto-Vac: for best ~$30)
    - Exterior: receives a powerwash multi-coat soak, foam drench soap, tires shined with wells cleaned, completed with a glossy wax wipedown

    **Total Starting Price:**
    - Motorcycle: ~$200
    - 2-door Car: ~$215
    - 4-door Car: ~$220
    - Mid-size SUV: ~$225
    - SUV & Truck: ~$230
    """)

if "Full Interior + Exterior" in selected_services:
    st.markdown("---")
    st.subheader("What's Included in Full Interior + Exterior Detail:")
    st.markdown("""
    - Interior Wipe Down & Vacuum
    - Steam Cleaning
    - Exterior Foam Bath
    - Towel Dry + Wheel & Rim Detail

    **Total Starting Price:**
    - Motorcycle: ~$350
    - 2-door Car: ~$370
    - 4-door Car: ~$380
    - Mid-size SUV: ~$390
    - SUV & Truck: ~$400
    """)

if "Golden-Ink Signature" in selected_services:
    st.markdown("---")
    st.subheader("What's Included in the Golden-Ink Signature:")
    st.markdown("""
    - Full Interior Shampoo + Extraction
    - Leather & Plastic Conditioning
    - Exterior Wash + Light Polish
    - Glass & Mirror Detailing
    
    **Total Starting Price:**
    - Motorcycle: ~$450
    - 2-door & 4-door Cars: ~$500
    - Mid-size SUV: ~$550
    - SUV & Truck: ~$575
    """)

if "Marbled Clay Buff/Polish/Sealed" in selected_services:
    st.markdown("---")
    st.subheader("What's Included in Marbled Clay Buff/Polish/Sealed:")
    st.markdown("""
    - Hand Wash
    - Iron Decontamination
    - Clay Bar Treatment
    - Buff & Polish
    - Paint Sealant
    - Tire & Trim Dressing
    - Glass Finish

    **Total Starting Price:**
    - Motorcycle: ~$555
    - 2-door & 4-door Cars: ~$777
    - Mid-size SUV: ~$888
    - SUV & Truck: ~$999
    """)

if "Golden-Ink Signature" in selected_services:
    st.markdown("---")
    st.subheader("What's Included in the Golden-Ink Signature:")
    st.markdown("""
    - Full Interior Shampoo + Extraction
    - Leather & Plastic Conditioning
    - Exterior Wash + Light Polish
    - Glass & Mirror Detailing
    
    **Total Starting Price:**
    - Motorcycle: ~$450
    - 2-door & 4-door Cars: ~$500
    - Mid-size SUV: ~$550
    - SUV & Truck: ~$575
    """)
