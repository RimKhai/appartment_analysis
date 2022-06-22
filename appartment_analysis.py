from selenium.webdriver import Chrome
from settings import Settings
from scraper import Scraper
from data_functions import DataFunctions


settings = Settings()
scraper = Scraper()
data_calc = DataFunctions()
need_scrap = False
prices = []
metro_dists = []
icons_class = []

browser = Chrome('driver\chromedriver.exe')
browser.get(settings.url)


def run_program():
    for i in range(settings.pages_number):
        scraper.values_concatenation(prices, settings, settings.price_name, browser)
        scraper.values_concatenation(metro_dists, settings, settings.metro_tag_name, browser)
        scraper.icons_extract(browser, icons_class)
        scraper.next_page(settings, browser, i)
    data_calc.data_collection(prices, metro_dists, icons_class)
    browser.close()

run_program()
