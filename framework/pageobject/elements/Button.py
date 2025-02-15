import logging
from framework.pageobject.elements.BaseElement import BaseElementCls

#logging.basicConfig(format='%(asctime)s - INFO - %(message)s', level=logging.INFO)

class ButtonCls(BaseElementCls):
    """
    The Button class defines the basic methods for working with button on web page.
    
    Methods:
    -----------
        __iter__:
            An abstract method for demonstrating the operation of the abc module.        
        find_element:
            Search for an item on a page using a known locator.
        click: 
            The function of clicking on an element.
    """
    
    # def __init__(self):
    #     """
    #     Creating a constructor that accepts a locator. 
    #     And initiates an instance of the WebDriver from Browser Class.
    #     """
    #     logging.info(f'Initiating Button class')
    
    def click(self, locator):
        # Method for clicking element.
        logging.info(f'Executing a click() method of the Button class')
        self.find_element(locator).click()