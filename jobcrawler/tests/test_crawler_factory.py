from jobcrawler.crawlers.crawler import CrawlerFactory
from jobcrawler.crawlers.airbuscrawler import AirbusCrawler
import pytest


def test_crawler_factory_airbus():
    isinstance(CrawlerFactory.get_crawler('Airbus'), AirbusCrawler)
    isinstance(CrawlerFactory.get_crawler('airbus'), AirbusCrawler)
    with pytest.raises(ValueError):
        CrawlerFactory.get_crawler('non-existent')
