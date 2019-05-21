import pytest
from jobcrawler.crawlers.airbuscrawler import AirbusCrawler
from jobcrawler.crawlers.crawler import Crawler
from jobcrawler.jobposting.jobitem import JobItem


def test_instantiate():
    crawler = AirbusCrawler()
    assert isinstance(crawler, AirbusCrawler)
    assert isinstance(crawler, Crawler)


def test_get_url():
    pass





def test_get_jobs(details=False):
    crawler = AirbusCrawler()
    jobs = crawler.get_jobs()
    assert all([isinstance(job, JobItem) for job in jobs])


def test_get_job_details():
    crawler = AirbusCrawler()
    job_items = crawler.get_jobs()
    crawler.apply_job_details(job_items)

