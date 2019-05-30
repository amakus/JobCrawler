import pytest
from jobcrawler.core.crawlers.airbuscrawler import AirbusCrawler
from jobcrawler.core.crawlers.abstract import Crawler
from jobcrawler.core.search.filter import SearchFilter
from jobcrawler.core.search.item import JobItem, JobDetails


def test_instantiate():
    crawler = AirbusCrawler()
    assert isinstance(crawler, AirbusCrawler)
    assert isinstance(crawler, Crawler)


def test_get_url():
    filtr = SearchFilter(keywords=['Engineering', 'Hamburg', 'Bremen'])
    crawler = AirbusCrawler(filtr)

    url = crawler._get_url()
    assert url == ("https://www.airbus.com/"
                   "careers/search-and-apply/search-for-vacancies.html?"
                   "&page=1&resultbypage=10000"   # all results on one page
                   "&filters="
                   "%2Cfilter_3_17"
                   "%2Cfilter_2_1054_2"
                   "%2Cfilter_2_1054_23"
                   )


def test_get_url_non_existent_keyword():
    filtr = SearchFilter(keywords=['Meow', 'Hamburg', 'Bremen'])
    crawler = AirbusCrawler(filtr)

    url = crawler._get_url()
    assert url == ("https://www.airbus.com/"
                   "careers/search-and-apply/search-for-vacancies.html?"
                   "&page=1&resultbypage=10000"  # all results on one page
                   "&filters="
                   "%2Cfilter_2_1054_2"
                   "%2Cfilter_2_1054_23"
                   )


@pytest.mark.skip('live request')
def test_get_jobs():
    filtr = SearchFilter(keywords=['Hamburg', 'Engineering'])
    crawler = AirbusCrawler(filtr)
    jobs = crawler.get_job_listings()

    assert len(jobs) > 0
    assert all([isinstance(job, JobItem) for job in jobs])


@pytest.mark.skip('live request')
def test_get_jobs_zero_results():
    filtr = SearchFilter(keywords=['Hamburg', 'Supply Management'])
    crawler = AirbusCrawler(filtr)
    jobs = crawler.get_job_listings()

    assert len(jobs) == 0


@pytest.mark.skip('live request')
def test_get_job_details():
    filtr = SearchFilter(keywords=['Hamburg', 'Engineering'])
    crawler = AirbusCrawler(filtr)
    jobs = crawler.get_job_listings()
    crawler.apply_job_details(jobs)

    for job in jobs:
        assert isinstance(job.details, JobDetails)
        assert any([d for d in job.details])
