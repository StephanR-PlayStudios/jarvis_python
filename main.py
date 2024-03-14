import os
import subprocess

from modules.jarvis.jarvis import Jarvis
from modules.utils.config import JarvisConfiguration

if __name__ == "__main__":
    decrypt_file = subprocess.run(['./bin/decrypt-ebenc.sh', os.environ.get('AES_KEY')],
                                  stdout=subprocess.PIPE,
                                  check=True,
                                  text=True)

    jarvis_configuration = JarvisConfiguration(decrypt_file.stdout)
    jarvis_client = Jarvis(jarvis_configuration)

    jarvis_client.login()
    data = jarvis_client.data_as_json()

    print(data)
