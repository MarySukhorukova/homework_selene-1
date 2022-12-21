from selene import be, have
from selene.support.shared import browser
import os
from selene import command
import tests


def test_filling_and_submitting_form():
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Harry')
    browser.element('#lastName').type('Potter')
    browser.element('#userEmail').type('hp@test.com')
    browser.all('[name=gender]').element_by(have.value('Male')).element('./following-sibling::*').click()
    browser.element('#userNumber').type('0123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('July')
    browser.element('.react-datepicker__year-select').send_keys('1980')
    browser.element(f'.react-datepicker__day--0{31}').click()

    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__), 'files/Pytest_logo.svg.png')))

    browser.element('#currentAddress').type('Hogwarts').perform(command.js.scroll_into_view)

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()

    browser.element('#submit').press_enter()

    # THEN
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
