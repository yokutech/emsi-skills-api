import requests
from datetime import datetime, timedelta

token = None
expires_in = None

def getToken():
    global token
    global expires_in

    now = datetime.now()

    if token is not None and expires_in is not None and now < expires_in:
        return token

    url = 'https://auth.emsicloud.com/connect/token'

    payload = {
        'client_id': '<EMSI_CLIENT_ID>',
        'client_secret': '<EMSI_SECRET>',
        'grant_type': 'client_credentials',
        'scope': '<EMSI_SCOPE>' or 'emsi_open'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request('POST', url, data=payload, headers=headers)

    auth = response.json()
    token = auth['access_token']
    expires_in = now + timedelta(seconds=auth['expires_in'])

    return token