from collections import namedtuple
from datetime import datetime


class JobItem:

    def __init__(self, company, title, url, details=None):
        self._date = datetime.now()
        self.company = company
        self.title = title
        self.url = url
        self.details = details or JobDetails()

    def __str__(self):
        return self.to_html(details=True)

    @property
    def date(self):
        return self._date

    def to_html(self, details=True):
        """Returns html table with job listing information. If 'details' is True, full job description is included."""

        table_rows = self._html_table_row('title', self.title)
        for item in iter(self.details) if details else iter([]):
            if item.value:
                table_rows += self._html_table_row(*item)
        else:
            table_rows += self._html_table_row('url', self.url)

        return f"<table frame='box'><tbody>{table_rows}</tbody></table>"

    @staticmethod
    def _html_table_row(*col_items):
        """Get html table row from column items. First column is highlighted/bold."""
        _first_col_width = '20%'

        first_col = f"<td width={_first_col_width}><b>{col_items[0].capitalize()}</b></td>"
        cols = ""
        for item in col_items[1:]:
            cols += f"<td>{item}</td>"

        return f"<tr>{first_col + cols}</tr>"


class JobDetails:
    """Contains details to a job posting."""
    _detail_item = namedtuple('DetailItem', ['name', 'value'])
    _elements = ['category', 'department', 'summary', 'duties', 'skills', 'location']  # for ordered iteration

    def __init__(self, category=None, department=None, summary=None, duties=None, skills=None, location=None):
        # if no detail provided, empty string
        self.category = category or ''
        self.department = department or ''
        self.summary = summary or ''
        self.duties = duties or ''
        self.skills = skills or ''
        self.location = location or ''

    def __iter__(self):
        for elem in self._elements:
            yield self._detail_item(elem, vars(self)[elem])

    def has_entries(self):
        return any([entry.value for entry in self])



