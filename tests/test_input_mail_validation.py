"""
File to test the functions that handle user main
address input validation.
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D1 - Custom Project - Job Matcher
"""

import unittest
from src.user_input_validation import validate_email

"""
Test documentation link: https://docs.google.com/spreadsheets/d/1m5PbyeRgWhdzUZFkYmPZjyFC4LP-1b0k/edit?usp=sharing&ouid=100177938618106623512&rtpof=true&sd=true
			                                        Pairwise Testing

ID  Mail Address | Name in Legal | Has "@"  |	Mail Domain	 |  Domain in Legal | Has "."   |  Top Level 	|TLD within Legal
    Name >=3chr    Characters      separator    >=3chr          Characters        separator    Domain (TLD)    Characters
                                                                                                >=2chr
T01 False           False           False       True            True                True        True            False
T02 True            True            True        False           False               False       False           False
T03 True            False           True        True            False               True        False           True
T04 True            True            False       False           True                False       True            True
T05 False           True            True        False           True                True        False           True
T06 False           True            False       True            False               False       False           True
T07 False           False           True        False           False               False       True            True

"""

class TestMailInputValidation(unittest.TestCase):

    def test_mail_without_at_separator_short_invalid_t01(self):
        mail = "*/domain.co^"
        valid = validate_email(mail)
        self.assertFalse(valid)

    def test_mail_without_dot_separator_short_invalid_t02(self):
        mail = "*mail@doc^"
        valid = validate_email(mail)
        self.assertFalse(valid)

    def test_mail_invalid_char_tld_short_t03(self):
        mail = "*ma*l@doma^n.c"
        valid = validate_email(mail)
        self.assertFalse(valid)

    def test_mail_no_separator_short_domain_t04(self):
        mail = "maildocom"
        valid = validate_email(mail)
        self.assertFalse(valid)

    def test_mail_invalid_name_short_domain_t05(self):
        mail = "ma@d^.c"
        valid = validate_email(mail)
        self.assertFalse(valid)

    def test_mail_no_at_separator_invalid_chars_in_domain_t06(self):
        mail = "mado^mainc"
        valid = validate_email(mail)
        self.assertFalse(valid)

    def test_mail_short_name_invalid_domain_t07(self):
        mail = "*@do^.com"
        valid = validate_email(mail)
        self.assertFalse(valid)
