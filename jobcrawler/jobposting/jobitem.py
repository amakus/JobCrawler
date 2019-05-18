from dataclasses import dataclass
from collections import namedtuple


class JobItem:

    def __init__(self, title, url, details=None):
        self.title = title
        self.url = url
        self.details = details or JobDetails()

    def to_html(self, verbose=True):
        """Returns html table with job listing information. If verbose, full job description is included."""

        table_rows = self._html_table_row('title', self.title)
        for item in iter(self.details) if verbose else iter([]):
            if item.content:
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


@dataclass
class JobDetails:
    """Contains details to a job posting."""
    _detail_item = namedtuple('DetailItem', ['name', 'content'])
    _elements = ['category', 'department', 'overview', 'duties', 'skills', 'location']  # for ordered iteration

    category: str = ''
    department: str = ''
    overview: str = ''
    duties: str = ''
    skills: str = ''
    location: str = ''

    def __iter__(self):
        for elem in self._elements:
            yield self._detail_item(elem, vars(self)[elem])

    def has_entries(self):
        return any([entry.content for entry in self])



