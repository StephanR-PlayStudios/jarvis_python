from modules.jarvis import Jarvis

jarvis_api_key = "odVarYgF1D"
jarvis_userAuthCode = "pJqv2ujfoHFC2xbJM9fA"
jarvis_clientId = "GgCe4CGAEJ"
jarvis_rest_url = "https://jarvis-prod.n3twork.com/api/v1/"
game_id = "da2a12ba-b3dc-46bc-9057-2e2fa6b47c48"
jarvis_client = Jarvis(jarvis_api_key, jarvis_userAuthCode, jarvis_clientId, game_id, jarvis_rest_url)

jarvis_client.login()
environments = jarvis_client.get_environments()
branches = jarvis_client.get_branches()

for environment in environments:
    print(environment)

for branch in branches:
    print(branch)