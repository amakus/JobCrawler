from typing import List, Optional

from jobcrawler.core.search.filter import SearchFilter
from jobcrawler.core.search.item import JobItem


class SearchResults:

    def __init__(self, domain, search_filter, new=None, removed=None):
        # type: (str, SearchFilter, Optional[List[JobItem]], Optional[List[JobItem]]) -> None
        self.domain = domain
        self.filter = search_filter
        self.new_jobs = new or []
        self.removed_jobs = removed or []

    def __bool__(self):
        return bool(self.new_jobs or self.removed_jobs)
