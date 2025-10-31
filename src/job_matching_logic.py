from src.user_data_manager import DataManager
from src.nlp_processor import NlpProcessor
from src.api_request import ApiRequest
from src.config import REMOTIVE_API
from src.job_listing_manager import ListingManager
from src.job_listing import JobListing


def evaluate_job(job_details):
    """
    Function to evalueate a job's suitability
     - if suitable, True
     - else, False
    """
    match_salary = False
    match_skills = False

    data_manager = DataManager()
    preferences = data_manager.get_preferences()
    skills = preferences["user_skills"]
    min_salary = preferences["min_salary"]

    try:
        job_salary = float(job_details["salary"])
        if job_salary >= min_salary:
            match_salary = True
    except:
        match_salary = True

    nlp_processor = NlpProcessor(65)
    try:
        job_skills = job_details["tags"]
        comparison_score = nlp_processor.compare_keywords(job_skills, skills)
        if comparison_score >= 65:
            match_skills = True
    except:
        print("Given data does not have the details of a job !!!")
    return match_skills and match_salary

def search_and_match_jobs(num_jobs):
    """
    Function to search for number of jobs and match the suitable ones
    and save the matched jobs in csv file
    """
    caller = ApiRequest()
    api_data = caller.get_request(REMOTIVE_API, num_jobs)

    listing_manager = ListingManager()

    try:
        job_details = api_data["jobs"]

        for job_detail in job_details:
            if evaluate_job(job_detail):
                job = JobListing(job_detail)
                listing_manager.register_listing(job.to_dict())

        listing_manager.save_listings()

    except KeyError as e:
        print(e)
        print("API Response does not have job data!!!!!")
