import re

def validate_user_name(user_name):
    """
    Function to check if the given user name input is valid.
    User name is considered valid if:
        - user name is not empty
        - user name is longer than 5 characters
    If valid -> returns True
    else     -> returns False
    """
    if len(user_name.strip()) <= 5:
        return False
    else:
        return True

def validate_email(email):
    """
    Function used to validate the email address input by user.
    Email address is considered valid if the mail matches the regular expression
    for mail ids:
        ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
        (e.g. mailaddr@exampledomain.extension)
    """
    mail_regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(mail_regex, email):
        return True
    else:
        return False

def validate_skills(skill_string):
    """
    Function to validate the string of skills entered by user.
    The string od skills is considered valid if the user has
    entered atleast 5 skills.
    """
    pass