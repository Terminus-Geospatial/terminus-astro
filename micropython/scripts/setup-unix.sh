#!/usr/bin/env bash

#  Micropython Install
MP_BIN='/Users/marvin/Desktop/Projects/workspace/micropython/ports/unix/build-standard/micropython'

#  Setup Dependencies
${MP_BIN} ./scripts/py/install-deps.py -v
