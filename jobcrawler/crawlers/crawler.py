from typing import List, Optional
from enum import Enum
from dataclasses import dataclass, field


class CrawlerFactory:

    @classmethod
    def get_crawler(cls, domain):
        pass


class Crawler:
    """Abstract class for specific crawlers."""

    def __init__(self, search_filter=None):
        # type: (Optional[SearchFilter]) -> None
        self.filter = search_filter


@dataclass
class SearchFilter:
    """Class for storing search filters for the domain request sent by the crawler, eg. locations."""
    include: List[str] = field(default_factory=list)
    exclude: List[str] = field(default_factory=list)


class Domain(Enum):
    """Enum class for crawler class factory."""
    AIRBUS = 'airbus'
