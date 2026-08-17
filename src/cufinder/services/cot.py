from ..models.responses import CotResponse
from .base import BaseService


class Cot(BaseService):
    """
    COT - Offers Free Trial Checker API.
    """

    def offers_free_trial(self, url: str) -> CotResponse:
        """
        Check if a company offers a free trial.

        Args:
            url: Company website URL

        Returns:
            CotResponse: Whether the company offers a free trial
        """

        try:
            response = self.client.post("/cot", {
                "url": url,
            })

            return CotResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "COT Service")