from ..request import request

def get_status():
    return request('GET', 'https://emsiservices.com/skills/status')