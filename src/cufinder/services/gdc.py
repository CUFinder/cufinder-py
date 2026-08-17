from ..models.responses import GdcResponse
from .base import BaseService


class Gdc(BaseService):
    """
    GDC - Gives Demo Checker API.
    """

    def gives_demo(self, url: str) -> GdcResponse:
        """
        Check if a company offers demos.

        Args:
            url: Company website URL

        Returns:
            GdcResponse: Whether the company gives demos
        """

        try:
            response = self.client.post("/gdc", {
                "url": url,
            })

            return GdcResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "GDC Service")