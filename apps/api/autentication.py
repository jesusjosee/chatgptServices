import requests
from decouple import config

def validate_api_key(api_key):
    url = "https://api.openai.com/v1/models"
    headers = { 'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return {"api_key": 'valid_api_key'}
    else:
        return {"api_key": 'invalid_api_key'}