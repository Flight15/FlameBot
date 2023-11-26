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

def main():
    blueprints = getBlueprints()
    for blueprint in blueprints:
        res = requests.get(f'{API_URL}/blueprints/{blueprint["identifier"]}/entities', headers=old_headers)
        resp = res.json()["entities"]
        for entity in resp:
            res = requests.post(f'{API_URL}/blueprints/{blueprint["identifier"]}/entities', headers=new_headers, json=entity)