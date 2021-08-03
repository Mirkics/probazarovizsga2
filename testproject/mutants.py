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



    iceman = driver.find_element_by_id("iceman")
    assert 'iceman' == "original"

finally:
    driver.close()




