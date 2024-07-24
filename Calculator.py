import streamlit as st
st.title(":red-background[SIMPLE STREAMLIT CALCULATOR]:abacus:")
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division

st.write("Select an operation to perform:")
st.write("1 Add")
st.write("2 Subtract")
st.write("3 Multiplication")
st.write("4 Division")

option = st.selectbox(
    "Select an operation to perform",
    ("Add", "Subtract", "Multiplication", "Division"))

st.write("You selected:", option)

if option == "Add":
    num1 = st.number_input("Enter the first number:",step=1)
    num2 = st.number_input("Enter the second number:",step=1)
    sum = int(num1) + int(num2)
    st.write("The sum of two numbers is:" + str(sum))
elif option == "Subtract":
    num1 = st.number_input("Enter the first number:",step=1)
    num2 = st.number_input("Enter the second number:",step=1)
    sub = int(num1) - int(num2)
    st.write("The subtraction of two numbers is:" + str(sub))
elif option == "Multiplication":
    num1 = st.number_input("Enter the first number:",step=1)
    num2 = st.number_input("Enter the second number:",step=1)
    mul = int(num1) * int(num2)
    st.write("The multiplication of two numbers is:" + str(mul))
elif option == "Division":
    num1 = st.number_input("Enter the first number:",step=1)
    num2 = st.number_input("Enter the second number:",step=1)
    div = int(num1) / int(num2)
    st.write("The division of two numbers is:" + str(div))



