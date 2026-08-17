from typing import Dict, Optional, Union

from ..models.responses import CsaResponse
from ..types import CsaParams
from .base import BaseService


class Csa(BaseService):
    """
    CSA - Company Signals API.
    """

    def get_company_signals(self, params: Union[CsaParams, Dict, None] = None) -> CsaResponse:
        """
        Get companies based on signals.

        Args:
            params: CSA parameters object containing signal criteria

        Returns:
            CsaResponse: Company signals information
        """

        try:
            if params is None:
                search_params = {}
            elif isinstance(params, dict):
                search_params = params
            else:
                search_params = params.to_dict()

            response = self.client.post("/csa", search_params)
            return CsaResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "CSA Service")