#!/bin/bash

python3 -m venv venv                        #sets up venv   
source venv/bin/activate            
export GH_TOKEN=$GH_TOKEN                   #ensure GH_TOKEN is in bashrc first

echo "TOKEN: $GH_TOKEN"

git fetch origin

if ! git merge origin/main; then
    echo "Merge conflict encountered. Attempting to resolve with 'theirs' strategy."
    git merge -X theirs origin/main 
fi

if [ -z "$GH_TOKEN" ]; then
    echo "token required"
    exit 1
fi

if [ -f requirements.txt ]; then
    pip install -r requirements.txt         #install requirements
fi

python3 main.py                             #run main
wait $!                                     #wait for end of execution

if [[ $(git status --porcelain) ]]; then    #commit to repo
    git add .
    git commit -m "Monthly update: $(date +'%Y-%m-%d')"
    echo "$GH_TOKEN" | gh auth login --with-token
    git push origin main
fi

deactivate                                  #exit venv

#GH_TOKEN=$GH_TOKEN ./run.sh
