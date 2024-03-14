#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
encrypt="$SCRIPT_DIR/../config.json-enc"

if [ -z "${1}" ]; then
    echo "Usage ${0} encrypt_key"
    exit 1
fi

openssl enc -d -aes-128-ecb -K "${1}" -in "$encrypt"

