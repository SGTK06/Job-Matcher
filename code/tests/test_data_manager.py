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
WT02. Test save input is of the wrong type

For Coverage Tests:
WT03. Test unexpected exceptions while file reading
WT04. Test save user to file
WT05. Test save preferences to file
"""
def raise_fnf_error(file):
    """rasise fnf error"""
    raise FileNotFoundError

def raise_empty_file_error(file):
    """rasise empty file error"""
    raise pandas.errors.EmptyDataError

def raise_unexpected_error(file):
    """rasise base error"""
    raise BaseException


class TestDataManager(unittest.TestCase):
    """
    class that tests the successful parsing od csv data
    by data manager
    """
    def setUp(self):
        """setup once at start"""
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
        """set up testing environment while class setup"""
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
        """restore prodcution environment while class teardown"""
        cls._production_user_data.to_csv(USER_DATA, index=False)
        cls._production_user_pref.to_csv(USER_PREFERENCES, index=False)

    def test_initialization_bt01(self):
        """test obj creation of data manager"""
        data_manager = DataManager()
        self.assertTrue(True)

    def test_initial_signed_in_bt02(self):
        """test if signed in initailly"""
        self.assertFalse(self.data_manager.is_signed_in())

    @mock.patch("pandas.read_csv")
    def test_signed_in_after_loading_data_bt03(self, user_df):
        """test if signed in after loading fake data"""
        # Create DataFrame
        user_df.return_value = pandas.DataFrame(self.user_data)

        new_manager = DataManager()
        self.assertTrue(new_manager.is_signed_in())

    @mock.patch("pandas.read_csv")
    def test_get_user_data_bt04(self, user_df):
        """test if fetting file data after loading fake data"""
        # Create DataFrame
        user_df.return_value = pandas.DataFrame(self.user_data)
        return_data = {
            "user_name": "Peter",
            "user_mail": "parker@marvel.com"
        }
        new_manager = DataManager()
        self.assertEqual(new_manager.get_user_data(), return_data)

    def test_get_empty_user_data_bt05(self):
        """test if getting data with empty file"""
        empty_data = {
            "user_name" : "",
            "user_mail" : ""
        }
        self.assertEqual(self.data_manager.get_user_data(), empty_data)

    def test_register_user_once_bt06(self):
        """test registering user once first time"""
        self.data_manager.register_user("abc", "abc@def.com")
        return_data = {
            "user_name": "abc",
            "user_mail": "abc@def.com"
        }
        self.assertEqual(self.data_manager.get_user_data(), return_data)

    def test_register_user_overwrite_details_bt07(self):
        """test registering user twice to overrride old details"""
        self.data_manager.register_user("a1b2", "a12@bc3.com")
        self.data_manager.register_user("abc", "abc@def.com")
        return_data = {
            "user_name": "abc",
            "user_mail": "abc@def.com"
        }
        self.assertEqual(self.data_manager.get_user_data(), return_data)

    def test_initial_preferences_bt08(self):
        """test if it has preferences stored initially"""
        self.assertFalse(self.data_manager.has_preferences())

    @mock.patch("pandas.read_csv")
    def test_loaded_preferences_bt09(self, pref_df):
        """test has preferences with fake data read"""
        pref_df.return_value = pandas.DataFrame(self.user_preferences)
        new_manager = DataManager()
        self.assertTrue(new_manager.has_preferences())

    @mock.patch("pandas.read_csv")
    def test_get_preferences_data_bt10(self, pref_df):
        """test getting preferences with fake data read"""
        # Create DataFrame
        pref_df.return_value = pandas.DataFrame(self.user_preferences)
        return_data = {
            "user_skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
            "min_salary": 10
        }
        new_manager = DataManager()
        self.assertEqual(new_manager.get_preferences(), return_data)

    def test_get_empty_preferences_data_bt11(self):
        """test getting preferences with empty file read"""
        empty_data = {
            "user_skills": [],
            "min_salary": 0
        }
        self.assertEqual(self.data_manager.get_preferences(), empty_data)

    def test_register_preferences_once(self):
        """register once to save details for first tkme simulation"""
        self.data_manager.register_preferences("skill1, skill2, skill3, skill4, skill5", "10")
        return_data = {
            "user_skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
            "min_salary": 10
        }
        self.assertEqual(self.data_manager.get_preferences(), return_data)

    def test_register_preferences_change_details(self):
        """register again overrides old preferences"""
        self.data_manager.register_preferences("skill1, skill2, skill3, skill4, skill5,", "10")
        self.data_manager.register_preferences("skill1, skill2, skill3, skill4, skill5, skill6", "20")
        return_data = {
            "user_skills": ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6"],
            "min_salary": 20
        }
        self.assertEqual(self.data_manager.get_preferences(), return_data)

    @mock.patch("pandas.read_csv")
    def test_missing_file_error_handled_wt01_a(self, reader):
        """chk if missing file error is handled"""
        reader.side_effect = raise_fnf_error
        new_manager = DataManager()
        self.assertTrue(True)

    @mock.patch("pandas.read_csv")
    def test_empty_file_error_handled_wt01_b(self, reader):
        """test if empty file error is handled"""
        reader.side_effect = raise_empty_file_error
        new_manager = DataManager()
        self.assertTrue(True)

    def test_register_preferences_with_invalid_salary_wt02_a(self):
        """test if wrong input salary type is handled"""
        self.data_manager.register_preferences("skill1, skill2", "hundred")
        pref = self.data_manager.get_preferences()
        self.assertEqual(pref["min_salary"], 0)

    def test_register_preferences_with_invalid_skills_wt02_b(self):
        """test invalid skill datatype is handled"""
        self.data_manager.register_preferences(1234, 10)
        pref = self.data_manager.get_preferences()
        self.assertEqual(pref["user_skills"], ["1234"])

    @mock.patch("pandas.read_csv")
    def test_unexpected_error_handled_wt03(self, reader):
        """test unexpected errors handled"""
        reader.side_effect = raise_unexpected_error
        new_manager = DataManager()
        self.assertTrue(True)

    def test_register_and_save_user_wt04(self):
        """ test saving data """
        self.data_manager.register_user("abc", "abc@def.com")
        self.data_manager.save_user()
        new_manager = DataManager()
        return_data = {
            "user_name": "abc",
            "user_mail": "abc@def.com"
        }
        self.assertEqual(new_manager.get_user_data(), return_data)

    def test_register_and_save_preferences_wt04(self):
        """test savinf preferences"""
        self.data_manager.register_preferences("skill1, skill2, skill3, skill4, skill5", "10")
        self.data_manager.save_preferences()
        new_manager = DataManager()
        return_data = {
            "user_skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
            "min_salary": 10
        }
        self.assertEqual(new_manager.get_preferences(), return_data)