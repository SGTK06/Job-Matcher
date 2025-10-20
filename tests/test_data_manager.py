import unittest
import pandas

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