import logging
import requests
import time
from typing import Optional, List
from jobcrawler.core.jobitem import JobItem, JobDetails
from jobcrawler.core.crawlers.crawler import Crawler
from jobcrawler.core.filter import SearchFilter
from jobcrawler.core.scrapers.airbusscraper import AirbusScraper

log = logging.getLogger('AirbusCrawler')


class AirbusCrawler(Crawler):
    """Crawler used for scraping Airbus.com job postings."""

    scraper = AirbusScraper
    _careers_url_head = ("https://www.airbus.com/" 
                         "careers/search-and-apply/search-for-vacancies.html?"
                         "&page=1&resultbypage=10000"  # all results on one page
                         "&filters=")

    def __init__(self, search_filter=None):
        # type: (Optional[SearchFilter]) -> None
        super(AirbusCrawler, self).__init__(search_filter)

    def get_jobs(self, details=False):
        pass

    def get_job_listings(self):
        """Retrieves all jobs from the listings page using search filters."""
        url = self._get_url()
        response = self._fetch_url_response(url)

        return self.scraper.scrape_jobs(response)

    def apply_job_details(self, job_items):
        # type: (List[JobItem]) -> List[JobItem]
        for job_item in job_items:
            try:
                response = self._fetch_url_response(job_item.url)
            except ValueError:
                log.warning(f'Could not retrieve job details for :{job_item.title}')
                job_item.details = JobDetails()
            else:
                job_item.details = self.scraper.scrape_job_details(response)

        return job_items

    def _get_url(self):
        """Returns a url for the get request with the search filters applied."""
        url = self._careers_url_head
        for kw in self.filter.keywords:
            filter_code = filter_map.get(kw.lower())
            if filter_code is None:
                continue
            url += f'%2C{filter_code}'

        return url

    def _fetch_url_response(self, url):
        """Makes get requests to given url and returns response. If unsuccessful, raises ValueError."""
        for fetch_attempt in range(self._retry_limit):
            response = requests.get(url)
            if response.ok:
                break
            else:
                time.sleep(self._retry_after)
        else:
            raise ValueError(f"Bad response from server for url: {url}")

        return response


filter_map = {

    # Functional area
    'engineering': 'filter_3_17',
    'finance': 'filter_3_37',
    'human resources': 'filter_3_43',
    'management': 'filter_3_52',
    'manufacturing': 'filter_3_56',
    'supply management': 'filter_3_83',

    # Germany
    'germany': 'filter_2_1054',
    'hamburg': 'filter_2_1054_2',
    'bremen': 'filter_2_1054_23',
    'manching': 'filter_2_1054_10',
    'munich': 'filter_2_1054_9',
    'berlin': 'filter_2_1054_46',
    'friedrichshafen': 'filter_2_1054_7',
    'langenhagen': 'filter_2_1054_70',
    'backnang': 'filter_2_1054_68',
    'potsdam': 'filter_2_1054_66',
    'frankfurt': 'filter_2_1054_64',
    'kassel': 'filter_2_1054_54',
    'varel': 'filter_2_1054_60',

    # France
    'france': 'filter_2_1072',
    'toulouse': 'filter_2_1072_6',
    'blagnac': 'filter_2_1072_3',
    'nantes': 'filter_2_1072_14',
    'marignane': 'filter_2_1072_12',
    'saint nazaire': 'filter_2_1072_8',
    'elancourt': 'filter_2_1072_1',

    # Division
    'airbus': 'filter_1_1',
    'airbus defense and space': 'filter_1_4',
    'airbus helicopters': 'filter_1_8',
    'subsidiaries': 'filter_1_9',

    # Experience
    'not specified': 'filter_4_1',
    'no work experience': 'filter_4_2',
    'mid-career': 'filter_4_3',
    'entry level': 'filter_4_5',
    'early career': 'filter_4_6',

}
