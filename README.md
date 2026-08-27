# IDS706-Assignment-1

[![Python tests](https://github.com/agastyavinchhi/IDS706-Assignment-1/actions/workflows/test.yml/badge.svg)](https://github.com/agastyavinchhi/IDS706-Assignment-1/actions/workflows/test.yml)

# My Python Project

This project asks for a name and number of credits, and prints a welcome message along with the number of credits for the Data Engineering course.

## Bonus Points
- Added make lint and make format in Makefile. Updated requirements.txt to reflect the same
- Added a new function, along with a unique test for the new function, and changed the welcome message

## Inputs
Enter your name when prompted. Also, enter the number of credits when prompted. The output will print a welcome message along with the number of credits the course is.

## Setup
python -m venv .venv
source .venv/bin/activate      # Mac / Linux
.venv\Scripts\activate          # Windows
pip install -r requirements.txt

## Run tests
python -m pytest

