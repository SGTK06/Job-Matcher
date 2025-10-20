import unittest
import pandas
from unittest import mock

from src.data_manager import DataManager

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

        self.data_manager = DataManager()

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

        new_manager = DataManager()
        self.assertEqual(new_manager.get_user_data(), self.user_data)

    def test_get_empty_user_data(self):
        empty_data = {
            "user_name" : "",
            "user_mail" : ""
        }
        self.assertEqual(self.data_manager.get_user_data(), empty_data)