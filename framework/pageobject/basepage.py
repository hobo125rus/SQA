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
        find_element:
            Search for an item on a page using a known locator.
        click: 
            The function of clicking on an element.
        clear: 
            The function of clearing on an element.
        send_keys: 
            The function of send keys to an element.
        is_title:
            Method for checking if the specified value is in the page header.
        input_textbox:
            A universal method for transferring text to a given input field.
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
        
    def click(self, locator):
        # Method for clicking element.
        logging.info(f'Executing a click() method of the BasePage class')
        self.find_element(locator).click()
    
    def clear(self, locator):
        # Method for clearing element.
        logging.info(f'Executing a clear() method of the BasePage class')
        self.find_element(locator).clear()
    
    def send_keys(self, text, locator):
        # Method for printing text to element.
        logging.info(f'Executing a send_keys() method of the BasePage class')
        self.find_element(locator).send_keys(text)
        
    def is_title(self, title):
        """
        The method implements the function of checking the page title. 
        Returns a boolean value if there is a title.
        """
        logging.info(f'Executing a is_title() method of the BasePage class')
        return title in self.driver.title
    
    def input_textbox(self, text, locator):
        """
        The method searches for an element of the any text box, clicks 
        and enters the required text into the field.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement text field.
        """
        logging.info(f'Executing a input_textbox() method of the BasePage class')
        self.click(locator)
        self.send_keys(text, locator)
        return self