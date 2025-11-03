"""
File with class representing Job Listing
for easy storage in files and dashboard
display

author: Sham Ganesh Thamarai Kannan
for: FIT2107 D2
"""
from datetime import datetime
from bs4 import BeautifulSoup

class JobListing:
    """
    class that represents a job listings and processes
    the job details returned by the API to store them
    in the correct info format
    """
    def __init__(self, job_data):
        """
        constructor function to create a job object/instance
        """

        self.id = int(job_data["id"])
        self.url = job_data["url"]
        self.title = job_data["title"]
        self.company_name = job_data["company_name"]
        self.company_logo =  job_data["company_logo"]
        self.category = job_data["category"]
        self.req_skills = job_data["tags"]
        self.job_type = job_data["job_type"]

        try:
            self.publication_date = datetime.fromisoformat(
                job_data["publication_date"]
            )
        except ValueError:
            self.publication_date = job_data["publication_date"]
        except TypeError:
            self.publication_date = job_data["publication_date"]

        self.location = job_data["candidate_required_location"]

        try:
            self.salary = float(job_data["salary"])
        except ValueError:
            self.salary = job_data["salary"]

        try:
            self.description = BeautifulSoup(job_data["description"],"html.parser").get_text()
        except:
            self.desciption = job_data["description"]

        self.application_status = False

    def apply(self):
        """function to apply to the job listing"""
        self.application_status = True

    def to_dict(self):
        """converts the processed data into dictionary
        for storage and processing"""

        tags = ", ".join(self.req_skills)
        dict_data = {
            "id": self.id,
            "url": self.url,
            "title": self.title,
            "company_name": self.company_name,
            "company_logo": self.company_logo,
            "category": self.category,
            "tags": tags,
            "job_type": self.job_type,
            "publication_date": self.publication_date,
            "candidate_required_location": self.location,
            "salary": self.salary,
            "description": self.description,
            "application_status": self.application_status
        }
        return dict_data
