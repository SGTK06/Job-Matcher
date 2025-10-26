"""
File with class representing Job Listing
for easy storage in files and dashboard
display

author: Sham Ganesh Thamarai Kannan
for: FIT2107 D2
"""
from datetime import datetime

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
            self.description = job_data["description"].split(r"</p>")[0].strip(r"<p>")
        except TypeError:
            self.desciption = job_data["description"]

        self.application_status = False
