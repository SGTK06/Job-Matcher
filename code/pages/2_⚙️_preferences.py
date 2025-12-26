import sys
import os
#to avoid streamlit import path errors => source:https://stackoverflow.com/questions/68033795/avoiding-sys-path-append-for-imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from src.user_input_validation import *
from src.user_data_manager import DataManager

# Set page configuration
st.set_page_config(
    page_title="Prferences Page",
    page_icon="⚙️",
    layout="centered"
)

# Title of the page
st.title("Set Up Your Preferences")

# Instructions
st.write("Please enter your skills and preferences in the form below:")

data_manager = DataManager()
# Preferences form
with st.form(key='preferences_form'):
    if data_manager.is_signed_in():
        user_pref = data_manager.get_preferences()
        skill_string = ", ".join(user_pref["user_skills"])

        try:
            min_salary = int(user_pref["min_salary"])
        except ValueError:
            min_salary = 0

        skills = st.text_input(
            "Enter a list of keywords that describe your skills",
            placeholder="skill-1, skill-2, skill-3, . . . . .",
            value=skill_string
        )
        minSalary = st.number_input(
            "Enter the minimum salary in k (1000)",
            step=100,
            min_value=0,
            value=min_salary
        )

    else:
        skills = st.text_input(
            "Enter a list of keywords that describe your skills",
            placeholder="skill-1, skill-2, skill-3, . . . . ."
        )
        minSalary = st.number_input(
            "Enter the minimum salary in k (1000)",
            step=100,
            min_value=0
        )

    # Save button
    save_button = st.form_submit_button(label="Save Preferences")

if save_button:
    if not validate_skills(skills):
        st.error("Increase your skillset, please add more of your skills!")

    else:
        username = data_manager.get_user_data()["user_name"]
        data_manager.register_preferences(skills, min_salary)
        saved = data_manager.save_preferences()
        if saved:
            st.success(f"Preferences saved successfully! You can start using the Job Matcher, {username}.")
        else:
            st.error("Failed to save preferences!")