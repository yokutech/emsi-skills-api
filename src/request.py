import json
import requests

from .auth import getToken

def request(
    method,
    url,
    params = {},
    data = {},
    headers = {},
    authenticated = True
):
    if authenticated:
        token = getToken()
        headers = {
            **headers,
            'Authorization': f'Bearer {token}'
        }
    
    response = requests.request(method, url, params= params, data=json.dumps(data), headers=headers)
    return response.json()
