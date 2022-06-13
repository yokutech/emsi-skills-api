from ..request import request

def get_related(ids, version='latest'):
    return request('POST', f'https://emsiservices.com/skills/versions/{version}/related', headers= { 'Content-Type': 'application/json' }, data={ 'ids': ids })
