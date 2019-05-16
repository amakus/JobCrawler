""" This is the main module of the JobCrawler package."""

from typing import List, Optional
from enum import Enum
import logging

log = logging.getLogger('MainModule')


class Crawler:
    """Abstract class for specific crawlers."""

    def __init__(self, ignore_kw=None, include_kw=None):
        # type: (Optional[List], Optional[List]) -> None
        self._ignore_kw = ignore_kw
        self._include_kw = include_kw

    @classmethod
    def from_domain(cls, domain, ignore_kw=None, include_kw=None):
        # type: (str, Optional[List], Optional[List]) -> Optional[Crawler]
        try:
            dom = Domain(domain.lower())
        except ValueError:
            return

        if dom is Domain.AIRBUS:
            return AirbusCrawler(ignore_kw, include_kw)


class AirbusCrawler(Crawler):
    """Crawler used for scraping Airbus.com job postings."""

    _ = "www.airbus.com"

    def __init__(self, ignore_kw, include_kw):
        super(AirbusCrawler, self).__init__(ignore_kw, include_kw)


class Domain(Enum):
    AIRBUS = 'airbus'