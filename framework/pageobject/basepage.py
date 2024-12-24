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
        find_element:
            Search for an item on a page using a known locator.
        click: 
            The function of clicking on an element.
        clear: 
            The function of clearing on an element.
        send_keys: 
            The function of send keys to an element.
    """
    
    def __init__(self, locator):
        """
        Creating a constructor that accepts a locator. 
        And initiates an instance of the WebDriver from Browser Class.
        """
        logging.info(f'Initiating BasePage class')
        self.driver = BrowserCls().get_driver()
        self.locator = locator        
    
    def find_element(self,time=10):
        """
        Creating a method that searches for one element by locator and returns it.
    
        Returns:
        -----------
        WebElement: object
            Pointer to web element.
        """
        logging.info(f'Executing a find_element({self.locator}) method of the BasePage class')
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(self.locator),
                                                    message=f"Can't find element by locator {self.locator}")
        
    def click(self):
        # Method for clicking element.
        logging.info(f'Executing a click() method of the BasePage class')
        self.find_element().click()
    
    def clear(self):
        # Method for clearing element.
        logging.info(f'Executing a clear() method of the BasePage class')
        self.find_element().clear()
    
    def send_keys(self, text):
        # Method for printing text to element.
        logging.info(f'Executing a send_keys() method of the BasePage class')
        self.find_element().send_keys(text)