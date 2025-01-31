class APIKeyMissingOrInvalidError(Exception):
    """Exception raised if the API key is missing or invalid."""
    
    def __init__(self, message="API key is required"):
        self.message = message
        super().__init__(self.message)

class RequestError(Exception):
    """Exception raised when an error occurs during the request."""
    
    def __init__(self, message="Error while sending the request"):
        self.message = message
        super().__init__(self.message)

class NotEnoughTokensError(Exception):
    """Exception raised if there are not enough tokens for the request."""
    
    def __init__(self, message="Not enough tokens to perform the request."):
        self.message = message
        super().__init__(self.message)
