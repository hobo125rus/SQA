from const.constants import TestCaseConstants

class SearchField(BasePage):

    def enter_word_search(self, word):
        """
        The method searches for an element of the search bar, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement search bar.
        """
        search_field = self.find_element(TestCaseConstants.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        """
        The method searches for the element of the search button and clicks on it.
        
        Returns:
        -----------
            The result of the click.
        """
        return self.find_element(TestCaseConstants.LOCATOR_SEARCH_BUTTON,time=2).click()
    
    def search_clear(self):
        """
        The method clears the search bar field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        search_field = self.find_element(TestCaseConstants.LOCATOR_SEARCH_FIELD)
        return search_field.clear()