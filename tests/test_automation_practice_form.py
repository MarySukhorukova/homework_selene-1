import time

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
    time.sleep(5)
    browser.element('#uploadPicture').set_value(os.path.abspath('files/Pytest_logo.svg.png'))
    time.sleep(5)
    browser.element('#currentAddress').set_value('Hogwarts').press_enter()
    time.sleep(5)
    browser.element('#react-select-3-input').send_keys('Haryana').press_enter()
    time.sleep(5)
    browser.element('#react-select-4-input').send_keys('Karnal').press_enter()
    time.sleep(5)
    browser.element('#submit').press_enter()
    time.sleep(5)
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    time.sleep(5)
    browser.element('.table').should(have.text('Harry Potter' and 'hp@test.com' and 'Male' and '0123456789' and '31 July,1980'
                                               and 'Arts' and 'Sports' and 'Pytest_logo.svg.png' and 'Hogwarts'))
