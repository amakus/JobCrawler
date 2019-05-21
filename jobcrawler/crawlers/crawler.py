from typing import List, Optional
from enum import Enum
from dataclasses import dataclass


class CrawlerFactory:

    @classmethod
    def get_crawler(cls, domain):
        pass


class Crawler:
    """Abstract class for specific crawlers."""

    def __init__(self, filter=None):
        # type: (Optional[SearchFilter]) -> None
        self.filter = filter


@dataclass
class SearchFilter:
    """Data class to store the search filters for the domain request sent by the crawler, eg. locations."""
    include: List[str]
    exclude: List[str]


class Domain(Enum):
    """Enum class for crawler class factory."""
    AIRBUS = 'airbus'
