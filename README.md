# Colour Palette Generator

This is a simple colour palette generator built using Flask.

## Installation (Ubuntu)

Python, pip and venv must all be installed:

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv
```

Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install pip requirements:

```bash
pip3 install -r requirements.txt
```

## Testing 

To run tests and retrieve coverage:

```bash
pytest --cov=application --cov-report=term-missing
```

To generate `JUnit` and `Cobertura` coverage reports:

```bash
pytest --cov=application --junitxml=junit.xml --cov-report=xml --cov-report=term-missing
```

## Running the App

Run:

```bash
python3 app.py
```
