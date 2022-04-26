from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def open_homepage(self):
        self.driver.get('https://www.giftster.com/')

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def find_elements(self, *args):
        by, val = args[0]
        return self.driver.find_elements(by, val)

    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True

    def fill_in_field(self, field, text):
        try:
            element = self.driver.find_element(*field)
            element.send_keys(text)
        except NoSuchElementException:
            return False
        return True
