import requests
import json

from icecream import ic

from modules.jarvis.jarvis_branch import JarvisBranch
from modules.jarvis.jarvis_environment import JarvisEnvironment
from modules.utils.config import JarvisConfiguration


class Jarvis:
    def __init__(self, jarvis_configuration: JarvisConfiguration):
        self.api_key = jarvis_configuration.jarvis_api_key
        self.user_auth_code = jarvis_configuration.jarvis_userAuthCode
        self.client_code = jarvis_configuration.jarvis_clientId
        self.game_id = jarvis_configuration.game_id
        self.base_url = jarvis_configuration.jarvis_rest_url
        self.access_token = None
        self.jarvis_environments = list()
        self.jarvis_branches = list()
        self.data = None

    def login_request(self):
        return {
            "grantor": "API",
            "userAuthCode": self.user_auth_code,
            "clientId": self.client_code
        }

    def login(self):
        url = f"{self.base_url}auth/oauth2"
        ic(f"Logging in to {url}")
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
        ic(f"Getting environments from {url}")
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        res = requests.get(url, headers=headers)
        response = res.json()
        if response['success']:
            for i in response['payload']:
                claimedBy = i['claimedByDisplayName'] if 'claimedByDisplayName' in i else ""
                self.jarvis_environments.append(JarvisEnvironment(i['id'], i['gameId'], i['name'], i['production'], i['configId'],
                                                      i['configVersion'], i['configName'], claimedBy))
        else:
            raise Exception("Failed to get environments")
        return self.jarvis_environments

    def get_branches(self):
        url = f"{self.base_url}config/branches/{self.game_id}"
        ic(f"Getting branches from {url}")
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        res = requests.get(url, headers=headers)
        response = res.json()
        if response['success']:
            for i in response['payload']:
                self.jarvis_branches.append(JarvisBranch(i['id'], i['gameId'], i['name'], i['gitBranch']))
        else:
            raise Exception("Failed to get branches")

        return self.jarvis_branches

    def data_as_json(self):
        self.get_branches()
        self.get_environments()
        self.data = json.dumps({
            "environments": [env.__dict__ for env in self.jarvis_environments],
            "branches": [branch.__dict__ for branch in self.jarvis_branches]
        })

    def refresh(self):
        self.login()
        self.data_as_json()
        return self.data
