# Import the streamlit library for the web interface
import streamlit as st

# A function to perform the temperature conversions
def convert_temp(value, input_unit, output_unit):
    # Convert input value to a common base (Kelvin)
    if input_unit == "Celsius":
        kelvin_value = value + 273.15
    elif input_unit == "Fahrenheit":
        kelvin_value = (value - 32) * 5/9 + 273.15
    else:  # Assumes input_unit is "Kelvin"
        kelvin_value = value

    # Convert from the common base (Kelvin) to the desired output unit
    if output_unit == "Celsius":
        return kelvin_value - 273.15
    elif output_unit == "Fahrenheit":
        return (kelvin_value - 273.15) * 9/5 + 32
    else:  # Assumes output_unit is "Kelvin"
        return kelvin_value

# Set the title of the app
st.title("Universal Temperature Converter")

# A simple explanation for the user
st.write("Select your input and output temperature scales to perform a conversion.")

# Create a number input widget for the temperature value
temp_value = st.number_input(label="Enter Temperature", value=0.0, key="temp_input")

# Create two selectbox widgets for selecting the units
input_scale = st.selectbox(
    label="Input Scale",
    options=["Kelvin", "Celsius", "Fahrenheit"],
    key="input_scale"
)

output_scale = st.selectbox(
    label="Output Scale",
    options=["Kelvin", "Celsius", "Fahrenheit"],
    index=1, # Sets Celsius as the default output
    key="output_scale"
)

# Perform the conversion when the user interacts with the widgets
converted_value = convert_temp(temp_value, input_scale, output_scale)

# Display the result to the user, formatted to two decimal places
st.write(f"The converted temperature is: {converted_value:.2f} {output_scale}")
