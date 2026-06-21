from ..models.responses import NacResponse
from .base import BaseService


class Nac(BaseService):
    """
    NAC - Company Name Normalizer API.
    """

    def normalize_company_name(
        self,
        company: str,
    ) -> NacResponse:
        """
        Normalize a company name.

        Args:
            company: Company name to normalize

        Returns:
            NacResponse: Normalized company name
        """

        try:
            params = {"company": company}
            response = self.client.post("/nac", params)
            return NacResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "NAC Service")
