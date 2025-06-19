@echo off
REM Check if virtual environment directory exists
if exist .venv (
    echo Virtual environment already exists. Activating...
) else (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment. Is Python installed and in PATH?
        goto :eof
    )
)

REM Activate virtual environment
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Failed to activate virtual environment.
    goto :eof
)

REM Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies.
    goto :eof
)

echo Environment setup complete!
echo You are now in the virtual environment.
echo To deactivate, type "deactivate".
pause