from ..models.responses import CefResponse
from .base import BaseService


class Cef(BaseService):
    """
    CEF - Company Employee Finder API.
    """

    def find_company_employees(
        self,
        query: str,
        page: int = None,
    ) -> CefResponse:
        """
        Returns a list of employees for a given company.

        Args:
            query: Company name to find employees for
            page: Page number for pagination

        Returns:
            CefResponse: Company employee information
        """

        try:
            params = {"query": query}
            if page is not None:
                params["page"] = page

            response = self.client.post("/cef", params)

            return CefResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "CEF Service")
