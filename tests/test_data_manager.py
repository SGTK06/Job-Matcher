"""
File to test the user data manager class
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D2
"""

import unittest
import pandas
from unittest import mock

from src.user_data_manager import DataManager
from src.config import *

"""
Testing DataManager to check if user data is handled
as expected:
Blackbox Tests:
BT01. Create manager object
BT02. Check initial signed-in state
BT03. Load user data from csv and chk signed in
BT04. Get user data when loaded from mocked csv read
BT05. Get user data when file is empty
BT06. Register user (new user) when file is empty
BT07. Register user (overwrite existing user) when file has data (mocked csv read)
BT08. Check initial has preferences is False
BT09. Check has preferences after loading preferences from csv
      (mocked csv read)
BT10. Check get preferences after loading preferences from csv
      (chk mocked csv read output is formatted correctly)
BT11. Check get preferences after loading preferences from empty csv
      (load current state of csv in testing env (empty file))
BT12. Register Preferences processes preferences to correct data format
      initial (no current preferences)
BT13. Register Preferences processes preferences to correct data format
      with existing preferences (overwrite preferences)

Whitebox Tests:
WT01. Test file does not exist case
      (to check if file not dound error is handled)
"""
def raise_fnf_error():
    raise FileNotFoundError


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

        self.data_manager = DataManager()

    @classmethod
    def setUpClass(cls):
        data_manager = DataManager()
        #make deep copy to prevent mutation of user data during testing
        cls._production_user_data = data_manager.user_data_frame.copy(deep=True)
        cls._production_user_pref = data_manager.user_preferences.copy(deep=True)

        #keep headers only
        user_data_headers = pandas.read_csv(USER_DATA, nrows=0)
        user_pref_headers = pandas.read_csv(USER_PREFERENCES, nrows=0)
        user_data_headers.to_csv(USER_DATA, index=False)
        user_pref_headers.to_csv(USER_PREFERENCES, index=False)

    @classmethod
    def tearDownClass(cls):
        cls._production_user_data.to_csv(USER_DATA, index=False)
        cls._production_user_pref.to_csv(USER_PREFERENCES, index=False)

    def test_initialization_bt01(self):
        data_manager = DataManager()
        self.assertTrue(True)

    def test_initial_signed_in_bt02(self):
        self.assertFalse(self.data_manager.is_signed_in())

    @mock.patch("pandas.read_csv")
    def test_signed_in_after_loading_data_bt03(self, user_df):
        # Create DataFrame
        user_df.return_value = pandas.DataFrame(self.user_data)

        new_manager = DataManager()
        self.assertTrue(new_manager.is_signed_in())

    @mock.patch("pandas.read_csv")
    def test_get_user_data_bt04(self, user_df):
        # Create DataFrame
        user_df.return_value = pandas.DataFrame(self.user_data)
        return_data = {
            "user_name": "Peter",
            "user_mail": "parker@marvel.com"
        }
        new_manager = DataManager()
        self.assertEqual(new_manager.get_user_data(), return_data)

    def test_get_empty_user_data_bt05(self):
        empty_data = {
            "user_name" : "",
            "user_mail" : ""
        }
        self.assertEqual(self.data_manager.get_user_data(), empty_data)

    def test_register_user_once_bt06(self):
        self.data_manager.register_user("abc", "abc@def.com")
        return_data = {
            "user_name": "abc",
            "user_mail": "abc@def.com"
        }
        self.assertEqual(self.data_manager.get_user_data(), return_data)

    def test_register_user_overwrite_details_bt07(self):
        self.data_manager.register_user("a1b2", "a12@bc3.com")
        self.data_manager.register_user("abc", "abc@def.com")
        return_data = {
            "user_name": "abc",
            "user_mail": "abc@def.com"
        }
        self.assertEqual(self.data_manager.get_user_data(), return_data)

    def test_initial_preferences_bt08(self):
        self.assertFalse(self.data_manager.has_preferences())

    @mock.patch("pandas.read_csv")
    def test_loaded_preferences_bt09(self, pref_df):
        pref_df.return_value = pandas.DataFrame(self.user_preferences)
        new_manager = DataManager()
        self.assertTrue(new_manager.has_preferences())

    @mock.patch("pandas.read_csv")
    def test_get_preferences_data_bt10(self, pref_df):
        # Create DataFrame
        pref_df.return_value = pandas.DataFrame(self.user_preferences)
        return_data = {
            "user_skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
            "min_salary": 10
        }
        new_manager = DataManager()
        self.assertEqual(new_manager.get_preferences(), return_data)

    def test_get_empty_preferences_data_bt11(self):
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

    @mock.patch("pandas.read_csv")
    def test_missing_file_error_handled_wt01(self, reader):
        reader.side_effect = raise_fnf_error
        new_manager = DataManager()
        self.assertTrue(True)

