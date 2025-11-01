"""
File to test the function that handles username
validation.
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D1 - Custom Project - Job Matcher
"""

import unittest
from src.user_input_validation import validate_user_name

"""
Tests to check whether the user input is validated properly
Validation of username
->Expected:
    - username greater than 5 characters in length is allowed
      else, they are rejected
    - tested using equivalence partitioning and boundary value
      analysis

test documentation link: https://docs.google.com/spreadsheets/d/19rBCg4nQodCvVc6PR-gtrDfqX90xzRkh/edit?usp=sharing&ouid=100177938618106623512&rtpof=true&sd=true

Boundary Value: len(username) = 5
Partitions: len(username) <= 5, len(username) > 5

Tests:
		        Equivalence Partitioning
Test ID	    Username Length	    Username Validation 	Username Validation
                                (Expected)              (Actual)
T01	        2   (<min length)	FALSE	                FALSE
T02	        10  (>min length)	TRUE	                TRUE


		        Boundary Value Analysis
Test ID	    Username Length	    Username Validation 	Username Validation
                                (Expected)              (Actual)
T03	        4	                FALSE	                FALSE
T04	        5	                FALSE	                FALSE
T05	        6	                TRUE	                TRUE

Edge case:
*Check if only whitespace inputs are rejected
*Check if whitespaces are stripped

Test ID	    Username Length	    Leading and Trailing    Effective Length    Username Validation 	Username Validation
                                whitespaces
T06         6                   6                       0                   FALSE                   FALSE
T07         6                   2                       4                   FALSE                   FALSE

"""

class TestInputValidation(unittest.TestCase):
    """class to test the validation logic of the user name input"""

    def test_short_user_name_t01(self):
        """
        test case to check if short user name
        input is rejected by the validation logic
        """
        user_name = "ab"
        self.assertFalse(validate_user_name(user_name))

    def test_long_user_name_t02(self):
        """
        test case to check if long user name 10chrs
        input is accepted by the validation logic
        """
        user_name = "abcdefghij"
        self.assertTrue(validate_user_name(user_name))

    def test_before_boundary_user_name_t03(self):
        """
        test case to check if 4 chr user name input
        is rejected by the validation logic
        BVA before boundary case
        """
        user_name = "abcd"
        self.assertFalse(validate_user_name(user_name))

    def test_boundary_len_user_name_t04(self):
        """
        test case to check if 5 chr user name input
        is rejected by the validation logic
        BVA boundary case
        """
        user_name = "abcde"
        self.assertFalse(validate_user_name(user_name))

    def test_after_boundary_user_name_t05(self):
        """
        test case to check if 6 chr user name input
        is accepted by the validation logic
        BVA after boundary case
        """
        user_name = "abcdef"
        self.assertTrue(validate_user_name(user_name))

    def test_whitespace_user_name_t06(self):
        """
        test case to check if space user name
        input is rejected by the validation logic
        """
        empty_name = "      "
        self.assertFalse(validate_user_name(empty_name))

    def test_space_strip_user_name_t07(self):
        """
        test case to check if leading and trailing
        spaces in user name input are stripped before
        evaluation  by the validation logic
        """
        blank_name = " abcd "
        self.assertFalse(validate_user_name(blank_name))