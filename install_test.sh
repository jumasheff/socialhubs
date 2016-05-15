#!/bin/bash

if [ ! -d "venv" ]; then
    virtualenv --no-site-packages --distribute venv
fi
. venv/bin/activate
pip install -r requirements.txt
deactivate
