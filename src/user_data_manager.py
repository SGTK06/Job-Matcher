import os
import pandas as pd
from src.config import USER_DATA, USER_PREFERENCES, SAVED_LISTINGS

class DataManager:
    """
    class to read csv data and manage the user data in csv files
    """
    def __init__(self):
        """
        constructor for data manager
        """
        self.user_data_frame = pd.read_csv(USER_DATA)
        self.user_preferences = pd.read_csv(USER_PREFERENCES)
        self.saved_listings = pd.read_csv(SAVED_LISTINGS)

    def load_file_or_create(self, filepath, columns):
        try:
            # Try to read the existing csv
            df = pd.read_csv(filepath)
            return df

        except FileNotFoundError:
            print(f"File not found: {filepath}")
            print(f"Creating new file with columns: {columns}")

            # Ensure directory exists
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
                print(f"Created directory: {directory}")

            # Create empty df with columns
            df = pd.DataFrame(columns=columns)

            # Save the empty DataFrame to create the file
            df.to_csv(filepath, index=False, encoding="utf-8")
            print(f"Created new CSV file: {filepath}")

            return df

        except pd.errors.EmptyDataError:
            # File exists but is empty
            print(f"File is empty: {filepath}")
            print(f"Initializing with columns: {columns}")

            df = pd.DataFrame(columns=columns)
            df.to_csv(filepath, index=False, encoding="utf-8")

            return df

        except Exception as e:
            # handle other unexpected errors
            print(f"Error loading {filepath}: {e}")
            print(f"Creating new file with columns: {columns}")

            # check if dir exists
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            df = pd.DataFrame(columns=columns)
            df.to_csv(filepath, index=False, encoding="utf-8")

            return df

    def is_signed_in(self):
        """
        returns True of user is signed in
        else, returns false
        """
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
        """
        used for registering user (storing
        data in dataframe)
        """
        new_user_data = {
            "user_name": user_name,
            "user_mail": user_mail
        }

        if not self.user_data_frame.empty:
            self.user_data_frame.loc[self.user_data_frame.index[0]] = new_user_data
        else:
            self.user_data_frame = pd.DataFrame([new_user_data])

        return True

    def save_user(self):
        """
        function to save data in dataframe in csv file
        """
        self.user_data_frame.to_csv(USER_DATA, index=False, encoding="utf-8")
        return True

    def register_preferences(self, skills, min_salary):
        """
        This function is used to save the user preferences for the app
        This takes skills string and minimum salary as inputs and saves
        it in a dataframe:
        """
        new_user_pref = {
            "user_skills": skills,
            "min_salary": min_salary
        }

        if not self.user_preferences.empty:
            self.user_preferences.loc[self.user_preferences.index[0]] = new_user_pref
        else:
            self.user_preferences = pd.DataFrame([new_user_pref])

        return True

    def get_preferences(self):
        """
        This function returns the preferences of the user in the form
        of a dictionary.
        """
        if self.has_preferences():
            user_pref = self.user_preferences.fillna("").iloc[0].to_dict()
            for key in user_pref:
                if key == "user_skills":
                    user_pref[key] = self.skill_set(user_pref[key])
                elif key == "min_salary":
                    try:
                        user_pref[key] = int(user_pref[key])
                    except ValueError:
                        user_pref[key] = 0

        else:
            user_pref = {}
            for column in self.user_preferences.columns:
                if column == "user_skills":
                    user_pref[column] = []
                elif column == "min_salary":
                    user_pref[column] = 0
                else:
                    user_pref[column] = ""

        return user_pref

    def has_preferences(self):
        """
        This function returns if the user has selected preferences
        previously as boolean
         - True : if user has selected preferences
         - False : if user has not selected preferences before
        """
        return not self.user_preferences.empty

    def skill_set(self, skill_string):
        """
        converts a string of skills to list of skills
        """
        skills = []
        for skill in skill_string.strip().split(","):
            skills.append(skill.strip())

        return skills

    def save_preferences(self):
        """
        function to save preferences in csv file
        """
        self.user_preferences.to_csv(USER_PREFERENCES, index=False, encoding="utf-8")
        return True
