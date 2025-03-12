import logging
from framework.pageobject.elements.BaseElement import BaseElementCls

class InputCls(BaseElementCls):
    """
    The Input class defines the basic methods for working with input fields on web page.
    
    Methods:
    -----------      
        clear: 
            The function of clearing on an element.
        send_keys: 
            The function of send keys to an element.
        input_textbox:
            A universal method for transferring text to a given input field.
    """

    def clear(self, locator):
        # Method for clearing element.
        logging.info(f'Executing a clear() method of the Input class')
        self.find_element(locator).clear()
    
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