from typing import Optional, List
from dataclasses import dataclass
from jobcrawler.crawlers.crawler import Crawler, SearchFilter


class AirbusCrawler(Crawler):
    """Crawler used for scraping Airbus.com job postings."""

    _careers_url = "https://www.airbus.com/careers/search-and-apply/search-for-vacancies.html?"
    _url_tail = '&page=1&resultbypage=10000'  # all results on one page

    def __init__(self, filter=None):
        # type: (Optional[SearchFilter]) -> None
        super(AirbusCrawler, self).__init__(filter)

    def get_jobs(self):
        pass

    def apply_job_details(self, job_items):
        pass

    def _get_job_listings(self):
        pass

    def _get_url(self):
        pass


@dataclass
class AirbusFilter(SearchFilter):
    contract_type: List[str]
    country: List[str]
    division: List[str]
    functional_area: List[str]
    work_experience: List[str]


filter_map = {
    # country
    'germany': 'filter_2_1054',

    # city
    'hamburg': '2Cfilter_2_1054_2',
    'bremen': '2Cfilter_2_1054_23',
    'manching': '2Cfilter_2_1054_10',
    'munich': '2Cfilter_2_1054_9',
    'friedrichshafen': '2Cfilter_2_1054_7',

    # functional area
    'engineering': 'filter_3_17'
}