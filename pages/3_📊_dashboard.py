import sys
import os
import warnings
from pathlib import Path

os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

# Suppress ALL warnings immediately
warnings.filterwarnings("ignore")

#to avoid streamlit import path errors => source:https://stackoverflow.com/questions/68033795/avoiding-sys-path-append-for-imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from datetime import datetime

try:
    from src.dashboard_data_feed import DashboardDataFeed
except ImportError as e:
    st.error(f"Import error: {e}")
    st.stop()

# Title of the page
st.title("📊 Job Matcher Dashboard")
st.write("Find and manage your matched job opportunities")

data_feed = DashboardDataFeed()

user_status = data_feed.get_user_status()
if not user_status["is_signed_in"]:
    st.warning("Please complete your profile first!!!")
    st.stop()

if not user_status["has_preferences"]:
    st.warning("Please set up your preferences first!!!")
    st.stop()

user_pref = data_feed.get_user_preferences()
st.sidebar.write(f"**Your Skills:** {', '.join(user_pref['user_skills'])}")
st.sidebar.write(f"**Minimum Salary:** ${user_pref['min_salary']}k")

st.subheader("💼 Your Job Listings")

display_jobs = data_feed.get_data_feed()

if not display_jobs:
    st.info("No jobs found. Try searching for new jobs or adjusting your filters.")
else:
    st.write(f"Showing {len(display_jobs)} job(s)")

    for i, job in enumerate(display_jobs):
        with st.expander(f"💼 {job["title"]} at {job["company_name"]}", expanded=False):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.write(f"**Company:** {job["company_name"]}")
                st.write(f"**Category:** {job["category"]}")
                st.write(f"**Job Type:** {job["job_type"]}")
                st.write(f"**Location:** {job["candidate_required_location"]}")
                st.write(f"**Salary:** {job["salary"]}")
                st.write(f"**Published:** {job["publication_date"]}")

                if job["tags"]:
                    st.write("**Required Skills:**")
                    tags_display = job["tags"]
                    st.write(tags_display)

                if job["description"]:
                    st.write("**Description:**")
                    desc = job["description"][:500] + "..."
                    st.write(desc)

            with col2:
                st.write(f"**Status:** {job["application_status"]}")

                # View original job posting
                if job["url"]:
                    st.link_button("View Original Posting", job["url"])