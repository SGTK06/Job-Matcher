import unittest
from unittest import mock

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

    def setUp(self):
        self.listings_manager = ListingManager()
        self.listings_data = {
            "id": [1],
            "url": ["self.url.link"],
            "title": ["job listing"],
            "company_name": ["comp"],
            "company_logo": ["logo.png"],
            "category": ["categotry1"],
            "tags": ["skill1"],
            "job_type": ["onsite"],
            "publication_date": ["20/10/25"],
            "candidate_required_location": ["ny"],
            "salary": ["10"],
            "description": ["testing"],
            "application_status": ["in progress"]
        }

    def test_initialization(self):
        listing_manager = ListingManager()
        self.assertTrue(True)

    def test_initial_listings(self):
        self.assertFalse(self.listings_manager.has_matched_listings())

    @mock.patch("pandas.read_csv")
    def test_listings_after_loading_data(self, job_df):
        # Create DataFrame
        job_df.return_value = pd.DataFrame(self.listings_data)

        new_manager = ListingManager()
        self.assertTrue(new_manager.has_matched_listings())

    @mock.patch("pandas.read_csv")
    def test_get_empty_listings_data(self, job_df):
        job_df.return_value = pd.DataFrame({
            "id": [],
            "url": [],
            "title": [],
            "company_name": [],
            "company_logo": [],
            "category": [],
            "tags": [],
            "job_type": [],
            "publication_date": [],
            "candidate_required_location": [],
            "salary": [],
            "description": [],
            "application_status": []
        })
        empty_data = []
        self.assertEqual(self.listings_manager.get_listings(), empty_data)

    def test_register_listing_initial(self):
        self.listings_manager.register_listing({
            "id": 1,
            "url": "self.url.link",
            "title": "job listing",
            "company_name": "comp",
            "company_logo": "logo.png",
            "category": "categotry1",
            "tags": "skill1",
            "job_type": "onsite",
            "publication_date": "20/10/25",
            "candidate_required_location": "ny",
            "salary": "10",
            "description": "testing",
            "application_status": "in progress"
        })
        self.assertEqual(
            self.listings_manager.listings_data_frame,
            pd.DataFrame(self.listings_data)
        )

    def test_register_listing_duplicate(self):
        self.listings_manager.register_listing({
            "id": 1,
            "url": "self.url.link",
            "title": "job listing",
            "company_name": "comp",
            "company_logo": "logo.png",
            "category": "categotry1",
            "tags": "skill1",
            "job_type": "onsite",
            "publication_date": "20/10/25",
            "candidate_required_location": "ny",
            "salary": "10",
            "description": "testing",
            "application_status": "in progress"
        })
        self.listings_manager.register_listing({
            "id": 1,
            "url": "self.url.link",
            "title": "job listing",
            "company_name": "comp",
            "company_logo": "logo.png",
            "category": "categotry1",
            "tags": "skill1",
            "job_type": "onsite",
            "publication_date": "20/10/25",
            "candidate_required_location": "ny",
            "salary": "10",
            "description": "testing",
            "application_status": "in progress"
        })
        self.assertEqual(
            self.listings_manager.listings_data_frame,
            pd.DataFrame(self.listings_data)
        )

    @mock.patch("pandas.read_csv")
    def test_register_listing(self, job_df):
        job_df.return_value = pd.DataFrame(self.listings_data)

        new_manager = ListingManager()

        new_manager.register_listing({
            "id": 2,
            "url": "self.url2.link",
            "title": "job listing2",
            "company_name": "comp2",
            "company_logo": "logo2.png",
            "category": "categotry2",
            "tags": "skill2",
            "job_type": "onsite2",
            "publication_date": "20/10/25",
            "candidate_required_location": "ny",
            "salary": "20",
            "description": "testing",
            "application_status": "in progress"
        })

        return_data = [{
            "id": 1,
            "url": "self.url.link",
            "title": "job listing",
            "company_name": "comp",
            "company_logo": "logo.png",
            "category": "categotry1",
            "tags": "skill1",
            "job_type": "onsite",
            "publication_date": "20/10/25",
            "candidate_required_location": "ny",
            "salary": "10",
            "description": "testing",
            "application_status": "in progress"
        },
        {
            "id": 2,
            "url": "self.url2.link",
            "title": "job listing2",
            "company_name": "comp2",
            "company_logo": "logo2.png",
            "category": "categotry2",
            "tags": "skill2",
            "job_type": "onsite2",
            "publication_date": "20/10/25",
            "candidate_required_location": "ny",
            "salary": "20",
            "description": "testing",
            "application_status": "in progress"
        }]

        self.assertEqual(
            new_manager.get_listings(),
            return_data
        )