import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_base_url():
    browser.config.base_url = 'https://demoqa.com'

