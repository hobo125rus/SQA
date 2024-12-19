from const.constants import TestCaseConstants

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
        input_name_field = self.find_element(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_NAME)
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
        name_field = self.find_element(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_NAME)
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
        input_email_field = self.find_element(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_EMAIL)
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
        email_field = self.find_element(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_EMAIL)
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
        input_subject_field = self.find_element(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_SUBJECT)
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
        subject_field = self.find_element(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_SUBJECT)
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
        input_comments_field = self.find_element(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_COMMENTS)
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
        comments_field = self.find_element(TestCaseConstants.LOCATOR_INPUT_TEXT_FIELD_COMMENTS)
        return comments_field.clear()

    def click_on_the_submit_button(self):
        """
        The method searches for the element of the form button and clicks on it.
        
        Returns:
        -----------
            The result of the click.
        """
        return self.find_element(TestCaseConstants.LOCATOR_SUBMIT_BUTTON,time=2).click()