"""
File for testing the job matcher logic
author: Sham Ganesh Thamarai Kannan
"""

import unittest
from unittest import mock
import pandas

from src.job_matching_logic import evaluate_job
from src.user_data_manager import DataManager
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
    @classmethod
    def setUpClass(cls):
        data_manager = DataManager()
        #make deep copy to prevent mutation of user data during testing
        cls.production_user_data = data_manager.user_data_frame.copy(deep=True)
        cls.production_user_pref = data_manager.user_preferences.copy(deep=True)

        #keep headers only
        user_data_headers = pandas.read_csv(USER_DATA, nrows=0)
        user_pref_headers = pandas.read_csv(USER_PREFERENCES, nrows=0)
        user_data_headers.to_csv(USER_DATA, index=False)
        user_pref_headers.to_csv(USER_PREFERENCES, index=False)

        cls.data_manager = DataManager()
        cls.data_manager.register_user("userX", "ux@mail.com")
        cls.data_manager.register_preferences(
            "python,numpy, pandas, testing, data, excel, algorithms, agile, java, math",
            1
        )
        cls.data_manager.save_preferences()

    @classmethod
    def tearDownClass(cls):
        cls.production_user_data.to_csv(USER_DATA, index=False)
        cls.production_user_pref.to_csv(USER_PREFERENCES, index=False)


    def setUp(self):

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

    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_different_skills_unsuitable_salary(self, comparison_score):
        comparison_score.return_value = 30

        job_details = {
            "salary": self.unsuitable_salary,
            "tags": self.unsuitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_different_skills_suitable_salary(self, comparison_score):
        comparison_score.return_value = 40

        job_details = {
            "salary": self.suitable_salary,
            "tags": self.unsuitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_matched_skills_unsuitable_salary(self, comparison_score):
        comparison_score.return_value = 85

        job_details = {
            "salary": self.unsuitable_salary,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_matched_skills_suitable_salary(self, comparison_score):
        comparison_score.return_value = 85

        job_details = {
            "salary": self.suitable_salary,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertTrue(suitability)

    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_matched_skills_exact_salary(self, comparison_score):
        comparison_score.return_value = 85

        job_details = {
            "salary": 1,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertTrue(suitability)

    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_matched_skills_exact_skills(self, comparison_score):
        comparison_score.return_value = 65

        job_details = {
            "salary": 1,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertTrue(suitability)

    def test_case_when_detail_not_job(self):
        data_manager = DataManager()

        job_details = {}

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    """
    @mock.patch("src.data_manager.DataManager.get_user_data", side_effect = get_user_data)
    @mock.patch("src.data_manager.DataManager.get_preferences", side_effect = get_preferences)
    """