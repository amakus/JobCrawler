import requests
from bs4 import BeautifulSoup
from jobcrawler.scrapers.scraper import Scraper
from jobcrawler.jobposting.jobitem import JobItem, JobDetails


class AirbusScraper(Scraper):
    """Scraper objects for Airbus html content."""

    @classmethod
    def scrape_jobs(cls, response):
        jobs = []
        soup = BeautifulSoup(response.text, 'html.parser')
        for job_posting in cls._iter_job_postings(soup):
            title, url = job_posting.text, job_posting['href']
            jobs.append(JobItem(title, url))

        return jobs

    @classmethod
    def scrape_job_details(cls, response):
        _details_description_div = ('h2', {'text': 'Description of the job'})

        soup = BeautifulSoup(response.text, 'html.parser')
        return JobDetails()

    @classmethod
    def _iter_job_postings(cls, soup):
        _job_div = ('div', {'class': 'c-jobcarousel__slider--title'})
        _job_div_a = 'a'

        for job_div in soup.find_all(*_job_div):
            div_a = job_div.find(_job_div_a)
            if div_a is not None:
                yield div_a
