"""
File to test the functions that handle user input
validation.
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D1 - Custom Project - Job Matcher
"""

import unittest
from src.user_input_validation import *

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

"""


class TestInputValidation(unittest.TestCase):
    """class to test the validation logic og the user input"""

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

    def test_less_skills(self):
        """test case to check if a low number of skills input is rejected
        eqv partiiton"""
        skill_string = "skill1, skill2"
        self.assertFalse(validate_skills(skill_string))

    def test_4_skills(self):
        """test case to check if input of 4 skills input is rejected
        BVA"""
        skill_string = "skill1, skill2, skill3, skill4"
        self.assertFalse(validate_skills(skill_string))

    def test_appropriate_skills(self):
        """test case to check if input of 5 skills input is accepted
        BVA"""
        skill_string = "skill1, skill2, skill3, skill4, skill5"
        self.assertTrue(validate_skills(skill_string))

    def test_one_extra_skills(self):
        """test case to check if input of 6 skills input is accepted
        BVA"""
        skill_string = "skill1, skill2, skill3, skill4, skill5, skill6"
        self.assertTrue(validate_skills(skill_string))

    def test_large_number_of_skills(self):
        """test case to check if a lot of skills input is accepted
        eqv part"""
        skill_string = "skill1, skill2, skill3, skill4, skill5, skill6, s7, s8, s9, s10, s11, s12, s13. s14"
        self.assertTrue(validate_skills(skill_string))