from ..models.responses import NauResponse
from .base import BaseService


class Nau(BaseService):
    """
    NAU - URL Normalizer API.
    """

    def normalize_url(self, url: str) -> NauResponse:
        """
        Normalize a URL.

        Args:
            url: URL to normalize

        Returns:
            NauResponse: Normalized URL
        """

        try:
            response = self.client.post("/nau", {
                "url": url,
            })

            return NauResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "NAU Service")