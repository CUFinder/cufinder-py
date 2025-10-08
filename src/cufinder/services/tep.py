"""TEP - Person Enrichment service."""

from ..models.responses import TepResponse
from .base import BaseService


class Tep(BaseService):
    """
    TEP - Person Enrichment API (V2).
    
    Enriches person information from various data sources.
    """

    def enrich_person(self, query: str) -> TepResponse:
        """
        Enrich person information.
        
        Args:
            query: Person name, email, or other identifier to enrich
            
        Returns:
            TepResponse: Enriched person information
            
        Example:
            ```python
            person = sdk.tep("John Doe")
            print(person.person.full_name)  # 'John Doe'
            print(person.person.job_title)  # 'Software Engineer'
            ```
        """

        try:
            response_data = self.client.post("/tep", {
                "query": query.strip(),
            })

            return TepResponse.from_dict(response_data)
        except Exception as error:
            raise self.handle_error(error, "TEP Service")
