from jobcrawler.crawlers.crawler import Crawler


class AirbusCrawler(Crawler):
    """Crawler used for scraping Airbus.com job postings."""

    _web_domain = "www.airbus.com"

    def __init__(self, settings=None):
        super(AirbusCrawler, self).__init__(settings)


