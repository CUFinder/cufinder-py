"""DTC - Domain to Company Name service."""

from urllib.parse import urlparse

from ..models.responses import DtcResponse
from .base import BaseService


class Dtc(BaseService):
    """
    DTC - Domain to Company Name API (V2).
    
    Retrieves the registered company name associated with a given website domain.
    """

    def get_company_name(self, company_website: str) -> DtcResponse:
        """
        Get company name from domain.
        
        Args:
            company_website: The website URL to lookup
            
        Returns:
            DtcResponse: Company name information
            
        Example:
            ```python
            company = sdk.dtc("https://example.com")
            print(company.company_name)  # 'Example Corp'
            ```
        """
        self.validate_required(company_website, "company_website")

        # Basic URL validation
        try:
            parsed_url = urlparse(company_website.strip())
            if not parsed_url.scheme or not parsed_url.netloc:
                raise ValueError("Invalid website URL format")
        except Exception:
            raise ValueError("Invalid website URL format")

        try:
            response_data = self.client.post("/dtc", {
                "company_website": company_website.strip(),
            })

            return DtcResponse.from_dict(response_data)
        except Exception as error:
            raise self.handle_error(error, "DTC Service")
