from ..models.responses import CcpResponse
from .base import BaseService


class Ccp(BaseService):
    """
    CCP - Company Career Page Finder API (V2)
    
    Find companies careers page
    """

    def find_careers_page(self, url: str) -> CcpResponse:
        """
        Args:
            url: The company domain you want to find it's career page
            
        Returns:
            CcpResponse: Company careers page
            
        Example:
            ```python
            result = client.ccp("stripe.com")
            print(result)
            ```
        """
        try:
            response = self.client.post("/ccp", {
                "url": url.strip(),
            })

            return CcpResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "CCP Service")
