import streamlit as st

# Define function to get dosage and warnings based on weight
def get_dosage_by_weight(weight, formulation):
    # Initialize warning message
    warning = ""

    # Diphenhydramine formulations and dosages by weight
    if formulation == "Children's Diphenhydramine Liquid (12.5 mg / 5 mL)":
        if weight < 11.00 or weight > 43.99:
            warning = "Warning: Children's Diphenhydramine liquid is not typically used for this weight. Please verify your selection."
        if 11.00 <= weight <= 15.99:
            return "5 mL", "12.5 mg", warning
        elif 16.00 <= weight <= 21.99:
            return "7.5 mL", "18.75 mg", warning
        elif 22.00 <= weight <= 26.99:
            return "10 mL", "25 mg", warning
        elif 27.00 <= weight <= 32.99:
            return "12.5 mL", "31.25 mg", warning
        elif 33.00 <= weight <= 43.99:
            return "15 mL", "37.5 mg", warning
        elif weight >= 44.00:
            return "20 mL", "50 mg", warning

    elif formulation == "Children's Diphenhydramine Chewables (12.5 mg)":
        if weight < 11.00 or weight > 43.99:
            warning = "Warning: Children's Diphenhydramine chewables are not typically used for this weight. Please verify your selection."
        if 11.00 <= weight <= 15.99:
            return "1 tablet", "12.5 mg", warning
        elif 16.00 <= weight <= 21.99:
            return "1.5 tablets", "18.75 mg", warning
        elif 22.00 <= weight <= 26.99:
            return "2 tablets", "25 mg", warning
        elif 27.00 <= weight <= 32.99:
            return "2.5 tablets", "31.25 mg", warning
        elif 33.00 <= weight <= 43.99:
            return "3 tablets", "37.5 mg", warning
        elif weight >= 44.00:
            return "4 tablets", "50 mg", warning

    elif formulation == "Adult Diphenhydramine Tablets (25 mg)":
        if weight < 22.00:
            warning = "Warning: Adult Diphenhydramine tablets are not typically used for this weight. Please verify your selection."
        if 22.00 <= weight <= 26.99:
            return "1 tablet", "25 mg", warning
        elif 27.00 <= weight <= 32.99:
            return "1 tablet", "25 mg", warning
        elif 33.00 <= weight <= 43.99:
            return "1.5 tablets", "37.5 mg", warning
        elif weight >= 44.00:
            return "2 tablets", "50 mg", warning

    return "Dose not available", "Please consult a healthcare provider.", warning

# Streamlit app layout
st.title("Pediatric Diphenhydramine Dosing Calculator")

# Select weight unit and input
unit = st.selectbox("Select weight unit", ["kg", "lbs"])

# Input weight, allowing decimal entry
weight = st.number_input(f"Enter the patient's weight in {unit}:", min_value=0, step=1)

# Convert weight to kg if entered in lbs
if unit == "lbs":
    weight = weight * 0.453592  # Convert pounds to kilograms

# Select the formulation
formulation = st.selectbox("Select the formulation", [
    "Children's Diphenhydramine Liquid (12.5 mg / 5 mL)",
    "Children's Diphenhydramine Chewables (12.5 mg)",
    "Adult Diphenhydramine Tablets (25 mg)"
])

# Calculate dosage and display warnings if needed
if st.button("Calculate Dosage"):
    dosage, dose, warning = get_dosage_by_weight(weight, formulation)
    if warning:
        st.warning(warning)
    st.write(f"Dosage: {dosage} ({dose})")
    st.write("Give every 4 to 6 hours as needed for allergy symptoms. Do not exceed 6 doses in 24 hours.")
    st.write("Do not use with any other diphenhydramine-containing products unless directed by a healthcare provider.")

st.write("Note: Dosing information is sourced from [HealthyChildren.org](https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Diphenhydramine.aspx).")
