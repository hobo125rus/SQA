from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from const.constants import TestCaseConstants

class BasePage:
    """
    The BasePage class defines the basic methods for working with WebDriver.
    """
    def __init__(self, driver):
        """
        Creating a constructor that accepts a webdriver driver instance. 
        Specify the base_url that will be used to open the page.
        """
        self.driver = driver
        self.base_url = TestCaseConstants.Test_URL

    def find_element(self, locator,time=10):
        """
        Creating a find_element method that searches for one element and returns it.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement.
        """
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        """
        The method calls the get function from WebDriver. 
        The method allows to go to the specified page.
        
        Returns:
        -----------
        driver: object
            Pointer to webdriver.
        """
        return self.driver.get(self.base_url)