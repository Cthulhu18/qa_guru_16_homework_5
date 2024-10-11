import os
from selene import browser, have, be, command


def test_the_form():
    browser.open('automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")  # Хотелось бы узнать подробнее про эти команды
    browser.driver.execute_script("$('footer').remove()")  # Хотелось бы узнать подробнее про эти команды
    browser.element('#firstName').type('Сергей')
    browser.element('#lastName').type('Махно')
    browser.element('#userEmail').type('test@mail.ru')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9371821244')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1989"]').click()
    browser.element('.react-datepicker__day--014').click()
    browser.element('#subjectsInput').type('c')
    browser.element('.subjects-auto-complete__menu-list').element(
        '//*[text()="Computer Science"]').click()  # Не понятно как нашли этот XPath
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img20.jpg'))
    browser.element('#currentAddress').type('ул. Лесная, д. 45, кв. 12')
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('//*[text()="Uttar Pradesh"]').click()  # Не понятно как нашли этот XPath
    browser.element('#city').click()
    browser.element('//*[text()="Lucknow"]').click()  # Не понятно как нашли этот XPath

    #  Не понятно зачем нужны проверки описанные в коде ниже

    browser.element('#dateOfBirthInput').should(have.attribute('value', '14 Aug 1989'))
    browser.all('.subjects-auto-complete__multi-value__label').should(have.exact_texts('Computer Science'))
    browser.element('.subjects-auto-complete__multi-value__remove').should(be.visible)
    browser.all('[type="checkbox"]')[1].should(have.attribute('value').value('2'))
    browser.all('[type="checkbox"]')[2].should(have.attribute('value').value('3'))
    browser.element('#submit').click()

    browser.element('table').should(be.visible)
    browser.element('//table//td[text()="Student Name"]/../td[2]').should(have.exact_text('Сергей Махно'))
    browser.element('//table//td[text()="Student Email"]/../td[2]').should(have.exact_text('test@mail.ru'))
    browser.element('//table//td[text()="Gender"]/../td[2]').should(have.exact_text('Male'))
    browser.element('//table//td[text()="Mobile"]/../td[2]').should(have.exact_text('9371821244'))
    browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(have.exact_text('14 August,1989'))
    browser.element('//table//td[text()="Subjects"]/../td[2]').should(have.exact_text('Computer Science'))
    browser.element('//table//td[text()="Hobbies"]/../td[2]').should(have.exact_text('Reading, Music'))
    browser.element('//table//td[text()="Picture"]/../td[2]').should(have.exact_text('img20.jpg'))
    browser.element('//table//td[text()="Address"]/../td[2]').should(
        have.exact_text('ул. Лесная, д. 45, кв. 12'))
    browser.element('//table//td[text()="State and City"]/../td[2]').should(have.exact_text('Uttar Pradesh Lucknow'))
