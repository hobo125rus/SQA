import logging
from framework.const.Constants import TestCaseConstants
from framework.pageobject.FeedbackPage import FeedbackPageCls

class InputFieldCls():
    """
    This class describes the basic methods of working with the elements responsible for the feedback area.
    
    Methods:
    -----------
        enter_word_name: 
            A method for implementing data entry in the name field.
        name_clear: 
            A method for clearing information in the name field.
        enter_word_email: 
            A method for implementing data entry in the email field.
        email_clear: 
            A method for clearing information in the email field.
        enter_word_subject: 
            A method for implementing data entry in the subject field.
        subject_clear: 
            A method for clearing information in the subject field.
        enter_word_comments: 
            A method for implementing data entry in the comments field.
        comments_clear: 
            A method for clearing information in the comments field.
        click_on_the_submit_button: 
            A method for implementing button clicks to perform a send information from feedback form.

    """
    
    @staticmethod
    def enter_word_name(word):
        """
        The method searches for an element of the name field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement name.
        """
        logging.info(f'Executing a enter_word_name() method of the InputField class')
        input_name_field = FeedbackPageCls(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_NAME)
        input_name_field.find_element()
        input_name_field.click()
        input_name_field.send_keys(word)
        return input_name_field
    
    @staticmethod
    def name_clear():
        """
        The method clears the name field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a name_clear() method of the InputField class')
        name_field = FeedbackPageCls(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_NAME)
        name_field.find_element()
        return name_field.clear()

    @staticmethod
    def enter_word_email(word):
        """
        The method searches for an element of the email field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement email.
        """
        logging.info(f'Executing a enter_word_email() method of the InputField class')
        input_email_field = FeedbackPageCls(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_EMAIL)
        input_email_field.find_element()
        input_email_field.click()
        input_email_field.send_keys(word)
        return input_email_field
    
    @staticmethod
    def email_clear():
        """
        The method clears the email field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a email_clear() method of the InputField class')
        email_field = FeedbackPageCls(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_EMAIL)
        email_field.find_element()
        return email_field.clear()
    
    @staticmethod
    def enter_word_subject(word):
        """
        The method searches for an element of the subject field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement subject.
        """
        logging.info(f'Executing a enter_word_subject() method of the InputField class')
        input_subject_field = FeedbackPageCls(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_SUBJECT)
        input_subject_field.find_element()
        input_subject_field.click()
        input_subject_field.send_keys(word)
        return input_subject_field
    
    @staticmethod
    def subject_clear():
        """
        The method clears the subject field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a subject_clear() method of the InputField class')
        subject_field = FeedbackPageCls(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_SUBJECT)
        subject_field.find_element()
        return subject_field.clear()
    
    @staticmethod
    def enter_word_comments(word):
        """
        The method searches for an element of the comments field, clicks 
        and enters the required word into the search.
        
        Returns:
        -----------
        WebElement: object
            Pointer to webelement comments.
        """
        logging.info(f'Executing a enter_word_comments() method of the InputField class')
        input_comments_field = FeedbackPageCls(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_COMMENTS)
        input_comments_field.find_element()
        input_comments_field.click()
        input_comments_field.send_keys(word)
        return input_comments_field
  
    @staticmethod  
    def comments_clear():
        """
        The method clears the comments field of values.
        
        Returns:
        -----------
            The result of the clear field.
        """
        logging.info(f'Executing a comments_clear() method of the InputField class')
        comments_field = FeedbackPageCls(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_COMMENTS)
        comments_field.find_element()
        return comments_field.clear()

    @staticmethod
    def click_on_the_submit_button():
        """
        The method searches for the element of the form button and clicks on it.
        
        Returns:
        -----------
            The result of the click.
        """
        logging.info(f'Executing a click_on_the_submit_button() method of the InputField class')
        click_on_the_submit = FeedbackPageCls(TestCaseConstants.LOCATOR_SUBMIT_BUTTON)
        click_on_the_submit.find_element()
        return click_on_the_submit.click()