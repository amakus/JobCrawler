from jobcrawler.jobposting.jobitem import JobItem
from jobcrawler.jobposting.jobitem import JobDescription


def test_job_item_instantiation():
    item = JobItem('title', 'url')
    assert isinstance(item, JobItem)


def test_job_item_properties():
    title = 'title'
    description = JobDescription()
    url = 'www.test.com'
    item = JobItem(title, url, description)

    assert item.title == title
    assert item.url == url
    assert isinstance(item.description, JobDescription)


def test_job_hash():
    pass


def test_job_description_instantiation():
    assert isinstance(JobDescription(), JobDescription)


def test_job_description_properties():
    category = 'cat'
    department = 'dep'
    overview = 'overview'
    duties = 'duties'
    skills = 'skills'
    location = 'loc'
    descr = JobDescription(category, department, overview, duties, skills, location)

    assert descr.category == category
    assert descr.department == department
    assert descr.overview == overview
    assert descr.duties == duties
    assert descr.skills == skills
    assert descr.location == location


def test_to_html_non_verbose():
    title = 'title'
    url = 'www.test.com'
    description = JobDescription('cat', '', '', '', '', 'loc')
    item = JobItem(title, url, description)

    expected_verbose = ("<table frame='box'>"
                        "<tbody>"
                        "<tr><td width=20%><b>Title</b></td><td>title</td></tr>"
                        "<tr><td width=20%><b>Category</b></td><td>cat</td></tr>"
                        "<tr><td width=20%><b>Location</b></td><td>loc</td></tr>"
                        "<tr><td width=20%><b>Url</b></td><td>www.test.com</td></tr>"
                        "</tbody>"
                        "</table>")
    expected_non_verbose = ("<table frame='box'>"
                            "<tbody>"
                            "<tr><td width=20%><b>Title</b></td><td>title</td></tr>"
                            "<tr><td width=20%><b>Url</b></td><td>www.test.com</td></tr>"
                            "</tbody>"
                            "</table>")

    assert item.to_html(verbose=True) == expected_verbose
    assert item.to_html(verbose=False) == expected_non_verbose
