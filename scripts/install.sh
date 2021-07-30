#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing