import sys
import os
#to avoid streamlit import path errors => source:https://stackoverflow.com/questions/68033795/avoiding-sys-path-append-for-imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from src.user_input_validation import *
from src.data_manager import DataManager

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

data_manager = DataManager()
# Signup form
with st.form(key='profile_form'):

    if data_manager.is_signed_in():
        user_data = data_manager.get_user_data()
        username = st.text_input(
            "Username",
            key='profile_username',
            placeholder="5+ chars",
            value=user_data["user_name"]
        )
        email = st.text_input(
            "Email",
            key='profile_email',
            placeholder="mail@domain.extension",
            value=user_data["user_mail"]
        )

    else:
        username = st.text_input(
            "Username",
            key='profile_username',
            placeholder="5+ chars"
        )
        email = st.text_input(
            "Email",
            key='profile_email',
            placeholder="mail@domain.extension"
        )

    # Save button
    save_button = st.form_submit_button(
        label="Save Profile"
    )

if save_button:
    if not validate_user_name(username):
        st.error("Invalid user name, please check your user name!")

    elif not validate_email(email):
        st.error("Invalid mail address, please check your mail id!")

    else:
        data_manager.register_user(username, email)
        saved = data_manager.save_user()
        if saved:
            st.success(f"Profile saved successfully! Welcome, {username}.")
        else:
            st.error("Failed to save profile!")