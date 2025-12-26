"""
File for testing the job matcher logic
author: Sham Ganesh Thamarai Kannan
"""

import unittest
from unittest import mock
import pandas

from src.job_matching_logic import evaluate_job

def get_user_data(self):
    """mock user data"""
    return {
        "user_name": "Ash Ketchum",
        "user_mail": "ashk@pokemon.com"
    }

def get_preferences(self):
    """mock user preferences"""
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

    def setUp(self):
        """set up at start of testing"""
        self.suitable_tags = {"user_skills": [
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
        ],
        "min_salary": 1
        }

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

    @mock.patch("src.user_data_manager.DataManager.get_preferences")
    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_different_skills_unsuitable_salary(self, comparison_score, preferences):
        preferences.return_value = {"user_skills": [
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
        ],
        "min_salary": 1
        }
        comparison_score.return_value = 30

        job_details = {
            "salary": self.unsuitable_salary,
            "tags": self.unsuitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    @mock.patch("src.user_data_manager.DataManager.get_preferences")
    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_different_skills_suitable_salary(self, comparison_score, preferences):
        preferences.return_value = {"user_skills": [
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
        ],
        "min_salary": 1
        }
        comparison_score.return_value = 40

        job_details = {
            "salary": self.suitable_salary,
            "tags": self.unsuitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    @mock.patch("src.user_data_manager.DataManager.get_preferences")
    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_matched_skills_unsuitable_salary(self, comparison_score, preferences):
        preferences.return_value = {"user_skills": [
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
        ],
        "min_salary": 1
        }
        comparison_score.return_value = 85

        job_details = {
            "salary": self.unsuitable_salary,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    @mock.patch("src.user_data_manager.DataManager.get_preferences")
    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_matched_skills_suitable_salary(self, comparison_score, preferences):
        preferences.return_value = {"user_skills": [
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
        ],
        "min_salary": 1
        }
        comparison_score.return_value = 85

        job_details = {
            "salary": self.suitable_salary,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertTrue(suitability)

    @mock.patch("src.user_data_manager.DataManager.get_preferences")
    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_matched_skills_exact_salary(self, comparison_score, preferences):
        preferences.return_value = {"user_skills": [
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
        ],
        "min_salary": 1
        }
        comparison_score.return_value = 85

        job_details = {
            "salary": 1,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertTrue(suitability)

    @mock.patch("src.user_data_manager.DataManager.get_preferences")
    @mock.patch("src.nlp_processor.NlpProcessor.compare_keywords")
    def test_matched_skills_exact_skills(self, comparison_score, preferences):
        preferences.return_value = {"user_skills": [
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
        ],
        "min_salary": 1
        }
        comparison_score.return_value = 65

        job_details = {
            "salary": 1,
            "tags": self.suitable_tags
        }

        suitability = evaluate_job(job_details)
        self.assertTrue(suitability)

    @mock.patch("src.user_data_manager.DataManager.get_preferences")
    def test_case_when_detail_not_job(self, preferences):
        preferences.return_value = {"user_skills": [
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
        ],
        "min_salary": 1
        }

        job_details = {}

        suitability = evaluate_job(job_details)
        self.assertFalse(suitability)

    """
    @mock.patch("src.user_data_manager.DataManager.get_user_data", side_effect = get_user_data)
    @mock.patch("src.user_data_manager.DataManager.get_preferences", side_effect = get_preferences)
    """