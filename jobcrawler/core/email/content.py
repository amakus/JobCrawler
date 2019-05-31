from typing import List
from jobcrawler.core.search.results import SearchResults


class HtmlContent:

    _table_width = 80  # percent
    _table_bottom_margin = 10  # px
    _cell_padding = 5  # px
    _p_tag_margin = 2  # em

    def __init__(self, search_results, details=True):
        # type: (List[SearchResults]) -> None
        self._search_results = sorted(search_results, key=lambda x: x.domain)
        self._details=details
        self._html_str = self._make_html_str()

    def __str__(self):
        return self._html_str

    def to_string(self):
        return str(self)

    def _make_html_str(self):
        return (f"<html>"
                f"  <head>"
                f"    <style>{self._table_css}{self._cell_css}{self._p_css}</style>"
                f"  </head>"
                f"  <body>"
                f"    {self._domain_results}"
                f"  </body>"
                f"</html>")

    @property
    def _table_css(self):
        return (f"table {{"
                f"  font-family: arial, sans-serif;"
                f"  border-collapse: collapse;"
                f"  width: {self._table_width}%;"
                f"  margin-bottom: {self._table_bottom_margin}px;"
                f"}}")

    @property
    def _cell_css(self):
        return (f"td, th {{"
                f"  text-align: left;"
                f"  vertical-align:top;"
                f"  padding: {self._cell_padding}px;"
                f"}}")

    @property
    def _p_css(self):
        return (f"p {{"
                f"  display: block;"
                f"  margin-top: {self._p_tag_margin}em;"
                f"  margin-bottom: {self._p_tag_margin}em;"
                f"}}")

    @property
    def _domain_results(self):
        html = ''
        for result in self._search_results:
            if not result:
                continue

            html += f'<h2><u>{result.domain.capitalize()}</u></h2>'

            if result.new_jobs:
                html += (f'<h3>New Job Postings ({len(result.new_jobs)}):</h3>'
                         f'{"".join([job.to_html(self._details) for job in result.new_jobs])}')

            if result.removed_jobs:
                html += (f'<h3>Removed Job Postings ({len(result.removed_jobs)}):</h3>'
                         f'{"".join([job.to_html(self._details) for job in result.removed_jobs])}')

        return html
