import json
import requests

CLIENT_ID = ${{ secrets.CLIENT_ID }}
CLIENT_SECRET = ${{ secrets.CLIENT_SECRET }}

API_URL = 'https://api.getport.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)

access_token = token_response.json()['accessToken']
headers = {
    'Authorization': f'Bearer {access_token}'
}

blueprint_id = 'microservice'
framework_id = 'framework'
response = requests.get(f'{API_URL}/blueprints/{blueprint_id}/entities', headers=headers)
dataServices = response.json()
response = requests.get(f'{API_URL}/blueprints/{framework_id}/entities', headers=headers)
dataFrameworks = response.json()

# You can now use the value in access_token when making further requests

service_eol_counts = {}
#iterate all services and construct arrays of relations per identifiers
for service_entity in dataServices["entities"]:
    service_identifier = service_entity["identifier"]
    related_frameworks = service_entity["relations"].get("used", [])

    #count EOL per service
    eol_countTemp = sum(1 for framework_id in related_frameworks if
                    any(framework["identifier"] == framework_id and framework["properties"]["status"] == "EOL"
                        for framework in dataFrameworks["entities"]))
    #insert to dict
    service_eol_counts[service_identifier] = eol_countTemp

for key in service_eol_counts:
    entity = {
        "identifier": key,
        'properties': {
            'eol_count': service_eol_counts[key]
        }

    }
    response = requests.post(f'{API_URL}/blueprints/{blueprint_id}/entities?upsert=true&merge=true', json=entity, headers=headers)
print(service_eol_counts)
