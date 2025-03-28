import abc
import logging
from framework.pageobject.Browser import BrowserCls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElementCls(abc.ABC):
    """
    The BaseElement class defines the basic methods for working with web page.
    
    Methods:
    -----------        
        click: 
            The function of clicking on an element.
        find_element:
            Search for an item on a page using a known locator.
    """
    
    def __init__(self):
        """
        Creating a constructor that accepts a locator. 
        And initiates an instance of the WebDriver from Browser Class.
        """
        logging.info(f'Initiating BasePage class')
        self.driver = BrowserCls().get_driver()
        logging.basicConfig(format='%(asctime)s - INFO - %(message)s', level=logging.INFO) 
    
    def click(self, locator):
        # Method for clicking element.
        logging.info(f'Executing a click() method of the BasePage class')
        self.find_element(locator).click()
    
    def find_element(self, locator, time=10):
        """
        Creating a method that searches for one element by locator and returns it.
    
        Returns:
        -----------
        WebElement: object
            Pointer to web element.
        """
        logging.info(f'Executing a find_element({locator}) method of the BasePage class')
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                    message=f"Can't find element by locator {locator}")
        
    
  