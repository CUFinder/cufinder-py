from ..models.responses import CsnResponse
from .base import BaseService


class Csn(BaseService):
    """
    CSN - Company Snapshot API (V2)
    
    Get company snapshot info
    """

    def get_company_snapshot(self, url: str) -> CsnResponse:
        """
        Args:
            url: The company domain you want to check
            
        Returns:
            CsnResponse: Company mission statement
            
        Example:
            ```python
            result = client.csc("stripe.com")
            print(result)
            ```
        """
        try:
            response = self.client.post("/csn", {
                "url": url.strip(),
            })

            return CsnResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "CSN Service")
