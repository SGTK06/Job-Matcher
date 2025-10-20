"""
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D1 - Custom Project - Job Matcher
"""

import unittest
from src.user_input_validation import validate_user_name, validate_email

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

    def test_space_user_name(self):
        """test case to check if space user name input is rejected by the validation logic"""
        empty_name = "        "
        self.assertFalse(validate_user_name(empty_name))

    def test_empty_mail(self):
        """test case to check if the empty mail id is rejected"""
        empty_mail_id = ""
        self.assertFalse(validate_email(empty_mail_id))

    def test_no_separator_mail(self):
        """test case to check if the no separator @ mail id is rejected"""
        empty_mail_id = "maildomain.com"
        self.assertFalse(validate_email(empty_mail_id))

    def test_no_id_mail(self):
        """test case to check if the no address mail id is rejected"""
        empty_mail_id = "@domain.com"
        self.assertFalse(validate_email(empty_mail_id))

    def test_no_domain_mail(self):
        """test case to check if the no domain mail id is rejected"""
        empty_mail_id = "mail@.com"
        self.assertFalse(validate_email(empty_mail_id))

    def test_no_extension_mail(self):
        """test case to check if the no extension mail id is rejected"""
        empty_mail_id = "mail@domain"
        self.assertFalse(validate_email(empty_mail_id))

    def test_valid_mail(self):
        """test case to check if the valid mail id is accepted"""
        empty_mail_id = "mail@domain.extension"
        self.assertTrue(validate_email(empty_mail_id))