from selene import be, have
from selene.support.shared import browser
import os


def test_filling_and_submitting_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Harry')
    browser.element('#lastName').type('Potter')
    browser.element('#userEmail').type('hp@test.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1980"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), 'files', 'Pytest_logo.svg.png')))
    browser.element('#currentAddress').type('Hogwarts')
    browser.element('#react-select-3-input').send_keys('Haryana').press_enter()
    browser.element('#react-select-4-input').send_keys('Karnal').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Harry Potter'))
    browser.element('.table').should(have.text('hp@test.com'))
    browser.element('.table').should(have.text('Male'))
    browser.element('.table').should(have.text('0123456789'))
    browser.element('.table').should(have.text('31 July,1980'))
    browser.element('.table').should(have.text('Arts'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('Pytest_logo.svg.png'))
    browser.element('.table').should(have.text('Hogwarts'))
    browser.element('.table').should(have.text('Haryana Karnal'))
