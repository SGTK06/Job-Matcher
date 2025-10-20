"""
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D1 - Custom Project - Job Matcher
"""

import unittest
from src.user_input_validation import validate_user_name

class TestInputValidation(unittest.TestCase):
    """class to test the validation logic og the user input"""

    def test_empty_user_name(self):
        """test case to check if empty user name input is rejected by the validation logic"""
        empty_name = ""
        self.assertFalse(validate_user_name(empty_name))

    def test_short_user_name(self):
        """test case to check if short user name input is rejected by the validation logic"""
        empty_name = "abcd"
        self.assertFalse(validate_user_name(empty_name))

    def test_5_chr_user_name(self):
        """test case to check if 5 chr user name input is rejected by the validation logic
        to test BVA edge case"""
        empty_name = "abcde"
        self.assertFalse(validate_user_name(empty_name))

    def test_6_chr_user_name(self):
        """test case to check if 6 chr user name input is accepted by the validation logic
        to test BVA case"""
        empty_name = "abcdef"
        self.assertTrue(validate_user_name(empty_name))

    def test_long_user_name(self):
        """test case to check if long user name input is accepted by the validation logic"""
        empty_name = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(validate_user_name(empty_name))