@echo off
setlocal

python -m venv venv
call venv\Scripts\activate.bat

if "%~1"=="" (
    echo Token required
    exit /b 1
)

set TOKEN=%~1

git fetch origin

if exist requirements.txt (
    pip install -r requirements.txt
)

python main.py

git status --porcelain >nul
if %errorlevel% neq 0 (
    git add .
    git commit -m "Monthly update: %date%"
    git push https://tbwcjw:%TOKEN%@github.com/tbwcjw/profanekernel.git main
)

deactivate
endlocal