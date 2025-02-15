import logging
from framework.pageobject.elements.BaseElement import BaseElementCls

#logging.basicConfig(format='%(asctime)s - INFO - %(message)s', level=logging.INFO)

class InputCls(BaseElementCls):
    """
    The Input class defines the basic methods for working with button on web page.
    
    Methods:
    -----------      
        clear: 
            The function of clearing on an element.
        send_keys: 
            The function of send keys to an element.
        input_textbox:
            A universal method for transferring text to a given input field.
    """
    
    # def __init__(self):
    #     """
    #     Creating a constructor that accepts a locator. 
    #     And initiates an instance of the WebDriver from Browser Class.
    #     """
    #     logging.info(f'Initiating Input class')

    def clear(self, locator):
        # Method for clearing element.
        logging.info(f'Executing a clear() method of the Input class')
        self.find_element(locator).clear()
    
    def click(self, locator):
        # Method for clicking element.
        logging.info(f'Executing a click() method of the Button class')
        self.find_element(locator).click()
    
    def send_keys(self, text, locator):
        # Method for printing text to element.
        logging.info(f'Executing a send_keys() method of the Input class')
        self.find_element(locator).send_keys(text)
        
    def input_textbox(self, text, locator):
        """
        The method searches for an element of the any text box, clicks 
        and enters the required text into the field.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement text field.
        """
        logging.info(f'Executing a input_textbox() method of the Input class')
        self.click(locator)
        self.send_keys(text, locator)
        return self