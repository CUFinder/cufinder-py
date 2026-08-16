from typing import Dict, Optional, Union

from ..models.responses import PsaResponse
from ..types import PsaParams
from .base import BaseService


class Psa(BaseService):
    """
    PSA - Contact Signals API.
    """

    def get_contact_signals(self, params: Union[PsaParams, Dict, None] = None) -> PsaResponse:
        """
        Get contacts based on company signals.

        Args:
            params: PSA parameters object containing signal criteria

        Returns:
            PsaResponse: Contact signals information
        """

        try:
            if params is None:
                search_params = {}
            elif isinstance(params, dict):
                search_params = params
            else:
                search_params = params.to_dict()

            response = self.client.post("/psa", search_params)
            return PsaResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "PSA Service")