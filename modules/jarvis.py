import requests
import json


class Jarvis:
    def __init__(self, api_key, user_auth_code, client_code, game_id, base_url):
        self.api_key = api_key
        self.user_auth_code = user_auth_code
        self.client_code = client_code
        self.game_id = game_id
        self.base_url = base_url
        self.access_token = None

    def login_request(self):
        return {
            "grantor": "API",
            "userAuthCode": self.user_auth_code,
            "clientId": self.client_code
        }

    def login(self):
        url = f"{self.base_url}auth/oauth2"
        headers = {
            "Content-Type": "application/json"
        }
        data = self.login_request()
        res = requests.post(url, headers=headers, data=json.dumps(data))
        response = res.json()
        if response['success']:
            self.access_token = response['payload']['access_code']
            return
        raise Exception("Failed to login")

    def get_environments(self):
        url = f"{self.base_url}config/environments/{self.game_id}"
        print(url)
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        res = requests.get(url, headers=headers)
        response = res.json()
        if response['success']:
            for i in response['payload']:
                claimedBy = i['claimedByDisplayName'] if 'claimedByDisplayName' in i else ""
                yield JarvisEnvironment(i['id'], i['gameId'], i['name'], i['production'], i['configId'], i['configVersion'], i['configName'], claimedBy)
            return response['payload']

    def get_branches(self):
        url = f"{self.base_url}config/branches/{self.game_id}"
        print(url)
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        res = requests.get(url, headers=headers)
        response = res.json()
        branches = list()
        if response['success']:
            for i in response['payload']:
                branches.append(JarvisBranch(i['id'], i['gameId'], i['name'], i['gitBranch']))
            return branches

class JarvisBranch:
    def __init__(self, branchId, gameId, name, gitBranch):
        self.id = branchId
        self.gameId = gameId
        self.name = name
        self.gitBranch = gitBranch

    def __str__(self):
        return f"[Environments] Name: {self.name}, branch: {self.gitBranch}"
class JarvisEnvironment:
    def __init__(self, id, gameId, name, production, configId, config_version, config_name, claimedByDisplayName):
        self.id = id
        self.gameId = gameId
        self.name = name
        self.production = production
        self.configId = configId
        self.config_version = config_version
        self.config_name = config_name
        self.claimedByDisplayName = claimedByDisplayName

    def __str__(self):
        return f"[Branches] Name: {self.name}, Production: {self.production}, Config: {self.config_name}, Claimed by: {self.claimedByDisplayName}"
