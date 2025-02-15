import abc
import logging
from framework.pageobject.Browser import BrowserCls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(format='%(asctime)s - INFO - %(message)s', level=logging.INFO)

class BasePageCls(abc.ABC):
    """
    The BasePage class defines the basic methods for working with web page.
    
    Methods:
    -----------
        __iter__:
            An abstract method for demonstrating the operation of the abc module.        
        is_title:
            Method for checking if the specified value is in the page header.
    """
    
    def __init__(self):
        """
        Creating a constructor that accepts a locator. 
        And initiates an instance of the WebDriver from Browser Class.
        """
        logging.info(f'Initiating BasePage class')
        self.driver = BrowserCls().get_driver()
    
    @abc.abstractmethod
    def __iter__(self):
        while False:
            yield None    
        
    def is_title(self, title):
        """
        The method implements the function of checking the page title. 
        Returns a boolean value if there is a title.
        """
        logging.info(f'Executing a is_title() method of the BasePage class')
        return title in self.driver.title