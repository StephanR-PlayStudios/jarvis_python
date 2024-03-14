import json
import os.path


class JarvisConfiguration:
    def __init__(self, config: str):
        self.config = json.loads(config)

        self.jarvis_api_key = self.config["jarvis_api_key"]
        self.jarvis_userAuthCode = self.config["jarvis_userAuthCode"]
        self.jarvis_clientId = self.config["jarvis_clientId"]
        self.jarvis_rest_url = self.config["jarvis_rest_url"]
        self.game_id = self.config["game_id"]

        if not self.jarvis_api_key or not self.jarvis_userAuthCode or not self.jarvis_clientId or not self.jarvis_rest_url or not self.game_id:
            raise Exception("Invalid configuration")

    # def load_config(self):
    #     if os.path.exists(self.path):
    #         with open(self.path, 'r') as file:
    #             return json.load(file)
    #     raise Exception("Config file not found")
