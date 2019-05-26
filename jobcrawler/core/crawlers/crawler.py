from typing import Optional
from jobcrawler.core.filter import SearchFilter


class CrawlerFactory:

    @classmethod
    def get_crawler(cls, domain):
        pass


class Crawler:
    """Abstract class for specific crawlers."""

    _retry_after = 30  # seconds
    _retry_limit = 5  # amount of failed calls

    def __init__(self, search_filter=None):
        # type: (Optional[SearchFilter]) -> None
        self.filter = search_filter

    def get_job_listings(self):
        raise NotImplementedError

    def _apply_include_filter(self, job_items):
        """Returns jobs that include any of the keywords in job title or details."""
        pass

    def _apply_exclude_filter(self, job_items):
        """Returns jobs that do not include any of the keywords in job title or details."""
        pass
