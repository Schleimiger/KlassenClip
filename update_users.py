import requests
import json

GITHUB_API_URL = "https://api.github.com/repos/deinusername/deinrepo/contents/users.json"
GITHUB_TOKEN = "DEIN_GITHUB_TOKEN"

def add_new_user(username, password, role):
    # Benutzerdaten abrufen
    response = requests.get(GITHUB_API_URL, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    users = json.loads(response.json()['content'])
    
    # Neuen Benutzer hinzufügen
    new_user = {
        "username": username,
        "password": password,
        "role": role
    }
    users.append(new_user)
    
    # JSON in Base64 kodieren
    encoded_data = base64.b64encode(json.dumps(users).encode()).decode()
    
    # Update der Datei auf GitHub
    update_data = {
        "message": "Add new user",
        "content": encoded_data,
        "sha": response.json()['sha']
    }
    update_response = requests.put(GITHUB_API_URL, json=update_data, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    return update_response.json()
