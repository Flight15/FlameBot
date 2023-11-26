import json
import requests
import os

API_URL = 'https://api.getport.io/v1'

OLD_JWT = os.getenv("OLD_JWT")
NEW_JWT = os.getenv("NEW_JWT")

old_headers = {
    'Authorization': f'Bearer {OLD_JWT}'
}

new_headers = {
    'Authorization': f'Bearer {NEW_JWT}'
}


def getBlueprints():
    res = requests.get(f'{API_URL}/blueprints', headers=old_headers)
    resp = res.json()["blueprints"]
    return resp

def postBlueprints(blueprints):
    blueprintsWithoutRelation = blueprints
    for bp in blueprintsWithoutRelation:
        bp.get("relations").clear()
        bp.get("mirrorProperties").clear()
        res = requests.post(f'{API_URL}/blueprints', headers=new_headers, json=bp)
    for blueprint in blueprints:
        res = requests.post(f'{API_URL}/blueprints', headers=new_headers, json=blueprint)

def postEntities(blueprints):
    for blueprint in blueprints:
        res = requests.get(f'{API_URL}/blueprints/{blueprint["identifier"]}/entities', headers=old_headers)
        resp = res.json()["entities"]
        for entity in resp:
            res = requests.post(f'{API_URL}/blueprints/{blueprint["identifier"]}/entities?upsert=true&validation_only=false&create_missing_related_entities=true&merge=false', headers=new_headers, json=entity)

def main():
    blueprints = getBlueprints()
    postBlueprints(blueprints)
    postEntities(blueprints)
    
        