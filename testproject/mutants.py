"""A Marvel új web alapú rajongó oldalt készít az X-man képregény adaptációkból.

Itt találod a webes applikáció prototípusát: https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html

Készíts egy Python python applikációt (akár csak egy darab python fileban) ami selenium-ot használ.

Teszteld le, hogy a különböző szűrőfeltételek alapján megfelelő karaktereket mutatja az oldal.

Tehát mondjuk iceman pontosan az original és a factor csapatban van benne és a hellfire illetve a force csapatokban nincs benne.

(Figyelem: ne engedd, hogy az oldal dinamikus működése elvonja a figyelmed a célról!
A karaktereket csoporthoz tartozását nem feltétlenül a felület változásával tudod ellenőrizni.)

Al alkalmazás helyesen mutatja a felületen a csoporthoz tartozást.
Nincs külön tesztadat leírás ehhez a feladathoz, tehát a látottak alapján kell a tesztadatot összeállítanod.

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat NEM kell OOP-t használnod.
Viszont tartalmazzon vizsgálatot a megodásod. Lehetőleg használj az assert összehasonlításokat."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html')
    time.sleep(2)

    iceman = driver.find_element_by_id("iceman").get_attribute("data-teams")
    print(iceman)
    assert iceman == "original factor"
    assert not iceman == 'hellfire'

    i_man = driver.find_element_by_xpath('//*[@id="iceman"]/h2').text
    print(i_man)
    assert i_man == "Iceman"

finally:
    driver.close()




