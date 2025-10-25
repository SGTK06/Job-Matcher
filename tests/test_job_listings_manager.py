import unittest

import pandas as pd

from src.job_listing_manager import ListingManager
from src.config import SAVED_LISTINGS

class TestListingManager(unittest.TestCase):
    """Test suite to check the listing manager"""

    @classmethod
    def setUpClass(cls):
        listing_manager = ListingManager()
        #make deep copy to prevent mutation of user data during testing
        cls.production_listings_data = listing_manager.listings_data_frame.copy(deep=True)

        #keep file headers only for testing
        saved_listings = pd.read_csv(SAVED_LISTINGS, nrows=0)
        saved_listings.to_csv(SAVED_LISTINGS, index=False)

    @classmethod
    def tearDownClass(cls):
        cls.production_listings_data.to_csv(SAVED_LISTINGS, index=False)

    def test_initialization(self):
        listing_manager = ListingManager()
        self.assertTrue(True)

