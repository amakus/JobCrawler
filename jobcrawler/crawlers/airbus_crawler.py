from jobcrawler.crawlers.crawler import Crawler


class AirbusCrawler(Crawler):
    """Crawler used for scraping Airbus.com job postings."""

    _ = "www.airbus.com"

    def __init__(self, ignore_kw, include_kw):
        super(AirbusCrawler, self).__init__(ignore_kw, include_kw)

