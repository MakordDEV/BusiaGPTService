# Busia GPT Service
busia_gpt_service is a Python package designed to interact with the Busia GPT models (such as busiai and chatgpt) through an easy-to-use API interface. This package allows you to send prompts to the Busia GPT models and receive responses, enabling you to integrate advanced AI functionalities into your own applications or scripts.

## Note:
This package is developed exclusively for use by the developer and their friends. Only authorized users who possess a valid API key will be able to access the service. If you're not familiar with the developer or do not have a key, you will not be able to use the API.

## Features
Simple interface to interact with GPT models.
Supports both BusiAI and ChatGPT models.
Requires a valid API key for authentication.
Handles common errors such as invalid API keys and insufficient tokens.
Provides clear error messages to guide you through any issues.
## Installation
To install the busiagptservice package, you can use pip:

```
pip install busiagptservice
```
Alternatively, if you want to install it directly from the repository:

```
git clone https://github.com/MakordDEV/BusiaGPTService.git
cd BusiaGPTService
pip install .
```
## Usage
To use the busiagptservice package, you must have a valid API key. Once you have your API key, you can start interacting with the Busia GPT models.

#Example:
```
from busia_gpt_service import BusiaGPT_Service

# Create an instance of the service
service = BusiaGPT_Service()

# Set your API key (this should be provided to you by the developer)
service.api_key = "YOUR_API_KEY"

# Send a prompt to the chatgpt model
response = service.use_chatgpt("Tell me a joke!")

# Print the response from the model
print(response["choices"][0]["message"]["content"])
```
In this example:

You create an instance of BusiaGPT_Service.
Set your API key to authenticate your requests.
Send a prompt to the chatgpt model (or busiai model).
The response from the model is printed.
## Available Methods:
use_busiai(prompt): Sends a prompt to the busiai model.
use_chatgpt(prompt): Sends a prompt to the chatgpt model.
## API Key
Getting an API Key:
To use the busia_gpt_service package, you must obtain an API key. This API key is only available to the developer and their friends. Unauthorized users will not be able to access the service.

If you are a trusted user, contact the developer for your API key.
## Set the API Key:
Once you have the key, you can set it in your code like so:

```
service.api_key = "YOUR_API_KEY"
```
Make sure to keep your API key secure and do not share it publicly.

## Error Handling
The service includes built-in error handling for common issues:

APIKeyMissingOrInvalidError: Raised if no API key is provided or the API key is invalid.
NotEnoughTokensError: Raised if there are insufficient tokens to process the request.
RequestError: Raised for any general errors encountered during the API request.
Contributing
Since this package is designed only for the developer and their trusted users, contributions from others are not expected at this time. If you believe you need access to the API or want to contribute, please contact the developer directly.

## License
This project is not licensed for public use and is only intended for use by the developer and their friends. Please refrain from distributing or sharing the package for malicious purposes.
