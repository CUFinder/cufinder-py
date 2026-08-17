from typing import Dict, Optional, Union

from ..models.responses import ClfResponse
from ..types import ClfParams
from .base import BaseService


class Clf(BaseService):
    """
    CLF - Contact Lookalikes API.
    """

    def find_contact_lookalikes(self, params: Union[ClfParams, Dict, None] = None) -> ClfResponse:
        """
        Find similar contacts based on a query.

        Args:
            params: CLF parameters object containing the query

        Returns:
            ClfResponse: Contact lookalikes information
        """

        try:
            if params is None:
                search_params = {}
            elif isinstance(params, dict):
                search_params = params
            else:
                search_params = params.to_dict()

            response = self.client.post("/clf", search_params)
            return ClfResponse.from_dict(self.parse_response_data(response))
        except Exception as error:
            raise self.handle_error(error, "CLF Service")