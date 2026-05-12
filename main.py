import streamlit as st

st.title("Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")
c = st.selectbox("Pick operation", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if c == "+":
        d = a + b
    elif c == "-":
        d = a - b
    elif c == "*":
        d = a * b
    elif c == "/":
        d = a / b
    
    st.write(f"Result: {d}")