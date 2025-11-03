"""
File to test the functions that handle user input
skills validation.
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D1 - Custom Project - Job Matcher
"""

import unittest
from src.user_input_validation import *

"""
Test Documentation: https://docs.google.com/spreadsheets/d/17EsnG-hwmBI43FiFopm1kA_hEeZ8p_mR/edit?usp=sharing&ouid=100177938618106623512&rtpof=true&sd=true
		Equivalence Partitioning
Test ID	Number of 	Skills Validation 	Skills Validation
        Skills      (Expected)          (Actual)
T01	      2	        FALSE	            FALSE
T02	      8	        TRUE	            TRUE





		Boundary Value Analysis
Test ID	Number of 	Skills Validation 	Skills Validation
        Skills      (Expected)          (Actual)
T03	    4	        FALSE	            FALSE
T04	    5	        TRUE	            TRUE
T05	    6	        TRUE	            TRUE



		            Edge Cases
Test ID	Edge Case           Skills Validation 	Skills Validation
        Description         (Expected)          (Actual)
T06	    blank whitespace 	FALSE	            FALSE
        input '   '
T07	    repeating 	        FALSE	            FALSE
        same skills
        (6 but 4 unique)

"""


class TestInputValidation(unittest.TestCase):
    """class to test the validation logic og the user input"""


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