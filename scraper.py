from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time



class Scraper:


    def values_exctract(self, browser, settings, page):
        count = 0
        price = []
        prices_elem = browser.find_elements(by=By.CLASS_NAME, value=settings.class_name)
        next_button = browser.find_element(by=By.LINK_TEXT, value=settings.button_name)
        while True:
            price.append(int(re.sub(r"[^\d]", '', prices_elem[count].text)))
            count += 1
            if count == len(prices_elem):
                break
        if page < settings.pages_number:
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable(next_button)).click()

        return price

    def prices_concatenation(self, prices, settings, browser):
        for i in range(settings.pages_number):
            time.sleep(settings.sleep_time)
            prices.extend(self.values_exctract(browser, settings, i))

        return prices