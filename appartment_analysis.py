from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from settings import Settings
from scraper import Scraper
from data_functions import DataFunctions


settings = Settings()
scraper = Scraper()
data_calc = DataFunctions()
prices = []
metro_dists = []
icons_class = []

browser = Chrome('driver\chromedriver.exe')
browser.get(settings.url)


def run_program():
    for i in range(settings.pages_number):
        scraper.values_concatenation(prices, settings, settings.price_name, browser)
        scraper.values_concatenation(metro_dists, settings, settings.metro_tag_name, browser)

        icon = browser.find_elements(By.CLASS_NAME, value='Icon')
        for j in icon:
            if j.get_attribute('class') == 'Icon Icon_type_small-pedestrian' or j.get_attribute('class') == 'Icon Icon_type_small-bus':
                if j.get_attribute('class') == 'Icon Icon_type_small-pedestrian':
                    icons_class.append('walk')
                if j.get_attribute('class') == 'Icon Icon_type_small-bus':
                    icons_class.append('bus')
        scraper.next_page(settings, browser, i)
    calc_res = data_calc.price_calculation(prices)
    data_calc.price_output(calc_res)
    print(prices)
    print(metro_dists)
    print(icons_class)
    print(len(prices), len(metro_dists), len(icons_class))
    browser.close()

run_program()
