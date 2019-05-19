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

    @staticmethod
    def _iter_job_postings(soup):
        _job_div = ('div', {'class': 'c-jobcarousel__slider--title'})
        _job_div_a = 'a'

        for job_div in soup.find_all(*_job_div):
            div_a = job_div.find(_job_div_a)
            if div_a is not None:
                yield div_a

    @classmethod
    def scrape_job_details(cls, response):
        _details_description_div = ('h2', {'text': 'Description of the job'})

        soup = BeautifulSoup(response.text, 'html.parser')

        return JobDetails(category=cls._get_category(soup),
                          department=cls._get_department(soup),
                          summary=cls._get_summary(soup),
                          duties=cls._get_duties(soup),
                          skills=cls._get_skills(soup),
                          location=cls._get_location(soup))

    @classmethod
    def _get_category(cls, soup):
        return cls._get_target_by_parent_str(soup, 'span', 'span', 'Division')

    @classmethod
    def _get_department(cls, soup):
        return cls._get_target_by_parent_str(soup, 'span', 'span', 'Functional Area')

    @classmethod
    def _get_summary(cls, soup):
        return cls._get_target_by_parent_str(soup, 'div', 'h2', 'Description of the job')

    @classmethod
    def _get_duties(cls, soup):
        return cls._get_target_by_parent_str(soup, 'div', 'h2', 'Tasks & accountabilities')

    @classmethod
    def _get_skills(cls, soup):
        return cls._get_target_by_parent_str(soup, 'div', 'h2', 'Required skills')

    @classmethod
    def _get_location(cls, soup):
        return cls._get_target_by_parent_str(soup, 'span', 'span', 'Location')

    @staticmethod
    def _get_target_by_parent_str(soup, target_tag, parent_tag, parent_string):
        parent_tag = soup.find(parent_tag, string=parent_string)
        if parent_tag:
            target_tag = parent_tag.findNext(target_tag)
            return target_tag.text if target_tag else None
