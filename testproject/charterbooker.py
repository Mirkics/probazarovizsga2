'''4 Feladat: charterbooker automatizálása
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a charterbooker app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a charterbooker app tesztelését.

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy assert összehasonlításokat.

Teszteld le a többoldalas formanyomtatvány működését.
Ellenőrizd a helyes kitöltésre adott választ:
"Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."
Készíts tesztesetet az e-mail cím validációjára.'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html')
    time.sleep(2)
     
# TC1 fill in the form

    Select(driver.find_element_by_name('bf_totalGuests')).select_by_value("1")

    # select_guest = Select(driver.find_element_by_name('bf_totalGuests'))
    # select_guest.select_by_value("1")

    #driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select/option[2]').click()

    time.sleep(1)
    next_button = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button')
    next_button.click()

    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input').send_keys("2021-5-12")

    Select(driver.find_element_by_name('bf_time')).select_by_value("Morning")
    #driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select/option[3]').click()

    Select(driver.find_element_by_name('bf_hours')).select_by_value("5")

    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button').click()

    driver.find_element_by_name("bf_fullname").send_keys("Kis Laci")

    input_email = driver.find_element_by_name("bf_email")
    input_email.send_keys("kis.laci@valami.com")

    driver.find_element_by_name("bf_message").send_keys("Hello")

    submit_button = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button')
    submit_button.click()

    time.sleep(2)
    message_text = "Your message was sent successfully. " \
                   "Thanks! We'll be in touch as soon as we can, which is usually like lightning " \
                   "(Unless we're sailing or eating tacos!)."
    message = driver.find_element_by_xpath('//*[@id="booking-form"]/h2').text
    print(message)
    assert message == message_text

# TC2 email validation. wrong email test data: kis.laci@valami@valami.com

    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html')
    time.sleep(2)

    Select(driver.find_element_by_name('bf_totalGuests')).select_by_value("1")

    time.sleep(1)
    next_button = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button')
    next_button.click()

    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input').send_keys("2021-5-12")

    Select(driver.find_element_by_name('bf_time')).select_by_value("Morning")
    # driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select/option[3]').click()

    Select(driver.find_element_by_name('bf_hours')).select_by_value("5")

    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button').click()

    driver.find_element_by_name("bf_fullname").send_keys("Kis Laci")

    input_email = driver.find_element_by_name("bf_email")
    input_email.send_keys("kis.laci@valami@valami.com")
    driver.find_element_by_name("bf_message").send_keys("Hello")

    error_message_text = driver.find_element_by_xpath('//*[@id="bf_email-error"]') # Hogyan kell innen kivenni a az error üzenetet?
    message = "Please enter a valid email address."
    assert error_message_text == message  # hibára fut - AssertionError
    time.sleep(10)

finally:
    driver.close()
