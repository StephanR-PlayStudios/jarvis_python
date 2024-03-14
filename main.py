from modules.jarvis.jarvis import Jarvis
from modules.utils.config import JarvisConfiguration

if __name__ == "__main__":
    jarvis_configuration = JarvisConfiguration("config.json")
    jarvis_client = Jarvis(jarvis_configuration)

    jarvis_client.login()
    data = jarvis_client.data_as_json()

    print(data)
    # for environment in environments:
    #     print(environment)
    #
    # for branch in branches:
    #     print(branch)
