import pytest
from framework.pageobject.Singleton import MetaSingleton
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#@pytest.fixture(scope="session")
class BrowserCls(metaclass=MetaSingleton):
    """
    Performing initialization for WebDriver. A fixture is used in the description. 
    Fixtures in pytest are functions that have their own frequency of execution.
    With the help of a fixture, you can prepare the initial state of the system for testing.
    We mark the function with its decorator @pytest.fixture and passing the scope parameter 
    with the session value. This means that this fixture function will be executed 
    only 1 time per test session.
    """
        
    def __init__(self, url):
        """
        Creating a constructor that initiates an instance of the WebDriver.
        Specify the url that will be used to open the page.
        """
        self.driver = webdriver.Safari()
        self.url = url
        # yield self.driver
        # self.driver.quit()        

    def back(self):
        # The method calls the back function from WebDriver.
        self.driver.back()

    # def get_browser(self):
    #     return BrowserCls()
    
    def get_driver(self):
        # The method return the pointer to WebDriver.
        return self.driver

    def go_to_url(self):
        """
        The method calls the get function from WebDriver. 
        The method allows to go to the specified url.
        """
        self.driver.get(self.url)
    
    def is_loaded(self, locator, timeout=3):
        # The method implements the function of checking the page load.
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, locator))
            WebDriverWait(self.driver, timeout).until(element_present)
            print("Page loaded")
        except TimeoutException:
            print("Timed out waiting for page to load")
        # finally:
            #print("Page loaded")
    
    def is_title(self, title):
        """
        The method implements the function of checking the page title. 
        Returns a boolean value if there is a title.
        """
        return title in self.driver.title
    
    def page_source(self):
        # The method returns the contents of the page.
        return self.driver.page_source
    
    def quit(self):
        # The method quit from WebDriver.
        self.driver.quit()
        
