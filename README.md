# IDS706-Assignment-1

[![Python tests](https://github.com/agastyavinchhi/IDS706-Assignment-1/actions/workflows/test.yml/badge.svg)](https://github.com/agastyavinchhi/IDS706-Assignment-1/actions/workflows/test.yml)

# My Python Project

This project asks for a name and prints a welcome message for the Data Engineering course. It also adds the number of credits of the course

## Bonus Points
- Added make lint and make format in Makefile. Updated requirements.txt to reflect the same
- Added a new function, along with a unique test for the new function, and changed the welcome message

## Setup
python -m venv .venv
source .venv/bin/activate      # Mac / Linux
.venv\Scripts\activate          # Windows
pip install -r requirements.txt

## Run tests
python -m pytest

## Inputs
Enter your name when prompted and enter the number of credits when prompted
