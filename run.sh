#!/bin/bash

python3 -m venv venv                        #sets up venv   
source venv/bin/activate            

if [ "$#" -ne 1 ]; then
    echo "token required"
fi

TOKEN=$1

git fetch origin

if [ -f requirements.txt ]; then
    pip install -r requirements.txt         #install requirements
fi

python3 main.py                             #run main
wait $!                                     #wait for end of execution

if [[ $(git status --porcelain) ]]; then    #commit to repo
    git add .
    git commit -m "Monthly update: $(date +'%Y-%m-%d')"
    git push https://tbwcjw:$TOKEN@github.com/tbwcjw/profanekernel.git main
fi
deactivate                                  #exit venv