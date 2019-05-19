from typing import Optional
from jobcrawler.crawlers.crawler import Crawler, SearchFilter


class AirbusCrawler(Crawler):
    """Crawler used for scraping Airbus.com job postings."""

    _web_domain = "www.airbus.com"

    def __init__(self, settings=None):
        # type: (Optional[SearchFilter]) -> None
        super(AirbusCrawler, self).__init__(settings)

    def get_jobs(self):
        pass

    def apply_job_details(self, job_items):
        pass

    def _get_job_listings(self):
        pass

    def _get_url(self):
        _url_tail = '&page=1&resultbypage=20'


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