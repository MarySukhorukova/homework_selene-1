from selene import be, have
from selene.support.shared import browser
import os


def test_filling_and_submitting_form(browser_base_url):
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
    browser.element('#subjectsInput').type('Dark Arts')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath('files/Pytest_logo.svg.png'))
    browser.element('#currentAddress').set_value('Hogwarts').press_enter()
    browser.element('#react-select-3-input').send_keys('Haryana').press_enter()
    browser.element('#react-select-4-input').send_keys('Karnal').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Harry Potter' and 'hp@test.com' and 'Male' and '0123456789' and '31 July,1980'
                                               and 'Dark Arts' and 'Sports' and 'Pytest_logo.svg.png' and 'Hogwarts'))
