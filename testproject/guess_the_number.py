'''3 Feladat: Guess the number automatizálása
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a Guess the number app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel az app funkcionalitását tesztelését.
Nem jár plusz pont azért ha úgy automatizálsz, hogy minnél optimálisabban és gyosabban találja ki a helyes számot a program

Egy tesztet kell írnod ami addig találgat a megadott intervallumon belül amíg ki nem találja a helyes számot.
Amikor megvan a helyes szám, ellenőrizd le, hogy a szükséges lépések száma mit az aplikáció kijelez egyezik-e a saját belső számlálóddal.

Teszteld le, hogy az applikáció helyesen kezeli az intervallumon kívüli találgatásokat.
Az applikéció -19 vagy 255 értéknél nem szabad, hogy összeomoljon. Azt kell kiírnia, hogy alá vagy fölé találtál-e.'''

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

    number = ()
    guess = 36 # random számot beírni
    input_number = driver.find_element_by_xpath("/html/body/div/div[2]/input").send_keys("36")
    guess_button = driver.find_elements_by_class_name("btn btn-primary")


    time.sleep(2)

    if guess in input_number:
        guess == number
        print("Yes! That is it.")
        if guess in input_number:
            guess > number
            print("Guess lower")
    else:
        print("Guess higher")




finally:
    driver.close()