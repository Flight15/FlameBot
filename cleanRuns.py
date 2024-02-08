import json
import requests

API_URL = 'https://api.getport.io/v1'

CLIENT_ID = "2gA7Yt4tsfH9RwRnbmp3ElzArMjNPmJr"
CLIENT_SECRET = "TJO25UQCp1k4UJBZP6pHw5zGQ1ncJ4809A9GdPy2CE4Ne4ec3Ygj4BglmwBYnmJU" 


credentials = { 'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET }
credentials = requests.post(f'{API_URL}/auth/access_token', json=credentials)
access_token = credentials.json()["accessToken"]
headers = {
    'Authorization': f'Bearer {access_token}'
}

runsResponse = requests.get(f'{API_URL}/actions/runs?active=true', headers=headers)
runs = runsResponse.json()["runs"]

for run in runs:
    print(f"Cleaning run {run['id']}")
    res = requests.patch(f"{API_URL}/actions/runs/{run['id']}", headers=headers, json={"status": "SUCCESS"})
    if res.status_code != 200:
        print(f"error cleaning run {run['id']}: {json.dumps(res.json())}")