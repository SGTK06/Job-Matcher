import os
import streamlit as st

# Disable Streamlit file watcher errors on torch
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"

from src.job_matching_logic import search_and_match_jobs

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Job Matcher", page_icon="💼", layout="centered")

st.title("💼 Job Matcher")
st.write("Welcome! This app helps you find jobs that match your profile and preferences.")
st.divider()

# --- Job Search Control ---
st.subheader("🔍 Run Job Matching")

st.write(
    "Click the button below to fetch job listings from the Remotive API, "
    "match them against your profile, and save suitable ones automatically."
)

num_jobs = st.number_input(
    "Number of jobs to fetch:",
    min_value=10,
    max_value=200,
    step=10,
    value=50,
)

if st.button("Start Job Matching"):
    with st.spinner("Fetching and matching jobs..."):
        try:
            search_and_match_jobs(num_jobs)
            st.success(f"✅ Job search complete! Saved {num_jobs} listings (if matched).")
        except Exception as e:
            st.error(f"❌ An error occurred while matching jobs:\n\n{e}")

st.info("You can view saved job listings and your profile using the sidebar navigation.")