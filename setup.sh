#!/bin/bash

# Install Python 3.12 if not already installed
if ! python3.12 --version &>/dev/null; then
  echo "Installing Python 3.12..."
  sudo apt-get update
  sudo apt-get install -y python3.12 python3.12-venv python3.12-dev
fi

# Create a virtual environment
python3.12 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r HelloUniversal/requirements.txt

echo "Setup complete. To activate the virtual environment, run 'source venv/bin/activate'."
