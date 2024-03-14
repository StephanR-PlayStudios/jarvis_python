#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
decrypt="$SCRIPT_DIR/../config.json"

if [ -z "${1}" ]; then
    echo "Usage ${0} encrypt_key"
    exit 1
fi

echo Working with "$decrypt"
#openssl enc -aes-128-ecb -K "${1}" -in "$decrypt" -out "${decrypt::${#decrypt}-8}"
openssl enc -aes-128-ecb -K "${1}" -in "$decrypt" -out "config.json-enc"

rm "$decrypt"

