import logging
from framework.pageobject.BasePage import BasePageCls
from framework.pageobject.elements.Button import ButtonCls
from framework.pageobject.elements.Input import InputCls
from framework.const.Constants import TestCaseConstants
class FeedbackPageCls(BasePageCls):
    """
    This class describes the basic methods of working with the feedback page.
    
    Methods:
    -----------
        __iter__:
            An abstract method for demonstrating the operation of the abc module. 
        input_search_text: 
            A method for implementing data entry in the search bar.
        click_on_the_search_button: 
            A method for implementing button clicks to perform a search..
        search_clear: 
            A method for clearing information in the search field.
        input_name_text: 
            A method for implementing data entry in the name field.
        name_clear: 
            A method for clearing information in the name field.
        input_email_text: 
            A method for implementing data entry in the email field.
        email_clear: 
            A method for clearing information in the email field.
        input_subject_text: 
            A method for implementing data entry in the subject field.
        subject_clear: 
            A method for clearing information in the subject field.
        input_comments_text: 
            A method for implementing data entry in the comments field.
        comments_clear: 
            A method for clearing information in the comments field.
        click_on_the_submit_button: 
            A method for implementing button clicks to perform a send information from feedback form.
    """
    
    def __iter__(self):
        while False:
            yield None
    
    def input_search_text(self, text):
        """
        The method searches for an element of the any text box, clicks 
        and enters the required text into the field.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement text field.
        """
        logging.info(f'Executing a input_search_text() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_SEARCH_FIELD
        input = InputCls()
        input.input_textbox(text,locator)
    
    def click_on_the_search_button(self):
        """
        The method searches for the element of the search button and clicks on it.
        
        Returns:
        -----------
            The result of the click.
        """
        logging.info(f'Executing a click_on_the_search_button() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_SEARCH_BUTTON
        button = ButtonCls()
        button.click(locator)
    
    def search_clear(self):
        """
        The method clears the search bar field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a search_clear() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_SEARCH_FIELD
        input = InputCls()
        input.clear(locator)
    
    def input_name_text(self, text):
        """
        The method searches for an element of the name field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement name.
        """
        logging.info(f'Executing a input_name_text() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_NAME
        input = InputCls()
        input.input_textbox(text,locator)
    
    def name_clear(self):
        """
        The method clears the name field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a name_clear() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_SEARCH_FIELD
        input = InputCls()
        input.clear(locator)

    def input_email_text(self, text):
        """
        The method searches for an element of the email field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement email.
        """
        logging.info(f'Executing a input_email_text() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_EMAIL
        input = InputCls()
        input.input_textbox(text,locator)
    
    def email_clear(self):
        """
        The method clears the email field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a email_clear() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_EMAIL
        input = InputCls()
        input.clear(locator)
    
    def input_subject_text(self, text):
        """
        The method searches for an element of the subject field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement subject.
        """
        logging.info(f'Executing a input_subject_text() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_SUBJECT
        input = InputCls()
        input.input_textbox(text,locator)
    
    def subject_clear(self):
        """
        The method clears the subject field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a subject_clear() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_SUBJECT
        input = InputCls()
        input.clear(locator)
    
    def input_comments_text(self, text):
        """
        The method searches for an element of the comments field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement comments.
        """
        logging.info(f'Executing a input_comments_text() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_COMMENTS
        input = InputCls()
        input.input_textbox(text,locator)
  
    def comments_clear(self):
        """
        The method clears the comments field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a comments_clear() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_COMMENTS
        input = InputCls()
        input.clear(locator)

    def click_on_the_submit_button(self):
        """
        The method searches for the element of the form button and clicks on it.
        
        Returns:
        -----------
            The result of the click.
        """
        logging.info(f'Executing a click_on_the_submit_button() method of the FeedbackPage class')
        locator = TestCaseConstants.LOCATOR_SUBMIT_BUTTON
        button = ButtonCls()
        button.click(locator)