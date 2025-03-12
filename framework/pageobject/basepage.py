import abc
import logging
from framework.pageobject.Browser import BrowserCls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framework.const.Constants import TestCaseConstants

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
        is_opened:
            Method for checking if the page is open.    
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
        if(self.is_opened(TestCaseConstants.Test_PageIsOpenConditionTag, TestCaseConstants.Test_PageIsOpenFlag)):
            logging.info(f'Executing a is_title() method of the BasePage class')
            return title in self.driver.title
        return False
    
    def is_opened(self, search_condition, page_flag, timeout=4):
        """
        The method implements the function of checking is page opened. 
        Returns a boolean value if there is a open.
        """
        try:
            page_opened = EC.presence_of_element_located((By.TAG_NAME, search_condition))
            if(WebDriverWait(self.driver, timeout).until(page_opened).text == page_flag):
                logging.info(f'Page is opened')
                return True
        except TimeoutException:
            logging.info(f'Timed out waiting for page to open')
            return False