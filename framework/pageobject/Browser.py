import logging
from framework.pageobject.Singleton import MetaSingleton
from framework.pageobject.BrowserFactory import BrowserFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.remote.errorhandler import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

logging.basicConfig(format='%(asctime)s - INFO - %(message)s', level=logging.INFO)

class BrowserCls(metaclass=MetaSingleton):
    """
    Performing initialization for WebDriver and base methods for working with WebDriver.
    
    Methods:
    -----------
        back:
            A method for returning to the previous page.
        get_driver:
            A method for returning pointer to the WebDriver.
        go_to_url:
            The method of going to the page passed to the class as an argument.
        is_loaded:
            The method of checking page element loading.
        page_source:
            The method of displaying the page content.
        quit:
            The method of exiting the WebDriver interface.
        alert_window:
            The method implements the function of checking exist alert window.
    """
        
    def __init__(self, url, browser_type):
        """
        Creating a constructor that initiates an instance of the WebDriver.
        Specify the url that will be used to open the page.
        """
        self.driver = BrowserFactory.set_browser_type(browser_type)
        self.url = url
        logging.info(f'Initiating Browser class')    

    def back(self):
        # The method calls the back function from WebDriver.
        logging.info(f'Executing a back() method of the Browser class')
        self.driver.back()
    
    def get_driver(self):
        # The method return the pointer to WebDriver.
        logging.info(f'Executing a get_driver() method of the Browser class')
        return self.driver

    def go_to_url(self):
        """
        The method calls the get function from WebDriver. 
        The method allows to go to the specified url.
        """
        logging.info(f'Executing a go_to_url() method of the Browser class')
        self.driver.get(self.url)
    
    def is_loaded(self, class_name, timeout=4):
        # The method implements the function of checking the page element load.
        logging.info(f'Executing an is_loaded() method of the Browser class')
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, class_name))
            WebDriverWait(self.driver, timeout).until(element_present)
            logging.info(f'Page loaded')
            return True
        except TimeoutException:
            logging.info(f'Timed out waiting for page to load')
            return False
    
    def page_source(self):
        # The method returns the contents of the page.
        logging.info(f'Executing a page_source() method of the Browser class')
        return self.driver.page_source
    
    def quit(self):
        # The method quit from WebDriver.
        logging.info(f'Executing a quit() method of the Browser class')
        self.driver.quit()
    
    def alert_window(self, timeout=3):
        """
        The method implements the function of checking exist alert window.
        Returns an exception is occured if alert is not found.
        """
        logging.info(f'Executing an alert_window() method of the Browser class')
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = Alert(self.driver)
            logging.info("Alert is finded")
            alert.accept()
        except NoAlertPresentException:
            logging.info("Alert is missing")        
