from jobcrawler.crawlers.crawler import Crawler
from jobcrawler.crawlers.airbus_crawler import AirbusCrawler
import pytest


def test_instantiate_airbus_crawler():
    crawler = Crawler.from_domain('Airbus')
    assert isinstance(crawler, AirbusCrawler)


def test_instantiate_wrong_crawler():
    with pytest.raises(ValueError):
        Crawler.from_domain('meow')
