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

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html')
    time.sleep(2)
     
#utólag tettem be
#     next_button = driver.find_element_by_class_name("next-btn next-btn1")
#     select = driver.find_element_by_tag_name("bf_totalGuests").click()
#     option = driver.find_element_by_xpath("//*[@id="step1"]/ul/li[1]/select/option[1]")
#     select(option)
#     click(next_button)
     
    
#     click(next_button)
         
        

finally:
    driver.close()
