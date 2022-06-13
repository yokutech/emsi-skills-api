from ..request import request

def get_versions():
    return request('GET', 'https://emsiservices.com/skills/versions')

def get_version_metadata(version='latest'):
    return request('GET', f'https://emsiservices.com/skills/versions/{version}')