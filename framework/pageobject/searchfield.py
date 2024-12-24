import logging
from framework.const.Constants import TestCaseConstants
from framework.pageobject.FeedbackPage import FeedbackPageCls

class SearchFieldCls():
    """
    This class describes the basic methods of working with the elements responsible for the search area.
    
    Methods:
    -----------
        enter_word_search: 
            A method for implementing data entry in the search bar.
        click_on_the_search_button: 
            A method for implementing button clicks to perform a search..
        search_clear: 
            A method for clearing information in the search field.
    """
    @staticmethod
    def enter_word_search(word):
        """
        The method searches for an element of the search bar, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement search bar.
        """
        logging.info(f'Executing a enter_word_search() method of the SearchField class')
        search_field = FeedbackPageCls(TestCaseConstants.LOCATOR_SEARCH_FIELD)
        search_field.find_element()
        search_field.click()
        search_field.send_keys(word)
        return search_field

    @staticmethod
    def click_on_the_search_button():
        """
        The method searches for the element of the search button and clicks on it.
        
        Returns:
        -----------
            The result of the click.
        """
        logging.info(f'Executing a click_on_the_search_button() method of the SearchField class')
        search_button = FeedbackPageCls(TestCaseConstants.LOCATOR_SEARCH_BUTTON)
        search_button.find_element()
        return search_button.click()
    
    @staticmethod
    def search_clear():
        """
        The method clears the search bar field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a search_clear() method of the SearchField class')
        search_field = FeedbackPageCls(TestCaseConstants.LOCATOR_SEARCH_FIELD)
        search_field.find_element()
        return search_field.clear()