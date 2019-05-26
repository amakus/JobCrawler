from dataclasses import dataclass, field
from typing import List


@dataclass
class SearchFilter:
    """Class for storing search filters for the domain request sent by the crawler, eg. locations."""
    keywords: List[str] = field(default_factory=list)
    include: List[str] = field(default_factory=list)
    exclude: List[str] = field(default_factory=list)
