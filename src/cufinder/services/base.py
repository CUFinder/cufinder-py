"""Base service class for all Cufinder API services."""

from ..client import CUFinderClient
from ..exceptions import CufinderError


class BaseService:
    """
    Base service class that provides common functionality for all services.
    
    Follows SOLID principles by providing a single responsibility base class.
    """

    def __init__(self, client: CUFinderClient):
        """
        Initialize the base service.
        
        Args:
            client: The CUFinderClient instance
        """
        self.client = client

    def handle_error(self, error: Exception, service_name: str) -> CufinderError:
        """
        Handle service errors consistently.
        
        Args:
            error: The error to handle
            service_name: The name of the service for error context
            
        Returns:
            CufinderError: Formatted error
        """
        if isinstance(error, CufinderError):
            return error

        # Handle other exceptions
        return CufinderError(
            f"{service_name}: {str(error)}",
            "UNKNOWN_ERROR",
            500,
        )


__all__ = ["BaseService"]