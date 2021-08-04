'''Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a sales Film register app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html oldalról.

Feladatod, hogy automatizáld az alkalmazás két funkciójának a tesztelését

Teszteld le, hogy betöltés után megjelennek filmek az alkalmazásban, méghozzá 24 db.
Teszteld le, hogy fel lehet-e venni az alábbi adatokkal egy új filmet:
Film title: Black widow
Release year: 2021
Chronological year of events: 2020
Trailer url: https://www.youtube.com/watch?v=Fp9pNPdNwjI
Image url: https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg
Film summary: https://www.imdb.com/title/tt3480822/'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html')
    time.sleep(2)

#TC1: check 24 films

    film_list = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/a')
    assert len(film_list) == 24

# TC2: new upload
    film_title = 'Black widow'
    release_year = '2021'
    cron_year_events = '2020'
    trailer_url = 'https://www.youtube.com/watch?v=Fp9pNPdNwjI'
    image_url = 'https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg'
    film_summary = 'https://www.imdb.com/title/tt3480822/'

    driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
    time.sleep(2)
    driver.find_element_by_id("nomeFilme").send_keys('Black widow')
    driver.find_element_by_xpath('//*[@id="anoLancamentoFilme"]').send_keys('2021')
    driver.find_element_by_xpath('//*[@id = "anoCronologiaFilme"]').send_keys('2020')
    driver.find_element_by_id("linkTrailerFilme").send_keys('https://www.youtube.com/watch?v=Fp9pNPdNwjI')
    driver.find_element_by_id("linkImagemFilme").send_keys('https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg')
    driver.find_element_by_id("linkImdbFilme").send_keys('https://www.imdb.com/title/tt3480822/')

    save_button = driver.find_element_by_xpath("/html/body/div[2]/div[2]/fieldset/button[1]")
    save_button.click()

    film_list = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/a')
    assert len(film_list) == 25


finally:
    driver.close()
