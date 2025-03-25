import pytest
from framework.const.Constants import TestCaseConstants

def pytest_addoption(parser):
    parser.addoption(
        '--base-url', action='store', default=TestCaseConstants.Test_URL, help='Base URL for the tests.'
    )
    parser.addoption(
        '--browser-type', action='store', default="safari", help='Browser type for the tests.'
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption('--base-url')

@pytest.fixture
def browser_type(request):
    return request.config.getoption('--browser-type')


    