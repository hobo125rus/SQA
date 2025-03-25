class TestCaseConstants(object):
    """
    Constants used in testing, as well as the testing URL.
    
    Test_URL: The address of the page where the test is being performed.
    Test_PageTitle: The title of the page where the test is being performed.
    Test_PageIsLoadFlag: The text that defines the end of page loading. 
    Test_COMMANDs: Commands to search for vulnerabilities according to test case #017.
        An enumeration of checks in the form of an array consisting of tuples. 
        Where the first tuple element is one value of the expected result of execution 
        of the command, which is the second tuple element.
    Test_XSS: Commands to search for vulnerabilities according to test case #012.
    """
    Test_URL = 'http://testfire.net/feedback.jsp'
    Test_PageTitle = 'Altoro Mutual'
    Test_PageIsLoadFlag = 'disclaimer'
    Test_PageIsOpenFlag = 'Feedback'
    Test_PageIsOpenConditionTag = 'h1'
    
    Test_COMMANDs   = [('total','/bin/ls -la|'), ('icrosoft','cmd.exe')]
    Test_XSS        = ['<script>alert("aaa!!!")</script>']
    
    
