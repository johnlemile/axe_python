# pages/base_page.py

# import dependencies
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, by, value, timeout=10, message=None):
        if not message:
            message = f"Element with {by}={value} not found within {timeout} seconds."
            
        return WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
            EC.presence_of_element_located((by, value)), message=message
        )

    @staticmethod
    def presence_of_element(by, value):
        return EC.presence_of_element_located((by, value))

    @staticmethod
    def visibility_of_element(by, value):
        return EC.visibility_of_element_located((by, value))
