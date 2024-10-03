#!/bin/bash

python3 -m venv venv                        #sets up venv   
source venv/bin/activate            

gh auth login

git fetch origin

if ! git merge origin/main; then
    echo "Merge conflict encountered. Attempting to resolve with 'theirs' strategy."
    git merge -X theirs origin/main 
fi

if [ -f requirements.txt ]; then
    pip install -r requirements.txt         #install requirements
fi

python3 main.py                             #run main
wait $!                                     #wait for end of execution

if [[ $(git status --porcelain) ]]; then    #commit to repo
    git add .
    git commit -m "Monthly update: $(date +'%Y-%m-%d')"
    git push origin main
fi

deactivate                                  #exit venv

#GH_TOKEN=$GH_TOKEN ./run.sh
