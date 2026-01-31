from ..models.responses import CbcResponse
from .base import BaseService


class Cbc(BaseService):
    """
    CBC - Company B2B or B2C Checker API (V2)
    
    Get company business type
    """

    def get_company_business_type(self, url: str) -> CbcResponse:
        """
        Args:
            url: The company domain you want to check is saas or not
            
        Returns:
            CbcResponse: yes or no
            
        Example:
            ```python
            result = client.cbc("stripe.com")
            print(result)
            ```
        """
        try:
            response = self.client.post("/cbc", {
                "url": url.strip(),
            })

            return CbcResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "CBC Service")
