import streamlit as st
import pandas as pd

def main():
    st.title("Streamlit Forms & Salary Calculator")
    menu = ["Home" , "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")

        with st.form(key='salaryform'):
            col1, col2, col3 = st.beta_columns([3, 2, 1])
            with col1:
                amount = st.number_input("Hourly Rate in $")
            with col2:
                hour_per_week = st.number_input("Hours Per Week", 1, 120)
                submit_button = st.form_submit_button(label='SignUp')

        # method1
        with st.form(key='form1'):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("Lastname")
            dob = st.date_input("Date of Birth")

            submit_button = st.form_submit_button(label='SignUp')

        if submit_button:
            st.success("Hello {} you've created an account". format(firstname))

        # method2
        form2 = st.form(key='form2')
        username = form2.text_input("Username")
        jobtype = form2.selectbox("Job", ["Dev", "Data Scientist", "Data Analyst"])
        submit_button2 = form2.form_submit_button("Login")

    else:
        st.subheader("About")


if __name__ == '__main__':
     main()

