import streamlit as st 
st.title("Multiplication using Streamlit")
 
# creates a horizontal line
st.write("---")

# input 1
num1 = st.number_input(label="Enter first number")
 
# input 2
num2 = st.number_input(label="Enter second number")

ans = 0
 
def calculate():
    ans = num1 * num2 
    st.success(f"Answer = {ans}")

if st.button("Calculate result"):
    calculate()

