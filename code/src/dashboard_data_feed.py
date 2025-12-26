import pandas as pd

from src.job_listing_manager import ListingManager
from src.user_data_manager import DataManager

class DashboardDataFeed:
    def __init__(self):
        self.user_data_manager = DataManager()
        self.listing_manager = ListingManager()

    def get_user_status(self):
        """Get user sign-in and preferences status"""
        return {
            "is_signed_in": self.user_data_manager.is_signed_in(),
            "has_preferences": self.user_data_manager.has_preferences()
        }

    def get_user_preferences(self):
        """Get user preferences"""
        return self.user_data_manager.get_preferences()

    def get_data_feed(self):
        """get the feed of jobs to display"""
        data = []
        job_records = self.listing_manager.get_listings()
        return job_records

