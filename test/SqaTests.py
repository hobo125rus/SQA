import logging
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.errorhandler import NoAlertPresentException
from framework.const.Constants import TestCaseConstants

def init_web_page():
    """
    A function that initializes the web driver and sets the initial logging parameters. 
    Parameters:
        None
    
    Returns:
    -----------
        driver: object
            Pointer to webdriver.
    """
    driver = webdriver.Safari()
    driver.get('http://testfire.net/feedback.jsp')
    logging.basicConfig(format='%(asctime)s - INFO - %(message)s', level=logging.INFO)
    return driver

def TC_012():
    """
    The function performs a check according to test case #12. 
    Cross-site Script Vulnerability Testing (XSS).    
    Parameters:
        None
    
    Returns:
    -----------
        bool
            Returns True if the test did not detect XSS vulnerabilities 
            and returns False if vulnerabilities are detected.    
    """
    driver = init_web_page()
    textarea_fields = driver.find_element(By.XPATH, '//textarea')
    input_tags = driver.find_elements(By.TAG_NAME, 'input')
    input_text_fields = []
    btn_submit = []
    btn_search = []

    for input_field in input_tags:
        if input_field.get_attribute('type') == 'text' \
        or input_field.get_attribute('name') == 'subject':
            input_text_fields.append(input_field)
        elif input_field.get_attribute('name') == 'submit':
            btn_submit = input_field
        elif input_field.get_attribute('value') == 'Go':
            btn_search = input_field
        else:
            logging.info(f'It is not possible to enter text for the "input" tag with the type: \
    {input_field.get_attribute("type")}')

    input_field = None
    input_text_fields.append(textarea_fields)
    logging.info(f'Total testing inputs: {len(input_text_fields)}')
    tcconstants = TestCaseConstants.Test_XSS

    for cmd in tcconstants:
        for input_field in input_text_fields:
            input_field.send_keys(cmd)
            if input_field.get_attribute('name') == 'query':
                btn_search.click()
            else:
                btn_submit.click()
            sleep(1)
            try:
                alert = Alert(driver)
                logging.info(f'Finded alert text: "{alert.text}".')
                alert.accept()
                assert False, 'Finded alert'
            except NoAlertPresentException:
                logging.info('No alert.')
                assert True
            driver.back()
            input_field.clear()
    driver.close()

#@pytest.mark.skip
def test_exception_tc012():
    TC_012()

def TC_017():
    """
    The function performs a check according to test case #17. 
    Testing of OS command injections.    
    Parameters:
        None
    
    Returns:
    -----------
        bool
            Returns True if the test did not detect OS command injections 
            and returns False if vulnerabilities are detected.    
    """
    driver = init_web_page()
    input_text_fields = driver.find_elements(By.XPATH, '//input[@type="text"]')
    input_subject_fields = driver.find_elements(By.XPATH, '//input[@name="subject"]')
    btn_submit = driver.find_element(By.XPATH, '//input[@name="submit"]')
    btn_search = driver.find_element(By.XPATH, '//input[@value="Go"]')
    textarea_fields = driver.find_elements(By.XPATH, '//textarea')
    tcconstants = TestCaseConstants.Test_COMMANDs

    for cmd in tcconstants:
        for input_field in input_text_fields:
            input_field.send_keys(cmd[1])
            if input_field.get_attribute('name') == 'query':
                btn_search.click()
                sleep(1)
                assert cmd[0] not in driver.page_source
            else:
                btn_submit.click()
                sleep(1)
                assert cmd[0] not in driver.page_source
            driver.back()
            input_field.clear()
        for input_subject in input_subject_fields:
            input_subject.send_keys(cmd[1])
            btn_submit.click()
            sleep(1)
            assert cmd[0] not in driver.page_source
            driver.back()
            input_subject.clear()
        for textarea in textarea_fields:
            textarea.send_keys(cmd[1])
            btn_submit.click()
            sleep(1)
            assert cmd[0] not in driver.page_source
            driver.back()
            textarea.clear()
    driver.close()

@pytest.mark.skip
def test_exception_tc017():
    TC_017()
    