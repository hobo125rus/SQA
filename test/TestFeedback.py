from framework.pageobject.inputfield import InputField
from framework.pageobject.inputfield import SearchField
from framework.const.constants import TestCaseConstants
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.errorhandler import NoAlertPresentException
from time import sleep

def test_feedback_search_tc012(browser):
    """
    Test function for XSS field 'search' vulnerabilities according to test case #012.
    """
    feedback_page = SearchField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        feedback_page.enter_word_search(cmd)
        feedback_page.click_on_the_search_button()
        sleep(1)
        try:
            alert = Alert(browser)
            alert.accept()
            assert False, 'Finded alert'
        except NoAlertPresentException:
            assert True        
        browser.back()
        feedback_page.search_clear()

def test_feedback_search_tc017(browser):
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'search' field
    according to test case #017.
    """
    feedback_page = SearchField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.enter_word_search(cmd[1])
        feedback_page.click_on_the_search_button()
        sleep(1)
        assert cmd[0] not in browser.page_source
        browser.back()
        feedback_page.search_clear()

def test_feedback_name_tc012(browser):
    """
    Test function for XSS field 'name' vulnerabilities according to test case #012.
    """
    feedback_page = InputField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        feedback_page.enter_word_name(cmd)
        feedback_page.click_on_the_submit_button()
        sleep(1)
        try:
            alert = Alert(browser)
            alert.accept()
            assert False, 'Finded alert'
        except NoAlertPresentException:
            assert True        
        browser.back()
        feedback_page.name_clear()

def test_feedback_name_tc017(browser):
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'name' field
    according to test case #017.
    """
    feedback_page = InputField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.enter_word_name(cmd[1])
        feedback_page.click_on_the_submit_button()
        sleep(1)
        assert cmd[0] not in browser.page_source
        browser.back()
        feedback_page.name_clear()
        
def test_feedback_email_tc012(browser):
    """
    Test function for XSS field 'email' vulnerabilities according to test case #012.
    """
    feedback_page = InputField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        feedback_page.enter_word_email(cmd)
        feedback_page.click_on_the_submit_button()
        sleep(1)
        try:
            alert = Alert(browser)
            alert.accept()
            assert False, 'Finded alert'
        except NoAlertPresentException:
            assert True        
        browser.back()
        feedback_page.email_clear()

def test_feedback_email_tc017(browser):
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'email' field
    according to test case #017.
    """
    feedback_page = InputField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.enter_word_email(cmd[1])
        feedback_page.click_on_the_submit_button()
        sleep(1)
        assert cmd[0] not in browser.page_source
        browser.back()
        feedback_page.email_clear()
        
def test_feedback_subject_tc012(browser):
    """
    Test function for XSS field 'subject' vulnerabilities according to test case #012.
    """
    feedback_page = InputField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        feedback_page.enter_word_subject(cmd)
        feedback_page.click_on_the_submit_button()
        sleep(1)
        try:
            alert = Alert(browser)
            alert.accept()
            assert False, 'Finded alert'
        except NoAlertPresentException:
            assert True        
        browser.back()
        feedback_page.subject_clear()

def test_feedback_subject_tc017(browser):
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'subject' field
    according to test case #017.
    """
    feedback_page = InputField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.enter_word_subject(cmd[1])
        feedback_page.click_on_the_submit_button()
        sleep(1)
        assert cmd[0] not in browser.page_source
        browser.back()
        feedback_page.subject_clear()
        
def test_feedback_comments_tc012(browser):
    """
    Test function for XSS field 'comments' vulnerabilities according to test case #012.
    """
    feedback_page = InputField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        feedback_page.enter_word_comments(cmd)
        feedback_page.click_on_the_submit_button()
        sleep(1)
        try:
            alert = Alert(browser)
            alert.accept()
            assert False, 'Finded alert'
        except NoAlertPresentException:
            assert True        
        browser.back()
        feedback_page.comments_clear()

def test_feedback_comments_tc017(browser):
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'comments' field
    according to test case #017.
    """
    feedback_page = InputField(browser)
    feedback_page.go_to_site()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.enter_word_comments(cmd[1])
        feedback_page.click_on_the_submit_button()
        sleep(1)
        assert cmd[0] not in browser.page_source
        browser.back()
        feedback_page.comments_clear()