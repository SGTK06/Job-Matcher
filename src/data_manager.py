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