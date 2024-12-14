from basepage import BasePage
from selenium.webdriver.common.by import By

class FeedbackLocators:
    LOCATOR_INPUT_TEXT_FIELD_NAME = (By.NAME, 'name')
    LOCATOR_INPUT_TEXT_FIELD_EMAIL = (By.NAME, 'email_addr')
    LOCATOR_INPUT_TEXT_FIELD_SUBJECT = (By.NAME, 'subject')
    LOCATOR_INPUT_TEXT_FIELD_COMMENTS = (By.NAME, 'comments')
    LOCATOR_SUBMIT_BUTTON = (By.NAME, 'submit')
    
    LOCATOR_SEARCH_FIELD = (By.NAME, 'query')
    LOCATOR_SEARCH_BUTTON = (By.XPATH, '//input[@value="Go"]')

class SearchField(BasePage):

    def enter_word_search(self, word):
        search_field = self.find_element(FeedbackLocators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(FeedbackLocators.LOCATOR_SEARCH_BUTTON,time=2).click()
    
    def search_clear(self):
        search_field = self.find_element(FeedbackLocators.LOCATOR_SEARCH_FIELD)
        return search_field.clear()
    
class InputField(BasePage):

    def enter_word_name(self, word):
        input_name_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_NAME)
        input_name_field.click()
        input_name_field.send_keys(word)
        return input_name_field
    
    def name_clear(self):
        name_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_NAME)
        return name_field.clear()

    def enter_word_email(self, word):
        input_email_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_EMAIL)
        input_email_field.click()
        input_email_field.send_keys(word)
        return input_email_field
    
    def email_clear(self):
        email_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_EMAIL)
        return email_field.clear()
    
    def enter_word_subject(self, word):
        input_subject_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_SUBJECT)
        input_subject_field.click()
        input_subject_field.send_keys(word)
        return input_subject_field
    
    def subject_clear(self):
        subject_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_SUBJECT)
        return subject_field.clear()
    
    def enter_word_comments(self, word):
        input_comments_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_COMMENTS)
        input_comments_field.click()
        input_comments_field.send_keys(word)
        return input_comments_field
    
    def comments_clear(self):
        comments_field = self.find_element(FeedbackLocators.LOCATOR_INPUT_TEXT_FIELD_COMMENTS)
        return comments_field.clear()

    def click_on_the_submit_button(self):
        return self.find_element(FeedbackLocators.LOCATOR_SUBMIT_BUTTON,time=2).click()