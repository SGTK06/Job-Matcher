import unittest
import pandas
from unittest import mock

from src.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    """
    class that tests the successful parsing od csv data
    by data manager
    """
    def test_initialization(self):
        data_manager = DataManager()
        self.assertTrue(True)

    def test_signed_in(self):
        new_manager = DataManager()
        self.assertFalse(new_manager.is_signed_in())

    @mock.patch("pandas.read_csv")
    def test_signed_in_after_loading_data(self, user_df):
        # initialize data of lists.
        data = {"user_name": ["Peter"],
                "user_mail": ["parker@marvel.com"]}

        # Create DataFrame
        user_df.return_value = pandas.DataFrame(data)

        new_manager = DataManager()
        self.assertTrue(new_manager.is_signed_in())