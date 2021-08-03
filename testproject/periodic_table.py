from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Oldal betöltése
driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html')
time.sleep(2)