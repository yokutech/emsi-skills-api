from ..request import request

def extract_skills_from_document(documentText, version='latest'):
    return request('POST', f'https://emsiservices.com/skills/versions/{version}/extract', headers={
        'Content-Type': 'application/json'
    }, data={ 'text': documentText })

def extract_skills_with_source_tracing(documentText, version='latest'):
    return request('POST', f'https://emsiservices.com/skills/versions/{version}/extract/trace', headers={
        'Content-Type': 'application/json'
    }, data={ 'text': documentText })