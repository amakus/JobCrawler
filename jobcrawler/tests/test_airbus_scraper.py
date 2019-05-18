from jobcrawler.jobposting.jobitem import JobItem, JobDetails
from jobcrawler.scrapers.airbusscraper import AirbusScraper

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

    assert details.category == 'Vehicle Mission & Control'
    assert details.location == 'Manching, Germany'

