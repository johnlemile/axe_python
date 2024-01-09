# pages/sample_page.py

# import dependencies
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SamplePage(BasePage):
    SAMPLE_ELEMENT = (By.XPATH, "/html/body/div[1]/div[6]/div[1]/div[1]/a[1]")

    def do_something(self):
        self.click_sample_element()

    def click_sample_element(self):
        self.find_element(*self.SAMPLE_ELEMENT).click()
