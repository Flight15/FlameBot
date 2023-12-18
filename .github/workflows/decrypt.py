import requests
import os

port_client_id = os.environ['PORT_CLIENT_ID']
port_client_secret = os.environ['PORT_CLIENT_SECRET']
api_url = "https://api.getport.io/v1"

credentials = {"client_id": port_client_id, "client_secret": port_client_secret}
res = requests.post(f"{api_url}/auth/access_token", json=credentials)
access_token = res.json()["access_token"]
headers = {
    "Authorization": f"Bearer {access_token}"
}

port_members = requests.get(f"{api_url}/teams/Port%20Member?fields=name&fields=users.email", headers=headers).json()
port_moderators = requests.get(f"{api_url}/teams/Port%20Moderator?fields=name&fields=users.email", headers=headers).json()
port_admins = requests.get(f"{api_url}/teams/Port%20Admin?fields=name&fields=users.email", headers=headers).json()

for member in port_members["users"]:
    print(member["email"])