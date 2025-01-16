#import pytest
from framework.pageobject.Browser import BrowserCls
from framework.pageobject.FeedbackPage import FeedbackPageCls
from framework.const.Constants import TestCaseConstants
from selenium.webdriver.support.wait import TimeoutException

#@pytest.mark.skip
def test_feedback_search_tc012():
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    feedback_page.input_search_text(TestCaseConstants.Test_XSS)
    feedback_page.click_on_the_search_button()
    try:
        test_page.alert_window()
        assert False, 'Finded alert'
    except TimeoutException: 
        assert True        
    test_page.back()
    feedback_page.search_clear()

#@pytest.mark.skip
def test_feedback_search_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'search' field
    according to test case #017.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.input_search_text(cmd[1])
        feedback_page.click_on_the_search_button()
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()
        feedback_page.search_clear()

#@pytest.mark.skip
def test_feedback_name_tc012():
    """
    Test function for XSS field 'name' vulnerabilities according to test case #012.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    feedback_page.input_name_text(TestCaseConstants.Test_XSS)
    feedback_page.click_on_the_submit_button()
    try:
        test_page.alert_window()
        assert False, 'Finded alert'
    except TimeoutException: 
        assert True        
    test_page.back()
    feedback_page.name_clear()

#@pytest.mark.skip
def test_feedback_name_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'name' field
    according to test case #017.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True 
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.input_name_text(cmd[1])
        feedback_page.click_on_the_submit_button()
        assert test_page.is_loaded("disclaimer") == True
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()        
        feedback_page.name_clear()  
 
#@pytest.mark.skip        
def test_feedback_email_tc012():
    """
    Test function for XSS field 'email' vulnerabilities according to test case #012.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        feedback_page.input_email_text(cmd)
        feedback_page.click_on_the_submit_button()
        try:
            test_page.alert_window()
            assert False, 'Finded alert'
        except TimeoutException:
            assert True  
        test_page.back()
        feedback_page.email_clear()

#@pytest.mark.skip
def test_feedback_email_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'email' field
    according to test case #017.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.input_email_text(cmd[1])
        feedback_page.click_on_the_submit_button()
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()
        feedback_page.email_clear()

#@pytest.mark.skip        
def test_feedback_subject_tc012():
    """
    Test function for XSS field 'subject' vulnerabilities according to test case #012.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        feedback_page.input_subject_text(cmd)
        feedback_page.click_on_the_submit_button()
        try:
            alert = test_page.alert_window()
            assert False, 'Finded alert'
        except TimeoutException:
            assert True        
        test_page.back()
        feedback_page.subject_clear()

#@pytest.mark.skip
def test_feedback_subject_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'subject' field
    according to test case #017.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.input_subject_text(cmd[1])
        feedback_page.click_on_the_submit_button()
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()
        feedback_page.subject_clear()

#@pytest.mark.skip        
def test_feedback_comments_tc012():
    """
    Test function for XSS field 'comments' vulnerabilities according to test case #012.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        feedback_page.input_comments_text(cmd)
        feedback_page.click_on_the_submit_button()
        try:
            test_page.alert_window()
            assert False, 'Finded alert'
        except TimeoutException:
            assert True        
        test_page.back()
        feedback_page.comments_clear()

#@pytest.mark.skip
def test_feedback_comments_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'comments' field
    according to test case #017.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    feedback_page = FeedbackPageCls() 
    assert feedback_page.is_title("Altoro Mutual") == True
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        feedback_page.input_comments_text(cmd[1])
        feedback_page.click_on_the_submit_button()
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()
        feedback_page.comments_clear()
    test_page.quit()
