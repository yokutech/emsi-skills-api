from ..request import request

def get_meta():
    return request('GET', 'https://emsiservices.com/skills/meta')
