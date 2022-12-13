from selene import be, have
from selene.support.shared import browser
import os


def test_filling_and_submitting_form(open_practice_form):
    browser.element('#firstName').should(be.blank).type('Harry')
    browser.element('#lastName').should(be.blank).type('Potter')
    browser.element('#userEmail').should(be.blank).type('hp@test.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').should(be.blank).type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1980"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').should(be.blank).type('Dark Arts')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath('tests/Pytest_logo.svg.png'))
    browser.element('#currentAddress').set_value('Hogwarts').press_enter()
    browser.element('#state').click()
    browser.element("//div[text()='Haryana']").click()
    browser.element('#city').click()
    browser.element("//div[text()='Karnal']").click()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Harry Potter' and 'hp@test.com' and 'Male' and '0123456789' and '31 July,1980'
                                               and 'Dark Arts' and 'Sports' and 'Pytest_logo.svg.png' and 'Hogwarts'))
