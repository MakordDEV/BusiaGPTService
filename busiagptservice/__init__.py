import requests
from busiagptservice.errors import *

class BusiaGPT_Service:
    """
    A service class for interacting with the GPTs API.

    This class allows you to make requests to the GPTs models (e.g., busiai or chatgpt).
    It requires a valid API key, which is used for authentication when making requests.
    
    Methods:
        use_busiai(prompt): Uses the busiai model to process the provided prompt.
        use_chatgpt(prompt): Uses the chatgpt model to process the provided prompt.
    """
    
    def __init__(self):
        """
        Initializes the BusiaGPT_Service instance.

        This sets the initial values for the API key (which is None by default) 
        and the base URL for making API requests.
        """
        self.api_key = None  # API key used for authorization
        self.base_url = "http://busia-tep-nya.ru/busia-gpt-service/api/"  # Base URL for the API
    
    def _check_api_key(self):
        """
        Ensures that the API key is set before making a request.

        Raises:
            APIKeyMissingOrInvalidError: If the API key is not provided.
        """
        if not self.api_key:
            raise APIKeyMissingOrInvalidError("API key is required to make the request.")

    def _handle_error(self, response_json):
        """
        Handles errors based on the response from the API.

        This method checks the error message and raises the appropriate custom error.
        
        :param response_json: The JSON response from the API that contains the error message.
        :raises: NotEnoughTokensError, APIKeyMissingOrInvalidError, RequestError based on the error message.
        """
        error_message = response_json.get('error', '')
        
        if "Not enough tokens" in error_message:
            raise NotEnoughTokensError("Not enough tokens to perform the request. You can top up your tokens in the Manager Busia.")
        elif "Invalid API key" in error_message:
            raise APIKeyMissingOrInvalidError("The API key is invalid and has been rejected by the system.")
        elif "Busi AI is" in error_message:
            raise RequestError("Busi AI is temporarily unavailable. Please try again later.")
        else:
            raise RequestError(error_message)

    def _send_request(self, model_name, prompt):
        """
        Sends a POST request to the API for a specific model with a given prompt.

        :param model_name: The name of the model (e.g., busiai or chatgpt).
        :param prompt: The prompt to be sent to the model.
        :return: The server's response in JSON format if successful.
        :raises: RequestError if there is an issue with the request or API response.
        """
        self._check_api_key()  # Ensure the API key is set

        url = f"{self.base_url}{model_name}/"  # Build the full URL for the request
        headers = {
            "Authorization": f"Bearer {self.api_key}",  # Set the Authorization header
            "Content-Type": "application/json"  # Indicate that the request body is JSON
        }
        
        # Send the request to the API
        try:
            response = requests.post(url, headers=headers, json={"prompt": prompt})  # Send request to the server
            response.raise_for_status()  # Raise an error if the response status is not 200 OK
            response_json = response.json()  # Parse the response as JSON

            # Handle errors if present in the response
            if 'error' in response_json:
                self._handle_error(response_json)

            return response_json  # Return the successful response

        except requests.RequestException as e:
            raise RequestError(f"Error during request to model {model_name}: {e}")

    def use_busiai(self, prompt):
        """
        Uses the busiai model to process the provided prompt.

        :param prompt: The prompt to be sent to the busiai model.
        :return: The server's response in JSON format if successful.
        :raises: RequestError if there is an issue with the request.
        """
        return self._send_request("busiai", prompt)

    def use_chatgpt(self, prompt):
        """
        Uses the chatgpt model to process the provided prompt.

        :param prompt: The prompt to be sent to the chatgpt model.
        :return: The server's response in JSON format if successful.
        :raises: RequestError if there is an issue with the request.
        """
        return self._send_request("chatgpt", prompt)
