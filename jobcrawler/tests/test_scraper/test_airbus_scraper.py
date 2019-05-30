import pytest
import requests
from jobcrawler.core.search.item import JobItem, JobDetails
from jobcrawler.core.scrapers.airbusscraper import AirbusScraper

pytest_plugins = ['jobcrawler/tests/data/fixtures/response']


def test_scrape(mock_response_job_listings_airbus):
    resp = mock_response_job_listings_airbus
    jobs = AirbusScraper.scrape_jobs(resp)
    first, last = jobs[0], jobs[-1]

    assert len(jobs) == 20
    assert all([isinstance(job, JobItem) for job in jobs])
    assert not any([job.details.has_entries() for job in jobs])

    assert first.title == 'Systems Engineer Human Factors Engineering (d/f/m)'
    assert first.url == 'https://www.airbus.com/careers/search-and-apply/search-for-vacancies/job-detail.html?uuid=15183'

    assert last.title == 'Systems Engineer (d/f/m)- Ground Mission Systems'
    assert last.url == 'https://www.airbus.com/careers/search-and-apply/search-for-vacancies/job-detail.html?uuid=15094'


def test_scrape_details(mock_response_job_post_airbus):
    resp = mock_response_job_post_airbus

    details = AirbusScraper.scrape_job_details(resp)  # type: JobDetails

    assert details.category == 'Airbus Defence and Space'
    assert details.department == 'Vehicle Mission & Control'
    assert details.summary[:50] == 'A vacancy for a Systems Engineer (d/f/m)- Ground M'
    assert details.duties[:50] == 'If you are looking for a challenging task in a dev'
    assert details.skills[:50] == 'We are looking for candidates with the following s'
    assert details.location == 'Manching, Germany'


@pytest.mark.skip('live request')
def test_scrape_airbus():
    url = ("https://www.airbus.com/careers/search-and-apply/search-for-vacancies.html?resultbypage=10000"
           "&filters="
           "filter_2_1054"  # Germany
           "%2Cfilter_2_1054_2"  # Hamburg
           "%2Cfilter_2_1054_23"  # Bremen
           )
    response = requests.get(url)
    jobs = AirbusScraper.scrape_jobs(response)

    assert len(jobs) == 73
