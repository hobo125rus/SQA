# Altoro Mutual testing project example

## Description

The project implemented two information security test cases for checking input forms for the Altoro Mutual web resource:

* The function with index #012 in TestFeedback.py - testing the search input and feedback form for XSS injection.
  Ex: test_feedback_<field_name>_tc012

* The function with index #017 in TestFeedback.py - testing the search input and feedback form for OS command injection.
  Ex: test_feedback_<field_name>_tc017

## The main classes presented in the framework are:

- BrowserCls: This class describes the basic methods of working with WebDriver.
- BasePageCls: This class describes the basic methods of working with web page.
- InputFieldCls: This class describes the basic methods of working with the elements responsible for the feedback area.
- SearchFieldCls: This class describes the basic methods of working with the elements responsible for the search area.

## Requirements

- python 3.11

- pytest 7.4

- selenium 4.27.1

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
