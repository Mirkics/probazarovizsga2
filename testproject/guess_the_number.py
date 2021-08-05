'''3 Feladat: Guess the number automatizálása
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a Guess the number app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel az app funkcionalitását tesztelését.
Nem jár plusz pont azért ha úgy automatizálsz, hogy minnél optimálisabban és gyosabban találja ki a helyes számot a program

Egy tesztet kell írnod ami addig találgat a megadott intervallumon belül amíg ki nem találja a helyes számot.
Amikor megvan a helyes szám, ellenőrizd le, hogy a szükséges lépések száma mit az aplikáció kijelez egyezik-e a saját belső számlálóddal.

Teszteld le, hogy az applikáció helyesen kezeli az intervallumon kívüli találgatásokat.
Az applikéció -19 vagy 255 értéknél nem szabad, hogy összeomoljon. Azt kell kiírnia, hogy alá vagy fölé találtál-e.'''
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html')
    time.sleep(2)

    # number = ()
    # guess = random.randint(1, 100) # random számot beírni
    input_number = driver.find_element_by_xpath("/html/body/div/div[2]/input")
    # input_number.send_keys(guess)
    #
    # time.sleep(2)
    guess_button = driver.find_element_by_xpath('/html/body/div/div[2]/span/button')
    # guess_button.click()
    # time.sleep(2)

    input_number.clear()

    # for i in input_number:
    #     if guess == number:
    #         print("Yes! That is it.")
    #     if guess > number:
    #         print("Guess lower")
    # else:
    #     print("Guess higher")
    #
    # szamolok = 0
    # for i in range(1, 100):
    #     szamolok += 1

# határéertéken kívüli érték tesztelése
# testdata = -19 message: Guess higher.", 255 message: "Guess lower."}

    input_number.send_keys('-19')
    guess_button.click()

    answer_higher = driver.find_element_by_xpath('//p[@class="alert alert-warning"]').text
    print(answer_higher)

    assert answer_higher == "Guess higher."
    time.sleep(1)
    input_number.clear()

    input_number.send_keys("255")
    guess_button.click()
    answer_lower = driver.find_element_by_xpath('/html/body/div/p[3]').text
    print(answer_lower)

    assert answer_lower == "Guess lower."

finally:
    driver.close()