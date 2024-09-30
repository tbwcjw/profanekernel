#!/bin/bash
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
    gh pr create --base main --head main --title "Monthly update" --body "Update for $(date +'%Y-%m-%d')"
fi

deactivate
