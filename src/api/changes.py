from ..request import request

def get_version_specific_changes(version='latest'):
    return request('GET', f'https://emsiservices.com/skills/versions/{version}/changes')