class TestCaseConstants(object):
    """
    Constants used in testing, as well as the testing URL.
    
    Test_ URL: The address of the page where the test is being performed.
    Test_COMMANDs: Commands to search for vulnerabilities according to test case #017.
        An enumeration of checks in the form of an array consisting of tuples. 
        Where the first tuple element is one value of the expected result of execution 
        of the command, which is the second tuple element.
    Test_XSS: Commands to search for vulnerabilities according to test case #012.
    """
    Test_URL = 'http://testfire.net/feedback.jsp'
    
    Test_COMMANDs   = [('total','/bin/ls -la|'), ('icrosoft','cmd.exe')]
    Test_XSS        = ['<script>alert("aaa!!!")</script>']
    
    """
    Creating the FeedbackLocators class. It is used only for storing locators.
    The class describes the locators:
    LOCATOR_INPUT_TEXT_FIELD_NAME: Locator for searching the 'name' field. 
    LOCATOR_INPUT_TEXT_FIELD_EMAIL: Locator for searching the 'email' field.
    LOCATOR_INPUT_TEXT_FIELD_SUBJECT: Locator for searching the 'subject' field.
    LOCATOR_INPUT_TEXT_FIELD_COMMENTS: Locator for searching the 'comments' field.
    LOCATOR_SUBMIT_BUTTON: Locator for searching the submit button in the form.
    
    LOCATOR_SEARCH_FIELD: Locator for searching the search input field.
    LOCATOR_SEARCH_BUTTON: Locator for searching the serach button.
    """
    LOCATOR_INPUT_TEXT_FIELD_NAME = (By.NAME, 'name')
    LOCATOR_INPUT_TEXT_FIELD_EMAIL = (By.NAME, 'email_addr')
    LOCATOR_INPUT_TEXT_FIELD_SUBJECT = (By.NAME, 'subject')
    LOCATOR_INPUT_TEXT_FIELD_COMMENTS = (By.NAME, 'comments')
    LOCATOR_SUBMIT_BUTTON = (By.NAME, 'submit')
    
    LOCATOR_SEARCH_FIELD = (By.NAME, 'query')
    LOCATOR_SEARCH_BUTTON = (By.XPATH, '//input[@value="Go"]')
