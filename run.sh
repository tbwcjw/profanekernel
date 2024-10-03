#!/bin/bash

python3 -m venv venv                        #sets up venv   
source venv/bin/activate            
export GH_TOKEN=$GH_TOKEN               #ensure GH_TOKEN is in bashrc

print "$GH_TOKEN"

git pull origin main                        #ensure up-to-date
if [ -f requirements.txt ]; then
    pip install -r requirements.txt         #install requirements
fi

python3 main.py                             #run main
wait $!                                     #wait for end of execution

if [[ $(git status --porcelain) ]]; then    #commit to repo
    git add .
    git commit -m "Monthly update: $(date +'%Y-%m-%d')"
    gh auth login --with-token <<< "$GH_TOKEN"
    git push origin main
fi

deactivate                                  #exit venv

#GH_TOKEN=$GH_TOKEN ./run.sh
