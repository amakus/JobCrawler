

class Scraper:
    """Abstract class for html content scrapers."""

    def scrape_jobs(self, response):
        """Scrapes a response object and returns job items."""
        raise NotImplementedError

    @classmethod
    def scrape_job_details(cls, response):
        """Scrapes a responise object and returns job details."""
        raise NotImplementedError
