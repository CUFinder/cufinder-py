from ..models.responses import CaaResponse
from .base import BaseService


class Caa(BaseService):
    """
    CAA - Company Activity API.
    """

    def get_company_activities(
        self,
        query: str,
        page: int = None,
    ) -> CaaResponse:
        """
        Get company activities.

        Args:
            query: Company name to get activities for
            page: Page number for pagination

        Returns:
            CaaResponse: Company activities information
        """

        try:
            params = {"query": query}
            if page is not None:
                params["page"] = page

            response = self.client.post("/caa", params)
            return CaaResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "CAA Service")
