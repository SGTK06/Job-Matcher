import pandas as pd
from src.config import *

class DataManager:
    """
    class to read csv data and manage the user data in csv files
    """
    def __init__(self):
        self.user_data_frame = pd.read_csv(USER_DATA)
        self.user_preferences = pd.read_csv(USER_PREFERENCES)

    def is_signed_in(self):
        return not self.user_data_frame.empty

    def get_user_data(self):
        """
        returns user data loaded from csv file
        if data is not available, it return dict with
        empty strings
        """
        if self.is_signed_in():
            user_data = self.user_data_frame.fillna("").iloc[0].to_dict()
        else:
            user_data = {}
            for column in self.user_data_frame.columns:
                user_data[column] = ""
        return user_data

    def register_user(self, user_name, user_mail):
        new_user_data = {
            "user_name" : user_name,
            "user_mail" : user_mail
        }

        if not self.user_data_frame.empty:
            self.user_data_frame.loc[self.user_data_frame.index[0]] = new_user_data
        else:
            self.user_data_frame = pd.DataFrame([new_user_data])

        return True

    def save_user(self):
        self.user_data_frame.to_csv(USER_DATA, index=False, encoding="utf-8")
        return True

    def register_preferences(self, skills, min_salary):
        """
        This function is used to save the user preferences for the app
        This takes skills string and minimum salary as inputs and saves
        it in a dataframe:
        """

    def get_preferences(self):
        """
        This function returns the preferences of the user in the form
        of a dictionary.
        """

    def has_preferences(self):
        """
        This function returns if the user has selected preferences
        previously as boolean
         - True : if user has selected preferences
         - False : if user has not selected preferences before
        """
        return not self.user_preferences.empty