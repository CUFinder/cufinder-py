"""PSE - People Search service."""

from typing import Optional

from ..models.responses import PseResponse
from .base import BaseService


class Pse(BaseService):
    """
    PSE - People Search API (V2).
    
    Search for people based on various criteria.
    """

    def search_people(
        self,
        query: Optional[str] = None,
        job_title: Optional[str] = None,
        company: Optional[str] = None,
        location: Optional[str] = None,
        page: Optional[int] = None,
    ) -> PseResponse:
        """
        Search people.
        
        Args:
            query: Person name or description to search for
            job_title: Job title to filter by
            company: Company to filter by
            location: Location to filter by
            page: Page number for pagination
            
        Returns:
            PseResponse: People search results
            
        Example:
            ```python
            people = sdk.pse(query="software engineer", company="TechCorp")
            print(f"Found {people.total} people")
            ```
        """
        try:
            search_params = {}

            # Add non-None parameters
            if query is not None:
                search_params["query"] = query
            if job_title is not None:
                search_params["job_title"] = job_title
            if company is not None:
                search_params["company"] = company
            if location is not None:
                search_params["location"] = location
            if page is not None:
                search_params["page"] = page

            response_data = self.client.post("/pse", search_params)

            return PseResponse.from_dict(response_data)
        except Exception as error:
            raise self.handle_error(error, "PSE Service")
