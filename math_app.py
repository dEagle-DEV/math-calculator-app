import streamlit as st
import math_module
from openai import OpenAI

# Setup OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def show_calculator_ui():
    st.title("🧮 Math Wizard")
    st.write("Welcome! Choose an operation and enter your numbers.")
    operation = st.selectbox(
        "Choose a mathematical operation:",
        ("Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Modulus"),
    )

    operation_functions = {
        "Add": math_module.add_numbers,
        "Subtract": math_module.subtract_numbers,
        "Multiply": math_module.multiply_numbers,
        "Divide": math_module.divide_numbers,
        "Power": math_module.power_numbers,
        "Square Root": math_module.square_root,
        "Modulus": math_module.modulus,
    }

    result = None

    if operation in ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulus"]:
        num1 = st.number_input("Please enter your first number:", step=1.0, format="%.2f")
        num2 = st.number_input("Please enter your second number:", step=1.0, format="%.2f")
    else:
        num1 = st.number_input("Enter the first number:", step=1.0, format="%.2f")

    if st.button("Calculate"):
        if operation in operation_functions:
            if operation == "Square Root":
                result = operation_functions["Square Root"](num1)
            else:
                result = operation_functions[operation](num1, num2)

            st.success(f"The result is {result}")
        else:
            st.error("Invalid operation selected")


# -------------------- MathGPT --------------------
def show_mathgpt_ui():
    st.title("💬 MathGPT")
    st.write("Welcome! What Math can I help you today?")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display previous messages
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if user_input := st.chat_input("Your Message"):
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["messages"]
        )

        assistant_reply = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})

        # Display assistant response immediately
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)


# -------------------- Tabs --------------------
tab1, tab2 = st.tabs(["🧮 Calculator", "💬 Chatbot"])

with tab1:
    show_calculator_ui()

with tab2:
    show_mathgpt_ui()
