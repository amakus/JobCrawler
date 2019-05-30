import pytest
from jobcrawler.core.search.item import JobItem, JobDetails
from jobcrawler.util.lorem_ipsum import bacon


@pytest.fixture
def fake_job_items():
    return [
        JobItem(
            company='Fake Inc.',
            title="Position at fake department doing fake work.",
            url="www.fakeurl.com",
            details=JobDetails(category='Cool job',
                               department='Fake department',
                               summary=bacon[0],
                               duties=bacon[1],
                               skills='Word, Excel, Common sense',
                               location='Hamburg, Germany')
        ),
        JobItem(
            company='Fake Doors Ltd.',
            title="Intern to make coffee and other things nobody likes to do",
            url="www.fake-doors.com",
            details=JobDetails(category='Fake doors',
                               department='Marketing and Sales',
                               summary=bacon[3],
                               duties=bacon[4],
                               skills='You must be passionate about fake doors.',
                               location='C137, Earth')
        ),
        JobItem(
            company='Dream Factory Inc',
            title="Title description that says nothing",
            url="www.wow-our-jobs-are-so-cool-check-it-out.com",
            details=JobDetails(category='Dream Factory Inc',
                               location='Beijing, CHina')
        )
    ]




