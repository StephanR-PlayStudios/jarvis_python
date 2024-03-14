#!/usr/bin/env python3
import argparse
import os
import subprocess

from icecream import ic

from modules.jarvis.jarvis import Jarvis
from modules.utils.config import JarvisConfiguration

if __name__ == "__main__":
    decrypt_key = os.environ.get("AES_KEY")
    if not decrypt_key:
        raise Exception("AES_KEY environment variable not found")
    decrypt_file = subprocess.run(['./bin/decrypt-ebenc.sh', os.environ.get('AES_KEY')],
                                  stdout=subprocess.PIPE,
                                  check=True,
                                  text=True)
    parser = argparse.ArgumentParser(prog='Jarvis', description='Jarvis tool to get data from it')
    parser.add_argument('--env', help='Get environments', action='store_true')
    parser.add_argument('--branch', help='Get branches', action='store_true')
    parser.add_argument('--batch', help='Get environments and branches', action='store_true', default=True)
    args = parser.parse_args()

    if args.batch:
        ic.disable()

    jarvis_configuration = JarvisConfiguration(decrypt_file.stdout)
    jarvis_client = Jarvis(jarvis_configuration)

    data = jarvis_client.refresh()
    print(data)
    

