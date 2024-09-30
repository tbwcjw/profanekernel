#!/bin/bash
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

python3 -m venv venv
source venv/bin/activate

python3 main.py
wait $!

if [[ $(git status --porcelain) ]]; then
    git add .
    git commit -m "Monthly update: $(date +'%Y-%m-%d')"
    git push origin main
fi