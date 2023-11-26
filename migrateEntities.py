import json
import requests
import os

API_URL = 'https://api.getport.io/v1'

OLD_CLIENT_ID = os.getenv("OLD_CLIENT_ID")
OLD_CLIENT_SECRET = os.getenv("OLD_CLIENT_SECRET")
NEW_CLIENT_ID = os.getenv("NEW_CLIENT_ID")
NEW_CLIENT_SECRET = os.getenv("NEW_CLIENT_SECRET")

old_credentials = { 'clientId': OLD_CLIENT_ID, 'clientSecret': OLD_CLIENT_SECRET }
old_token_response = requests.post(f'{API_URL}/auth/access_token', json=old_credentials)
old_access_token = old_token_response.json()["accessToken"]
old_headers = {
    'Authorization': f'Bearer {old_access_token}'
}

new_credentials = { 'clientId': NEW_CLIENT_ID, 'clientSecret': NEW_CLIENT_SECRET }
new_token_response = requests.post(f'{API_URL}/auth/access_token', json=new_credentials)
new_access_token = new_token_response.json()["accessToken"]
new_headers = {
    'Authorization': f'Bearer {new_access_token}'
}


def getBlueprints():
    res = requests.get(f'{API_URL}/blueprints', headers=old_headers)
    resp = res.json()["blueprints"]
    return resp

def postBlueprints(blueprints):
    blueprintsWithoutRelation = blueprints.copy()
    for bp in blueprintsWithoutRelation:
        bp.get("relations").clear()
        bp.get("mirrorProperties").clear()
        requests.post(f'{API_URL}/blueprints', headers=new_headers, json=bp)
    for blueprint in blueprints:
        requests.post(f'{API_URL}/blueprints', headers=new_headers, json=blueprint)

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
    
        