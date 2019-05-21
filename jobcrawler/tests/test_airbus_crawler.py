import pytest
from jobcrawler.crawlers.airbuscrawler import AirbusCrawler, AirbusFilter
from jobcrawler.crawlers.crawler import Crawler
from jobcrawler.jobposting.jobitem import JobItem


def test_instantiate():
    crawler = AirbusCrawler()
    assert isinstance(crawler, AirbusCrawler)
    assert isinstance(crawler, Crawler)


def test_get_url():
    filtr = AirbusFilter(location=['hamburg', 'bremen'])
    crawler = AirbusCrawler(filtr)

    url = crawler._get_url()
    assert url == ("https://www.airbus.com/careers/search-and-apply/search-for-vacancies.html?filters",
                   "filter_2_1054_2&filter_2_1054_23",
                   "&page=1&resultbypage=10000")


def test_get_jobs(details=False):
    crawler = AirbusCrawler()
    jobs = crawler.get_jobs()
    assert all([isinstance(job, JobItem) for job in jobs])


def test_get_job_details():
    crawler = AirbusCrawler()
    job_items = crawler.get_jobs()
    crawler.apply_job_details(job_items)


def test_airbus_filter():
    pass

