from ..models.responses import NapResponse
from .base import BaseService


class Nap(BaseService):
    """
    NAP - Person Name Normalizer API.
    """

    def normalize_person_name(self, person_name: str) -> NapResponse:
        """
        Normalize a person name.

        Args:
            person_name: Person name to normalize

        Returns:
            NapResponse: Normalized person name
        """

        try:
            response = self.client.post("/nap", {
                "person_name": person_name,
            })

            return NapResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "NAP Service")