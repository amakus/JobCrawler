from jobcrawler.core.search.filter import SearchFilter
from jobcrawler.core.search.results import SearchResults
from jobcrawler.core.email.content import HtmlContent

pytest_plugins = ['jobcrawler/tests/data/fixtures/job_items']


def test_email_html(fake_job_items):
    jobs = fake_job_items
    res = SearchResults('Airbus', SearchFilter(), new=jobs, removed=[jobs[0]])

    content = HtmlContent([res])

    with open('test_file.html', 'w') as file:
        file.write(content.to_string())
