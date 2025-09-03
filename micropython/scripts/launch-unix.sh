#!/usr/bin/env bash

MP_BIN='/Users/marvin/Desktop/Projects/workspace/micropython/ports/unix/build-standard/micropython'

#  Path to micropython libraries
MP_LIB_PATH="${HOME}/.micropython/lib"

#  Copy micropython libraries to lib folder
rsync -avP src/tmns/ ${MP_LIB_PATH}/tmns/

${MP_BIN} -i src/main.py
