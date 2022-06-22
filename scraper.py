from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time


class Scraper:
    def next_page(self, settings, browser, page):
        if page < settings.pages_number:
            next_button = browser.find_element(by=By.LINK_TEXT, value=settings.button_name)
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable(next_button)).click()

    def values_extract(self, browser, value_link):
        count = 0
        values = []
        values_elem = browser.find_elements(by=By.CLASS_NAME, value=value_link)
        while True:
            values.append(int(re.sub(r"[^\d]", '', values_elem[count].text)))
            count += 1
            if count == len(values_elem):
                break

        return values

    def icons_extract(self, browser, icons_class):
        icon = browser.find_elements(By.CLASS_NAME, value='Icon')
        for j in icon:
            if j.get_attribute('class') == 'Icon Icon_type_small-pedestrian' or j.get_attribute(
                    'class') == 'Icon Icon_type_small-bus':
                if j.get_attribute('class') == 'Icon Icon_type_small-pedestrian':
                    icons_class.append('walk')
                if j.get_attribute('class') == 'Icon Icon_type_small-bus':
                    icons_class.append('bus')

        return icons_class

    def values_concatenation(self, values, settings, value_link, browser):
        time.sleep(settings.sleep_time)
        values.extend(self.values_extract(browser, value_link))

        return values
