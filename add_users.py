import json
import base64
import requests

# GitHub API URL für die users.json
GITHUB_API_URL = "https://api.github.com/repos/deinusername/deinrepo/contents/users.json"
GITHUB_TOKEN = "DEIN_GITHUB_TOKEN"

# Funktion zum Hinzufügen eines neuen Benutzers
def add_new_user(username, password, role):
    # Benutzerdaten abrufen
    response = requests.get(GITHUB_API_URL, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    users = json.loads(base64.b64decode(response.json()['content']).decode())

    # Neuen Benutzer hinzufügen
    new_user = {
        "username": username,
        "password": password,
        "role": role
    }
    users.append(new_user)

    # Die geänderte Liste der Benutzer in Base64 kodieren
    encoded_data = base64.b64encode(json.dumps(users).encode()).decode()

    # Datei auf GitHub aktualisieren
    update_data = {
        "message": "Benutzer hinzugefügt",
        "content": encoded_data,
        "sha": response.json()['sha']
    }
    update_response = requests.put(GITHUB_API_URL, json=update_data, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    return update_response.json()

# Beispielhafter Aufruf der Funktion
add_new_user("neuerbenutzer", "meinpassword123", "student")
