import pytest
from jobcrawler.core.crawlers.factory import CrawlerFactory
from jobcrawler.core.crawlers.airbuscrawler import AirbusCrawler


def test_crawler_factory_airbus():
    assert CrawlerFactory.get_crawler('Airbus') is AirbusCrawler
    assert CrawlerFactory.get_crawler('airbus') is AirbusCrawler
    assert CrawlerFactory.get_crawler('AIRBUS') is AirbusCrawler
    with pytest.raises(ValueError):
        CrawlerFactory.get_crawler('non-existent')
