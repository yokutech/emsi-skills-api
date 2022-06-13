from ..request import request


def list_all_skills(version='latest'):
    return request('GET', f'https://emsiservices.com/skills/versions/{version}/skills')


def list_skills_by_params(params, version='latest'):
    return request('GET', f'https://emsiservices.com/skills/versions/{version}/skills', params=params)


def search_skills(term, version='latest'):
    return request('GET', f'https://emsiservices.com/skills/versions/{version}/skills', params={
        'q': term
    })


def skills_by_type(type_ids, version='latest'):
    return request('GET', f'https://emsiservices.com/skills/versions/{version}/skills', params={
        'typeIds': type_ids
    })

def skills_by_ids(skill_ids, params={}, version='latest'):
    return request('POST', f'https://emsiservices.com/skills/versions/{version}/skills',
                   params=params,
                   data={
                       'ids': skill_ids
                   }, headers={
                       'Content-Type': 'application/json'
                   }, )

def skill_by_id(skill_id, version='latest'):
    return request('GET', f'https://emsiservices.com/skills/versions/{version}/skills/{skill_id}')

