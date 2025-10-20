import streamlit as st

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

with st.form(key='preferences_form'):

    skills = st.text_input(
        "Enter a list of keywords that describe your skills",
        placeholder="skill-1, skill-2, skill-3, . . . . ."
    )
    minSalary = st.number_input(
        "Enter the minimum salary",
        step=100,
        min_value=0
    )

    # Save button
    save_button = st.form_submit_button(label="Save Preferences")
