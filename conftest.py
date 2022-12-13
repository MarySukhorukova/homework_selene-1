import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def open_practice_form():
    form_url = 'https://demoqa.com/automation-practice-form'
    browser.open(form_url)

