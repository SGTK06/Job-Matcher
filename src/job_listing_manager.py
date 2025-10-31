import pandas as pd
from src.config import SAVED_LISTINGS

class ListingManager:
    """
    class to read the csv data of jobs stored in csv files
    for processing as dataframes
    """
    def __init__(self):
        self.columns = [
            "id",
            "url",
            "title",
            "company_name",
            "company_logo",
            "category",
            "tags",
            "job_type",
            "publication_date",
            "candidate_required_location",
            "salary",
            "description",
            "application_status"
        ]
        try:
            self.listings_data_frame = pd.read_csv(SAVED_LISTINGS)
            self.listings_data_frame = self.listings_data_frame.reindex(columns=self.columns)
        except FileNotFoundError:
            self.listings_data_frame = pd.DataFrame(columns=self.columns)


    def has_matched_listings(self):
        """returns if the user has listings matched to profile"""
        return not self.listings_data_frame.empty

    def register_listing(self, new_listing):
        """add new listing to saved listings in a pandas dataframe"""
        if new_listing["id"] in self.listings_data_frame["id"].values:
            return
        else:
            self.listings_data_frame = pd.concat(
                [self.listings_data_frame, pd.DataFrame([new_listing])],
                ignore_index=True
            )

    def get_listings(self):
        """get listings saved in the file as a list of Job objects"""
        listing_dict = self.listings_data_frame.to_dict(orient="records")
        return listing_dict

    def save_listings(self):
        """save the listings in the dataframe to a csv file"""
        self.listings_data_frame.to_csv(SAVED_LISTINGS, index=False, mode="w",chunksize=1000)

