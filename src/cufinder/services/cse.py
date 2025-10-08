"""CSE - Company Search service."""

from typing import Optional

from ..models.responses import CseResponse
from .base import BaseService


class Cse(BaseService):
    """
    CSE - Company Search API (V2).
    
    Search for companies based on various criteria.
    """

    def search_companies(
        self,
        query: Optional[str] = None,
        industry: Optional[str] = None,
        location: Optional[str] = None,
        size: Optional[str] = None,
        page: Optional[int] = None,
    ) -> CseResponse:
        """
        Search companies.
        
        Args:
            query: Company name or description to search for
            industry: Industry to filter by
            location: Location to filter by
            size: Company size to filter by
            page: Page number for pagination
            
        Returns:
            CseResponse: Company search results
            
        Example:
            ```python
            companies = sdk.cse(query="tech startup", industry="software")
            print(f"Found {companies.total} companies")
            ```
        """
        try:
            search_params = {}

            # Add non-None parameters
            if query is not None:
                search_params["query"] = query
            if industry is not None:
                search_params["industry"] = industry
            if location is not None:
                search_params["location"] = location
            if size is not None:
                search_params["size"] = size
            if page is not None:
                search_params["page"] = page

            response_data = self.client.post("/cse", search_params)

            return CseResponse.from_dict(response_data)
        except Exception as error:
            raise self.handle_error(error, "CSE Service")
