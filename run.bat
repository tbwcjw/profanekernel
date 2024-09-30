@echo off
:: sets up venv
python -m venv venv                 
call venv\Scripts\activate

::set github token
set GH_TOKEN=%GH_TOKEN%

:: ensures up-to-date
git pull

:: installs requirements
if exist requirements.txt (
    pip install -r requirements.txt
)
:: run main
python main.py

::commit to repo
git status --porcelain >nul 2>&1
if not errorlevel 1 (
    git add .
    for /f "tokens=1-3 delims=/ " %%a in ('date /t') do (
        set TODAY=%%c-%%a-%%b
    )
    git commit -m "Monthly update: %TODAY%"
    
    ::push commit
    git push origin master
)

::exit venv
deactivate