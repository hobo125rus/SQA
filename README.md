# Altoro Mutual testing project example

## Description

The project implemented two information security test cases for checking input forms for the Altoro Mutual web resource:

- testing the search input and feedback form for XSS injection.

- testing the search input and feedback form for OS command injection.

## Requirements

python 3.11

pytest 7.4

selenium 4.27.1

You need to install Safari web-driver.

## Notes
The `requirements.txt` file should list all Python libraries that project
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

## Install project

```bash
git clone https://github.com/hobo125rus/SQA.git

cd SQA

```

## Running

```bash
pytest tests/TestFeedback.py

```