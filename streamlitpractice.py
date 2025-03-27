import streamlit as st
st.title("My first webapp")

criteria_annaul_salary = 50000
criteria_year_of_work = 5

annual_salary = st.number_input("Enter your annual salary: ")
year_of_work = st.number_input("Enter your year of work: ")

if st.button("Submit"):
    if annual_salary >= criteria_annaul_salary and year_of_work >= criteria_year_of_work:
        st.write("Congratulation, your application has been accepted.")
    else:
        st.write("Sorry, your application has been rejected.")

# In TERMINAL type: streamlit run streamlitpractice.py