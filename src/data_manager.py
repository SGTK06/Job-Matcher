import pandas as pd
from src.config import *

class DataManager:
    """
    class to read csv data and manage the user data in csv files
    """
    def __init__(self):
        self.user_data_frame = pd.read_csv(USER_DATA)

    def is_signed_in(self):
        return self.user_data_frame.empty