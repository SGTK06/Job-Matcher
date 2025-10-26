import unittest
from datetime import datetime

from src.job_listing import JobListing

class TestjobListing(unittest.TestCase):
    """
    class for testing job listing objects
    """
    def setUp(self):
        self.job_details = {
            "id": 100,
            "url": "https://remotive.com/remote-jobs/",
            "title": "QA",
            "company_name" : "quantum",
            "company_logo" : "logo.png",
            "category" : "testing",
            "tags" : ["TDD", "CI/CD"],
            "job_type" : "remote",
            "publication_date" : "2025-10-24T14:51:03",
            "candidate_required_location" : "-",
            "salary" : "1",
            "description" : "<p>As a QA specializing in TDD.</p>\
                <p>Key Responsibilities:</p>"
        }

    def test_initialization(self):
        """tests if class converts API return data to job object"""
        job = JobListing(self.job_details)
        self.assertTrue(True)

    def test_time_correct_data_format(self):
        """tests if class converts API return data format
        to the expected format"""
        job = JobListing(self.job_details)
        self.assertEqual(job.publication_date, datetime.fromisoformat("2025-10-24T14:51:03"))

    def test_time_incorrect_data_format(self):
        """tests if class converts API return data format
        to the expected format"""
        mod_details = dict(self.job_details)
        mod_details["publication_date"] = "2025/10/24"
        job = JobListing(mod_details)
        self.assertEqual(job.publication_date, "2025/10/24")

    def test_description_format(self):
        """tests of returned description is formatted correctly"""
        job = JobListing(self.job_details)
        self.assertEqual(job.description, "As a QA specializing in TDD.")

    def test_description_non_html_format(self):
        """tests if class converts API return data format
        to the expected format"""
        mod_details = dict(self.job_details)
        mod_details["description"] = "Job Desc"
        job = JobListing(mod_details)
        self.assertEqual(job.description, "Job Desc")

    def test_salary_number_format(self):
        """tests if the salary data  returned by API is
        converted to float if number"""
        mod_details = dict(self.job_details)
        mod_details["salary"] = "10"
        job = JobListing(mod_details)
        self.assertEqual(job.salary, 10)

    def test_salary_text_format(self):
        """tests if the salary data  returned by API is
        converted to float if number"""
        mod_details = dict(self.job_details)
        mod_details["salary"] = "Competitive"
        job = JobListing(mod_details)
        self.assertEqual(job.salary, "Competitive")

    def test_applied_initial(self):
        """tests if the job is applied to initially"""
        job = JobListing(self.job_details)
        self.assertFalse(job.application_status)

    def test_status_after_applying(self):
        """tests if the job is applied to initially"""
        job = JobListing(self.job_details)
        job.apply()
        self.assertTrue(job.application_status)

    def test_dict_format(self):
        job = JobListing(self.job_details)
        return_data = self.job_details = {
            "id": 100,
            "url": "https://remotive.com/remote-jobs/",
            "title": "QA",
            "company_name" : "quantum",
            "company_logo" : "logo.png",
            "category" : "testing",
            "tags" : ["TDD", "CI/CD"],
            "job_type" : "remote",
            "publication_date" : datetime.fromisoformat("2025-10-24T14:51:03"),
            "candidate_required_location" : "-",
            "salary" : 1,
            "description" : "As a QA specializing in TDD."
        }
        self.assertEqual