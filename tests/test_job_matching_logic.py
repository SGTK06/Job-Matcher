"""
File for testing the job matcher logic
author: Sham Ganesh Thamarai Kannan
"""

import unittest
from unittest import mock
import pandas

from src.job_matching_logic import evaluate_job
from src.data_manager import DataManager
from src.config import USER_DATA, USER_PREFERENCES

def get_user_data(self):
    return {
        "user_name": "Ash Ketchum",
        "user_mail": "ashk@pokemon.com"
    }

def get_preferences(self):
    return {
        "user_skills": [
            "python",
            "numpy",
            "pandas",
            "testing",
            "data",
            "excel",
            "algorithms",
            "agile",
            "java",
            "math"],
        "min_salary": 1
        }

class TestJobMatching(unittest.TestCase):
    """
    Class to test the job matching logic of the system
    """
    def set_up_testing_env(self):
        data_manager = DataManager()
        #make deep copy to prevent mutation of user data during testing
        self.production_user_data = data_manager.user_data_frame.copy(deep=True)
        self.production_user_pref = data_manager.user_preferences.copy(deep=True)

        #keep headers only
        user_data_headers = pandas.read_csv(USER_DATA, nrows=0)
        user_pref_headers = pandas.read_csv(USER_PREFERENCES, nrows=0)
        user_data_headers.to_csv(USER_DATA, index=False)
        user_pref_headers.to_csv(USER_PREFERENCES, index=False)

    def restore_production_env(self):
        self.production_user_data.to_csv(USER_DATA, index=False)
        self.production_user_pref.to_csv(USER_PREFERENCES, index=False)


    def setUp(self):
        self.set_up_testing_env()

        self.user_skills ="python,numpy, pandas, testing, data, excel, algorithms, agile, java, math"

        self.pref_salary = "1" #  k (1000)

        self.suitable_tags = [
            "python",
            "numpy",
            "pandas",
            "testing",
            "data",
            "excel",
            "algorithms",
            "agile",
            "java",
            "math"
        ]

        self.unsuitable_tags = [
            "project management",
            "physics",
            "chemistry",
            "genetics",
            "biology",
            "mechanical",
            "robotics"
        ]

        self.suitable_salary = "2"
        self.unsuitable_salary = "0"

    def tearDown(self):
        self.restore_production_env()

    def test_different_skills_unsuitable_salary(self):
        data_manager = DataManager()
        data_manager.register_user("userX", "ux@mail.com")
        data_manager.register_preferences(
            self.user_skills,
            self.pref_salary
        )
        data_manager.save_preferences()

        job_details = {
            "salary": self.unsuitable_salary,
            "tags": self.unsuitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    def test_different_skills_suitable_salary(self):
        data_manager = DataManager()
        data_manager.register_user("userX", "ux@mail.com")
        data_manager.register_preferences(
            self.user_skills,
            self.pref_salary
        )
        data_manager.save_preferences()

        job_details = {
            "salary": self.suitable_salary,
            "tags": self.unsuitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    def test_matched_skills_unsuitable_salary(self):
        data_manager = DataManager()
        data_manager.register_user("userX", "ux@mail.com")
        data_manager.register_preferences(
            self.user_skills,
            self.pref_salary
        )
        data_manager.save_preferences()

        job_details = {
            "salary": self.unsuitable_salary,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    def test_matched_skills_suitable_salary(self):
        data_manager = DataManager()
        data_manager.register_user("userX", "ux@mail.com")
        data_manager.register_preferences(
            self.user_skills,
            self.pref_salary
        )
        data_manager.save_preferences()

        job_details = {
            "salary": self.suitable_salary,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertTrue(suitability)

    def test_matched_skills_exact_salary(self):
        data_manager = DataManager()
        data_manager.register_user("userX", "ux@mail.com")
        data_manager.register_preferences(
            self.user_skills,
            self.pref_salary
        )
        data_manager.save_preferences()

        job_details = {
            "salary": self.pref_salary,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertTrue(suitability)

    def test_case_when_detail_not_job(self):
        data_manager = DataManager()
        data_manager.register_user("userX", "ux@mail.com")
        data_manager.register_preferences(
            self.user_skills,
            self.pref_salary
        )
        data_manager.save_preferences()

        job_details = {}

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    """
    @mock.patch("src.data_manager.DataManager.get_user_data", side_effect = get_user_data)
    @mock.patch("src.data_manager.DataManager.get_preferences", side_effect = get_preferences)
    """