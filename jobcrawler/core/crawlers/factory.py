from jobcrawler.core.crawlers.airbuscrawler import AirbusCrawler
from jobcrawler.core.search.domain import Domain


class CrawlerFactory:

    @classmethod
    def get_crawler(cls, company):
        domain = Domain(str(company).capitalize())

        if domain is Domain.AIRBUS:
            return AirbusCrawler

        raise ValueError(f'{company} not an implemented company')