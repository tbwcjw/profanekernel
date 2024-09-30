#!/bin/bash

source ~/.bashrc

if [ -z "$GH_TOKEN" ]; then
    echo "GH_TOKEN not set"
    exit 1
fi

python3 -m venv venv
source venv/bin/activate

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

python3 main.py
wait $!

if [[ $(git status --porcelain) ]]; then
    git add .
    git commit -m "Monthly update: $(date +'%Y-%m-%d')"
    export GH_TOKEN=$GH_TOKEN
    gh repo sync origin main
fi

deactivate
