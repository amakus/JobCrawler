import pytest
import responses
from jobcrawler.crawlers.airbuscrawler import AirbusCrawler
from jobcrawler.crawlers.crawler import Crawler
from jobcrawler.jobposting.jobitem import JobItem


def test_instantiate():
    crawler = AirbusCrawler()
    assert isinstance(crawler, AirbusCrawler)
    assert isinstance(crawler, Crawler)


def test_call_urls():
    crawler = AirbusCrawler()
    pass

@pytest.mark.skip('live request')
def test_site_response():
    pass


def test_scrape_jobs():
    crawler = AirbusCrawler()
    raw_data = crawler.scrape_data()


def test_parse_data(airbus_dummy_data):
    crawler = AirbusCrawler()
    data = airbus_dummy_data
    jobs = crawler.parse_data(data)


def test_get_jobs():
    crawler = AirbusCrawler()
    jobs = crawler.get_jobs()
    assert all([isinstance(job, JobItem) for job in jobs])