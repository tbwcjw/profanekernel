#!/bin/bash

python3 -m venv venv                        #sets up venv   
source venv/bin/activate            

git pull                                    #ensure up-to-date
if [ -f requirements.txt ]; then
    pip install -r requirements.txt         #install requirements
fi

python3 main.py                             #run main
wait $!                                     #wait for end of execution

if [[ $(git status --porcelain) ]]; then    #commit to repo
    git add .
    git commit -m "Monthly update: $(date +'%Y-%m-%d')"
    export GH_TOKEN=$GH_TOKEN               #ensure GH_TOKEN is in bashrc
    gh pr create --fill --base main --head main --title "Monthly update: $(date +'%Y-%m-%d')" --body "Automated update."
    gh pr merge --auto
fi

deactivate                                  #exit venv

#GH_TOKEN=$GH_TOKEN ./run.sh
