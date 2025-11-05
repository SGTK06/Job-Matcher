import unittest
import pandas
from unittest import mock

from src.job_listing_manager import ListingManager
from src.config import SAVED_LISTINGS

"""
Testing ListingManager to check if job listing data is handled
as expected:

Blackbox Tests:
BT01. Create manager object
BT02. Check initial has_matched_listings is False
BT03. Load listings data from csv and check listings exist (mocked read)
BT04. Get listings data when loaded from mocked csv read
BT05. Get listings when file is empty
BT06. Register new listing when file is empty
BT07. Register duplicate listing (should not duplicate entry)

Whitebox Tests:
WT01. Test file not found error handled
WT02. Test unexpected exception while file reading
WT03. Test save listings to file
"""

def raise_fnf_error(file):
    raise FileNotFoundError

def raise_unexpected_error(file):
    raise BaseException


class TestListingManager(unittest.TestCase):
    """
    class that tests the successful parsing of csv data
    by listing manager
    """

    @classmethod
    def setUpClass(cls):
        listing_manager = ListingManager()
        # make deep copy to prevent mutation of job data during testing
        cls._production_listing_data = listing_manager.listings_data_frame.copy(deep=True)

        # keep headers only
        listings_headers = pandas.read_csv(SAVED_LISTINGS, nrows=0)
        listings_headers.to_csv(SAVED_LISTINGS, index=False)

    @classmethod
    def tearDownClass(cls):
        cls._production_listing_data.to_csv(SAVED_LISTINGS, index=False)

    def setUp(self):
        self.listings_data = {
            "id": [1],
            "url": ["self.url.link"],
            "title": ["job listing"],
            "company_name": ["comp"],
            "company_logo": ["logo.png"],
            "category": ["category1"],
            "tags": ["skill1"],
            "job_type": ["onsite"],
            "publication_date": ["20/10/25"],
            "candidate_required_location": ["ny"],
            "salary": [10],
            "description": ["testing"],
            "application_status": ["in progress"]
        }

        self.new_listing = {
            "id": 2,
            "url": "self.url2.link",
            "title": "job listing2",
            "company_name": "comp2",
            "company_logo": "logo2.png",
            "category": "category2",
            "tags": "skill2",
            "job_type": "onsite2",
            "publication_date": "21/10/25",
            "candidate_required_location": "la",
            "salary": "20",
            "description": "testing2",
            "application_status": "in progress"
        }

        self.listing_manager = ListingManager()

    def test_initialization_bt01(self):
        listing_manager = ListingManager()
        self.assertTrue(True)

    def test_initial_no_listings_bt02(self):
        self.assertFalse(self.listing_manager.has_matched_listings())

    @mock.patch("pandas.read_csv")
    def test_listings_after_loading_data_bt03(self, job_df):
        job_df.return_value = pandas.DataFrame(self.listings_data)
        new_manager = ListingManager()
        self.assertTrue(new_manager.has_matched_listings())

    @mock.patch("pandas.read_csv")
    def test_get_listings_data_bt04(self, job_df):
        job_df.return_value = pandas.DataFrame(self.listings_data)
        new_manager = ListingManager()
        return_data = [{
            "id": 1,
            "url": "self.url.link",
            "title": "job listing",
            "company_name": "comp",
            "company_logo": "logo.png",
            "category": "category1",
            "tags": "skill1",
            "job_type": "onsite",
            "publication_date": "20/10/25",
            "candidate_required_location": "ny",
            "salary": 10,
            "description": "testing",
            "application_status": "in progress"
        }]
        self.assertEqual(new_manager.get_listings(), return_data)

    def test_get_empty_listings_bt05(self):
        empty_data = []
        self.assertEqual(self.listing_manager.get_listings(), empty_data)

    def test_register_listing_bt06(self):
        self.listing_manager.register_listing(self.new_listing)
        return_data = [self.new_listing]
        return_data[0]["salary"] = int(return_data[0]["salary"])
        self.assertEqual(self.listing_manager.get_listings(), return_data)

    def test_register_duplicate_listing_bt07(self):
        self.listing_manager.register_listing(self.new_listing)
        self.listing_manager.register_listing(self.new_listing)
        return_data = [self.new_listing]
        return_data[0]["salary"] = int(return_data[0]["salary"])
        self.assertEqual(self.listing_manager.get_listings(), return_data)

    @mock.patch("pandas.read_csv")
    def test_missing_file_error_handled_wt01(self, reader):
        reader.side_effect = raise_fnf_error
        new_manager = ListingManager()
        self.assertTrue(True)

    @mock.patch("pandas.read_csv")
    def test_unexpected_error_handled_wt02(self, reader):
        reader.side_effect = raise_unexpected_error
        new_manager = ListingManager()
        self.assertTrue(True)

    def test_register_and_save_listings_wt03(self):
        self.listing_manager.register_listing(self.new_listing)
        self.listing_manager.save_listings()
        new_manager = ListingManager()
        return_data = [self.new_listing]
        return_data[0]["salary"] = int(return_data[0]["salary"])
        self.assertEqual(new_manager.get_listings(), return_data)