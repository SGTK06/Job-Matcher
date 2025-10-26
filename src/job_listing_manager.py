import pandas as pd
from src.config import SAVED_LISTINGS

class ListingManager:
    """
    class to read the csv data of jobs stored in csv files
    for processing as dataframes
    """
    def __init__(self):
        self.listings_data_frame = pd.read_csv(SAVED_LISTINGS)

    def has_matched_listings(self):
        """returns if the user has listings matched to profile"""
        return not self.listings_data_frame.empty

    def register_listing(self):
        """add new listing to saved listings in a pandas dataframe"""

    def get_listings(self):
        """get listings saved in the file as a list of Job objects"""

    def save_listings(self):
        """save the listings in the dataframe to a csv file"""

