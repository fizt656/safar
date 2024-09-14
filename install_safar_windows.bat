@echo off

REM Check if Python is installed
python --version 2>NUL
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.7 or higher and try again.
    exit /b 1
)

REM Create a virtual environment
python -m venv safar_env

REM Activate the virtual environment
call safar_env\Scripts\activate.bat

REM Install the required dependencies
pip install -r requirements.txt

REM Copy config_example.py to config.py
copy config_example.py config.py

REM Ask for OpenRouter and Replicate tokens
set /p openrouter_key=Enter your OpenRouter API key: 
set /p replicate_token=Enter your Replicate API token: 

REM Update config.py with the provided tokens
powershell -Command "(gc config.py) -replace 'OPENROUTER_KEY = .*', 'OPENROUTER_KEY = ''%openrouter_key%''' | Set-Content config.py"
powershell -Command "(gc config.py) -replace 'REPLICATE_API_TOKEN = .*', 'REPLICATE_API_TOKEN = ''%replicate_token%''' | Set-Content config.py"

REM Set environment variables
setx OPENROUTER_KEY "%openrouter_key%"
setx REPLICATE_API_TOKEN "%replicate_token%"

REM Update the activate.bat script to set environment variables
echo set "OPENROUTER_KEY=%openrouter_key%" >> safar_env\Scripts\activate.bat
echo set "REPLICATE_API_TOKEN=%replicate_token%" >> safar_env\Scripts\activate.bat

echo Installation and configuration complete!
echo To run Safar, use the following commands:
echo safar_env\Scripts\activate.bat
echo python safar.py

REM Deactivate the virtual environment
deactivate