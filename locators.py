from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SEARCH_BUTTON = (By.XPATH, '//input[@value="Go"')
    SUBMIT_BUTTON = (By.NAME, 'Submit')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass