from typing import Dict, Optional, Union

from ..models.responses import CjaResponse
from ..types import CjaParams
from .base import BaseService


class Cja(BaseService):
    """
    CJA - Company Jobs API.
    """

    def search_company_jobs(self, params: Union[CjaParams, Dict, None] = None) -> CjaResponse:
        """
        Search for company jobs.

        Args:
            params: CJA parameters object containing search criteria

        Returns:
            CjaResponse: Company jobs information
        """

        try:
            if params is None:
                search_params = {}
            elif isinstance(params, dict):
                search_params = params
            else:
                search_params = params.to_dict()

            response = self.client.post("/cja", search_params)
            return CjaResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "CJA Service")
