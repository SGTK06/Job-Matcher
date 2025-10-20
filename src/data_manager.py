import pandas as pd
from src.config import *

class DataManager:
    """
    class to read csv data and manage the user data in csv files
    """
    def __init__(self):
        self.user_data_frame = pd.read_csv(USER_DATA)

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