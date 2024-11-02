import streamlit as st

# Define function to get dosage and warnings based on weight
def get_dosage_by_weight(weight, formulation):
    # Define weight ranges and dosages for each formulation
    warning = ""  # Initialize warning message

    if formulation == "Infant Diphenhydramine Liquid (12.5 mg / 5 mL)":
        if weight > 10.99:
            warning = "Warning: Infant Diphenhydramine is not typically used for this weight. Please verify your selection."
        if 3.00 <= weight <= 5.00:
            return "1.25 mL", "2.5 mg", warning
        elif 5.01 <= weight <= 7.99:
            return "2.5 mL", "5 mg", warning
        elif 8.00 <= weight <= 10.99:
            return "3.75 mL", "7.5 mg", warning

    elif formulation == "Children's Diphenhydramine Liquid (12.5 mg / 5 mL)":
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

# Define function to get dosage by age
def get_dosage_by_age(age, formulation):
    # Define age ranges and dosages for each formulation
    warning = ""  # Initialize warning message

    if formulation == "Infant Diphenhydramine Liquid (12.5 mg / 5 mL)":
        if age > 23:
            warning = "Warning: Infant Diphenhydramine is not typically used for this age. Please verify your selection."
        if 0 <= age <= 3:
            return "1.25 mL", "2.5 mg", warning
        elif 4 <= age <= 11:
            return "2.5 mL", "5 mg", warning
        elif 12 <= age <= 23:
            return "3.75 mL", "7.5 mg", warning

    elif formulation == "Children's Diphenhydramine Liquid (12.5 mg / 5 mL)":
        if age < 24 or age > 143:
            warning = "Warning: Children's Diphenhydramine liquid is not typically used for this age. Please verify your selection."
        if 24 <= age <= 35:
            return "5 mL", "12.5 mg", warning
        elif 36 <= age <= 47:
            return "7.5 mL", "18.75 mg", warning
        elif 48 <= age <= 71:
            return "10 mL", "25 mg", warning
        elif 72 <= age <= 95:
            return "12.5 mL", "31.25 mg", warning
        elif 96 <= age <= 143:
            return "15 mL", "37.5 mg", warning
        elif age >= 144:
            return "20 mL", "50 mg", warning

    elif formulation == "Children's Diphenhydramine Chewables (12.5 mg)":
        if age < 24 or age > 143:
            warning = "Warning: Children's Diphenhydramine chewables are not typically used for this age. Please verify your selection."
        if 24 <= age <= 35:
            return "1 tablet", "12.5 mg", warning
        elif 36 <= age <= 47:
            return "1.5 tablets", "18.75 mg", warning
        elif 48 <= age <= 71:
            return "2 tablets", "25 mg", warning
        elif 72 <= age <= 95:
            return "2.5 tablets", "31.25 mg", warning
        elif 96 <= age <= 143:
            return "3 tablets", "37.5 mg", warning
        elif age >= 144:
            return "4 tablets", "50 mg", warning

    elif formulation == "Adult Diphenhydramine Tablets (25 mg)":
        if age < 72:
            warning = "Warning: Adult Diphenhydramine tablets are not typically used for this age. Please verify your selection."
        if 72 <= age <= 95:
            return "1.5 tablets", "37.5 mg", warning
        elif age >= 96:
            return "2 tablets", "50 mg", warning

    return "Dose not available", "Please consult a healthcare provider.", warning

# Streamlit app layout
st.title("Pediatric Diphenhydramine Dosing Calculator")

# Select dosing type
choice = st.selectbox("Select Dosing by Weight or Age", ["Weight", "Age"])

# Main input for dosing by weight
if choice == "Weight":
    # Select unit for weight entry
    unit = st.selectbox("Select weight unit", ["kg", "lbs"])

    # Input weight with integer display but allowing for decimal entry
    weight = st.number_input(f"Enter the patient's weight in {unit}:", min_value=0, step=1)

    # Convert weight to kg if entered in lbs
    if unit == "lbs":
        weight = weight * 0.453592  # Convert pounds to kilograms

    formulation = st.selectbox("Select the formulation", [
        "Infant Diphenhydramine Liquid (12.5 mg / 5 mL)",
        "Children's Diphenhydramine Liquid (12.5 mg / 5 mL)",
        "Children's Diphenhydramine Chewables (12.5 mg)",
        "Adult Diphenhydramine Tablets (25 mg)"
    ])

    if st.button("Calculate Dosage"):
        dosage, dose, warning = get_dosage_by_weight(weight, formulation)
        if warning:
            st.warning(warning)
        st.write(f"Dosage: {dosage} ({dose})")
        st.write("Give every 4 to 6 hours as needed for allergy symptoms. Do not exceed 6 doses in 24 hours.")
        st.write("Do not use with other diphenhydramine-containing products unless directed by a healthcare provider.")

# Main input for dosing by age
elif choice == "Age":
    # Select unit for age entry
    age_unit = st.selectbox("Select age unit", ["Months", "Years"])

    # Enter age
    if age_unit == "Years":
        age = st.number_input("Enter the patient's age in years:", min_value=0, step=1)
        age = age * 12  # Convert years to months
    else:
        age = st.number_input("Enter the patient's age in months:", min_value=0, step=1)

    formulation = st.selectbox("Select the formulation", [
        "Infant Diphenhydramine Liquid (12.5 mg / 5 mL)",
        "Children's Diphenhydramine Liquid (12.5 mg / 5 mL)",
        "Children's Diphenhydramine Chewables (12.5 mg)",
        "Adult Diphenhydramine Tablets (25 mg)"
    ])

    if st.button("Calculate Dosage"):
        dosage, dose, warning = get_dosage_by_age(age, formulation)
        if warning:
            st.warning(warning)
        st.write(f"Dosage: {dosage} ({dose})")
        st.write("Give every 4 to 6 hours as needed for allergy symptoms. Do not exceed 6 doses in 24 hours.")
        st.write("Do not use with other diphenhydramine-containing products unless directed by a healthcare provider.")

st.write("Note: Dosing information is sourced from [HealthyChildren.org](https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Diphenhydramine.aspx).")
