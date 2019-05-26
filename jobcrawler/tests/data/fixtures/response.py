import pytest
from jobcrawler.tests.data.fixtures import site_html_strings_airbus


class MockResponse:

    def __init__(self, ok=None, content=None, text=None, status_code=None, url=None):
        self.ok = ok
        self.content = content
        self.text = text
        self.status_code = status_code
        self.url = url


@pytest.fixture
def mock_response_job_listings_airbus():
    ok = True
    content = site_html_strings_airbus.job_listings_content
    text = site_html_strings_airbus.job_listings_text
    status_code = 200
    url = 'https://www.airbus.com/careers/search-and-apply/search-for-vacancies.html?filters=filter_3_17,filter_2_1054'

    return MockResponse(ok=ok, content=content, text=text, status_code=status_code, url=url)


@pytest.fixture
def mock_response_job_post_airbus():
    ok = True
    content = site_html_strings_airbus.job_post_content
    text = site_html_strings_airbus.job_post_text
    status_code = 200
    url = 'https://www.airbus.com/careers/search-and-apply/search-for-vacancies/job-detail.html?uuid=15094'

    return MockResponse(ok=ok, content=content, text=text, status_code=status_code, url=url)
