import unittest
import pandas
from unittest import mock

from src.user_data_manager import DataManager
from src.config import *

class TestDataManager(unittest.TestCase):
    """
    class that tests the successful parsing od csv data
    by data manager
    """
    def setUp(self):

        self.user_data = {
            "user_name": ["Peter"],
            "user_mail": ["parker@marvel.com"]
        }

        self.user_preferences = {
            "user_skills": ["skill1, skill2, skill3, skill4, skill5"],
            "min_salary": [10]
        }

        self.set_up_testing_env()
        self.data_manager = DataManager()

    def tearDown(self):
        self.restore_production_env()

    def set_up_testing_env(self):
        data_manager = DataManager()
        #make deep copy to prevent mutation of user data during testing
        self._production_user_data = data_manager.user_data_frame.copy(deep=True)
        self._production_user_pref = data_manager.user_preferences.copy(deep=True)

        #keep headers only
        user_data_headers = pandas.read_csv(USER_DATA, nrows=0)
        user_pref_headers = pandas.read_csv(USER_PREFERENCES, nrows=0)
        user_data_headers.to_csv(USER_DATA, index=False)
        user_pref_headers.to_csv(USER_PREFERENCES, index=False)

    def restore_production_env(self):
        self._production_user_data.to_csv(USER_DATA, index=False)
        self._production_user_pref.to_csv(USER_PREFERENCES, index=False)

    def test_initialization(self):
        data_manager = DataManager()
        self.assertTrue(True)

    def test_initial_signed_in(self):
        self.assertFalse(self.data_manager.is_signed_in())

    @mock.patch("pandas.read_csv")
    def test_signed_in_after_loading_data(self, user_df):
        # Create DataFrame
        user_df.return_value = pandas.DataFrame(self.user_data)

        new_manager = DataManager()
        self.assertTrue(new_manager.is_signed_in())

    @mock.patch("pandas.read_csv")
    def test_get_user_data(self, user_df):
        # Create DataFrame
        user_df.return_value = pandas.DataFrame(self.user_data)
        return_data = {
            "user_name": "Peter",
            "user_mail": "parker@marvel.com"
        }
        new_manager = DataManager()
        self.assertEqual(new_manager.get_user_data(), return_data)

    def test_get_empty_user_data(self):
        empty_data = {
            "user_name" : "",
            "user_mail" : ""
        }
        self.assertEqual(self.data_manager.get_user_data(), empty_data)

    def test_register_user_once(self):
        self.data_manager.register_user("abc", "abc@def.com")
        return_data = {
            "user_name": "abc",
            "user_mail": "abc@def.com"
        }
        self.assertEqual(self.data_manager.get_user_data(), return_data)

    def test_register_user_change_details(self):
        self.data_manager.register_user("a1b2", "a12@bc3.com")
        self.data_manager.register_user("abc", "abc@def.com")
        return_data = {
            "user_name": "abc",
            "user_mail": "abc@def.com"
        }
        self.assertEqual(self.data_manager.get_user_data(), return_data)

    def test_initial_preferences(self):
        self.assertFalse(self.data_manager.has_preferences())

    @mock.patch("pandas.read_csv")
    def test_loaded_preferences(self, pref_df):
        pref_df.return_value = pandas.DataFrame(self.user_preferences)
        new_manager = DataManager()
        self.assertTrue(new_manager.has_preferences())

    @mock.patch("pandas.read_csv")
    def test_get_preferences_data(self, pref_df):
        # Create DataFrame
        pref_df.return_value = pandas.DataFrame(self.user_preferences)
        return_data = {
            "user_skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
            "min_salary": 10
        }
        new_manager = DataManager()
        self.assertEqual(new_manager.get_preferences(), return_data)

    def test_get_empty_preferences_data(self):
        empty_data = {
            "user_skills": [],
            "min_salary": 0
        }
        self.assertEqual(self.data_manager.get_preferences(), empty_data)

    def test_register_preferences_once(self):
        self.data_manager.register_preferences("skill1, skill2, skill3, skill4, skill5", "10")
        return_data = {
            "user_skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
            "min_salary": 10
        }
        self.assertEqual(self.data_manager.get_preferences(), return_data)

    def test_register_preferences_change_details(self):
        self.data_manager.register_preferences("skill1, skill2, skill3, skill4, skill5,", "10")
        self.data_manager.register_preferences("skill1, skill2, skill3, skill4, skill5, skill6", "20")
        return_data = {
            "user_skills": ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6"],
            "min_salary": 20
        }
        self.assertEqual(self.data_manager.get_preferences(), return_data)
