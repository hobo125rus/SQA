from basepage import BasePage
from selenium.webdriver.common.by import By

class FeedbackLocators:
    """
    Creating the FeedbackLocators class. It is used only for storing locators.
    The class describes the locators:
    LOCATOR_INPUT_TEXT_FIELD_NAME: Locator for searching the 'name' field. 
    LOCATOR_INPUT_TEXT_FIELD_EMAIL: Locator for searching the 'email' field.
    LOCATOR_INPUT_TEXT_FIELD_SUBJECT: Locator for searching the 'subject' field.
    LOCATOR_INPUT_TEXT_FIELD_COMMENTS: Locator for searching the 'comments' field.
    LOCATOR_SUBMIT_BUTTON: Locator for searching the submit button in the form.
    
    LOCATOR_SEARCH_FIELD: Locator for searching the search input field.
    LOCATOR_SEARCH_BUTTON: Locator for searching the serach button.
    """
    LOCATOR_INPUT_TEXT_FIELD_NAME = (By.NAME, 'name')
    LOCATOR_INPUT_TEXT_FIELD_EMAIL = (By.NAME, 'email_addr')
    LOCATOR_INPUT_TEXT_FIELD_SUBJECT = (By.NAME, 'subject')
    LOCATOR_INPUT_TEXT_FIELD_COMMENTS = (By.NAME, 'comments')
    LOCATOR_SUBMIT_BUTTON = (By.NAME, 'submit')
    
    LOCATOR_SEARCH_FIELD = (By.NAME, 'query')
    LOCATOR_SEARCH_BUTTON = (By.XPATH, '//input[@value="Go"]')

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
        search_field = self.find_element(FeedbackLocators.LOCATOR_SEARCH_FIELD)
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
        return self.find_element(FeedbackLocators.LOCATOR_SEARCH_BUTTON,time=2).click()
    
    def search_clear(self):
        """
        The method clears the search bar field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        search_field = self.find_element(FeedbackLocators.LOCATOR_SEARCH_FIELD)
        return search_field.clear()
    
class InputField(BasePage):

    def enter_word_name(self, word):
        """
        The method searches for an element of the name field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement name.
        """
        input_name_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_NAME)
        input_name_field.click()
        input_name_field.send_keys(word)
        return input_name_field
    
    def name_clear(self):
        """
        The method clears the name field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        name_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_NAME)
        return name_field.clear()

    def enter_word_email(self, word):
        """
        The method searches for an element of the email field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement email.
        """
        input_email_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_EMAIL)
        input_email_field.click()
        input_email_field.send_keys(word)
        return input_email_field
    
    def email_clear(self):
        """
        The method clears the email field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        email_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_EMAIL)
        return email_field.clear()
    
    def enter_word_subject(self, word):
        """
        The method searches for an element of the subject field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement subject.
        """
        input_subject_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_SUBJECT)
        input_subject_field.click()
        input_subject_field.send_keys(word)
        return input_subject_field
    
    def subject_clear(self):
        """
        The method clears the subject field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        subject_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_SUBJECT)
        return subject_field.clear()
    
    def enter_word_comments(self, word):
        """
        The method searches for an element of the comments field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement comments.
        """
        input_comments_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_COMMENTS)
        input_comments_field.click()
        input_comments_field.send_keys(word)
        return input_comments_field
    
    def comments_clear(self):
        """
        The method clears the comments field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        comments_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_COMMENTS)
        return comments_field.clear()

    def click_on_the_submit_button(self):
        """
        The method searches for the element of the form button and clicks on it.
        
        Returns:
        -----------
            The result of the click.
        """
        return self.find_element(FeedbackLocators.LOCATOR_SUBMIT_BUTTON,time=2).click()