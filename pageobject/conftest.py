import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    """
    Performing initialization for WebDriver. A fixture is used in the description. 
    Fixtures in pytest are functions that have their own frequency of execution.
    With the help of a fixture, you can prepare the initial state of the system for testing.
    We mark the function with its decorator @pytest.fixture and passing the scope parameter 
    with the session value. This means that this fixture function will be executed 
    only 1 time per test session.
    """
    driver = webdriver.Safari()
    yield driver
    driver.quit()