from framework.pageobject.Browser import BrowserCls
from framework.pageobject.InputField import InputFieldCls
from framework.pageobject.SearchField import SearchFieldCls
from framework.const.Constants import TestCaseConstants
from selenium.webdriver.support.wait import TimeoutException

#@pytest.mark.skip
def test_feedback_search_tc012():
    """
    Test function for XSS field 'search' vulnerabilities according to test case #012.
    """
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    sfc = SearchFieldCls()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        sfc.enter_word_search(cmd)
        sfc.click_on_the_search_button()
        try:
            test_page.alert_window()
            assert False, 'Finded alert'
        except TimeoutException: 
            assert True        
        test_page.back()
        sfc.search_clear()

#@pytest.mark.skip
def test_feedback_search_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'search' field
    according to test case #017.
    """
   
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    sfc = SearchFieldCls()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        sfc.enter_word_search(cmd[1])
        sfc.click_on_the_search_button()
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()
        sfc.search_clear()

#@pytest.mark.skip
def test_feedback_name_tc012():
    """
    Test function for XSS field 'name' vulnerabilities according to test case #012.
    """
    
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    ifc = InputFieldCls()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        ifc.enter_word_name(cmd)
        ifc.click_on_the_submit_button()
        try:
            test_page.alert_window()
            assert False, 'Finded alert'
        except TimeoutException:
            assert True        
        test_page.go_to_url()
        ifc.name_clear()

#@pytest.mark.skip
def test_feedback_name_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'name' field
    according to test case #017.
    """
    
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    ifc = InputFieldCls()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        ifc.enter_word_name(cmd[1])
        ifc.click_on_the_submit_button()
        assert test_page.is_loaded("disclaimer") == True
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()        
        ifc.name_clear()  
 
#@pytest.mark.skip        
def test_feedback_email_tc012():
    """
    Test function for XSS field 'email' vulnerabilities according to test case #012.
    """
  
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    ifc = InputFieldCls()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        ifc.enter_word_email(cmd)
        ifc.click_on_the_submit_button()
        try:
            test_page.alert_window()
            assert False, 'Finded alert'
        except TimeoutException:
            assert True  
        test_page.back()
        ifc.email_clear()

#@pytest.mark.skip
def test_feedback_email_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'email' field
    according to test case #017.
    """
    
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    ifc = InputFieldCls()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        ifc.enter_word_email(cmd[1])
        ifc.click_on_the_submit_button()
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()
        ifc.email_clear()

#@pytest.mark.skip        
def test_feedback_subject_tc012():
    """
    Test function for XSS field 'subject' vulnerabilities according to test case #012.
    """
    
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    ifc = InputFieldCls()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        ifc.enter_word_subject(cmd)
        ifc.click_on_the_submit_button()
        try:
            alert = test_page.alert_window()
            assert False, 'Finded alert'
        except TimeoutException:
            assert True        
        test_page.back()
        ifc.subject_clear()

#@pytest.mark.skip
def test_feedback_subject_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'subject' field
    according to test case #017.
    """
  
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    ifc = InputFieldCls()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        ifc.enter_word_subject(cmd[1])
        ifc.click_on_the_submit_button()
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()
        ifc.subject_clear()

#@pytest.mark.skip        
def test_feedback_comments_tc012():
    """
    Test function for XSS field 'comments' vulnerabilities according to test case #012.
    """
  
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    ifc = InputFieldCls()
    tcconstants = TestCaseConstants.Test_XSS
    for cmd in tcconstants:
        ifc.enter_word_comments(cmd)
        ifc.click_on_the_submit_button()
        try:
            test_page.alert_window()
            assert False, 'Finded alert'
        except TimeoutException:
            assert True        
        test_page.back()
        ifc.comments_clear()

#@pytest.mark.skip
def test_feedback_comments_tc017():
    """
    Vulnerability testing function for OS command injection vulnerabilities of 'comments' field
    according to test case #017.
    """
    
    test_page = BrowserCls("https://testfire.net/feedback.jsp")
    test_page.go_to_url()
    test_page.is_loaded("disclaimer")
    assert test_page.is_title("Altoro Mutual") == True
    ifc = InputFieldCls()
    tcconstants = TestCaseConstants.Test_COMMANDs
    for cmd in tcconstants:
        ifc.enter_word_comments(cmd[1])
        ifc.click_on_the_submit_button()
        assert cmd[0] not in test_page.page_source()
        test_page.go_to_url()
        ifc.comments_clear()
    test_page.quit()
