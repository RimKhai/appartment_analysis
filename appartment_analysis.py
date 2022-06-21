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

browser = Chrome('driver\chromedriver.exe')
browser.get(settings.url)

def run_program():
    scraper.prices_concatenation(prices, settings, browser)
    calc_res = data_calc.price_calculation(prices)
    data_calc.price_output(calc_res)
    print(prices)
    browser.close()

run_program()
