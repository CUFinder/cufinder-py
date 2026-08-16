from typing import Dict, Optional, Union

from ..models.responses import JcaResponse
from ..types import JcaParams
from .base import BaseService


class Jca(BaseService):
    """
    JCA - Job Changes API.
    """

    def get_job_changes(self, params: Union[JcaParams, Dict, None] = None) -> JcaResponse:
        """
        Get job changes within a date range.

        Args:
            params: JCA parameters object containing date range

        Returns:
            JcaResponse: Job changes information
        """

        try:
            if params is None:
                search_params = {}
            elif isinstance(params, dict):
                search_params = params
            else:
                search_params = params.to_dict()

            response = self.client.post("/jca", search_params)
            return JcaResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "JCA Service")