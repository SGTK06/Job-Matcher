import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Profile Page",
    page_icon="👤",
    layout="centered"
)

# Title of the page
st.title("Set Up Your Profile")

# Instructions
st.write("Please fill up the details below to set up your profile start using the Job Matcher:")

# Signup form
with st.form(key='profile_form'):

    username = st.text_input("Username", key='profile_username')
    email = st.text_input("Email", key='profile_email')

    # Submit button
    save_button = st.form_submit_button(
        label="Save Profile"
    )