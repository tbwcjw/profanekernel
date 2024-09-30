#!/bin/bash

python3 main.py
wait $!

if [[ $(git status --porcelain) ]]; then
    git add .
    git commit -m "Monthly update: $(date +'%Y-%m-%d')"
    git push origin main
fi