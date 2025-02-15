import logging
from framework.pageobject.elements.BaseElement import BaseElementCls

class ButtonCls(BaseElementCls):
    """
    The Button class defines the basic methods for working with button on web page.
    
    Methods:
    -----------
        click: 
            The function of clicking on an element.
    """
    
    def click(self, locator):
        # Method for clicking element.
        logging.info(f'Executing a click() method of the Button class')
        self.find_element(locator).click()