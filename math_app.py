import streamlit as st
import math_module
from math_module import square_root

st.title("🧮 Math Wizard")
st.write("Welcome! Choose an operation and enter your numbers.")

operation = st.selectbox("Choose a mathematical operation:",
                         ("Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Modulus",)
                         )

operation_functions = {
    "Add": math_module.add_numbers,
    "Subtract": math_module.subtract_numbers,
    "Multiply": math_module.multiply_numbers,
    "Divide": math_module.divide_numbers,
    "Power": math_module.power_numbers,
    "Square Root": math_module.square_root,
    "Modulus": math_module.modulus
}

result = None


if operation in ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulus"]:
    num1 = st.number_input("Please enter your first number:", step=1.0, format="%.2f")
    num2 = st.number_input("Please enter your second number:", step=1.0, format="%.2f")

else:
    num1 = st.number_input("Enter the first number:", step=1.0, format="%.2f")
    num = None

if st.button("Calculate"):
    if operation in operation_functions:
        if operation == "Square Root":
            result = operation_functions["Square Root"](num1)
        else:
            result = operation_functions[operation](num1, num2)

        st.success(f"The result is {result}")
    else:
        st.error("Invalid operation selected")


