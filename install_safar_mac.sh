#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install Python 3.7 or higher and try again."
    exit 1
fi

# Create a virtual environment
python3 -m venv safar_env

# Activate the virtual environment
source safar_env/bin/activate

# Install the required dependencies
pip install -r requirements.txt

# Copy config_example.py to config.py
cp config_example.py config.py

# Ask for OpenRouter and Replicate tokens
read -p "Enter your OpenRouter API key: " openrouter_key
read -p "Enter your Replicate API token: " replicate_token

# Update config.py with the provided tokens
sed -i '' "s|OPENROUTER_KEY = .*|OPENROUTER_KEY = '$openrouter_key'|" config.py
sed -i '' "s|REPLICATE_API_TOKEN = .*|REPLICATE_API_TOKEN = '$replicate_token'|" config.py

# Set environment variables
echo "export OPENROUTER_KEY='$openrouter_key'" >> safar_env/bin/activate
echo "export REPLICATE_API_TOKEN='$replicate_token'" >> safar_env/bin/activate

echo "Installation and configuration complete!"
echo "To run Safar, use the following commands:"
echo "source safar_env/bin/activate"
echo "python safar.py"

# Deactivate the virtual environment
deactivate