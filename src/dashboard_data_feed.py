import pandas as pd

from src.job_listing_manager import ListingManager

class DashboardDataFeed:
    def __init__(self):
        listing_manager = ListingManager()
        all_jobs = listing_manager.get_listings()