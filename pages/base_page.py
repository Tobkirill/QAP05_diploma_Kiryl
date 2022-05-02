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

    def get_element_attributes(self, element):
        return self.driver.execute_script(
            """
            let attr = arguments[0].attributes;
            let items = {}; 
            for (let i = 0; i < attr.length; i++) {
                items[attr[i].name] = attr[i].value;
            }
            return items;
            """,
            element
        )

    def is_field_required(self, field):
        element = self.find_element(field)
        attributes = self.get_element_attributes(element)
        assert attributes['required'] == 'required'

    def is_url_correct(self, url):
        assert self.driver.current_url == url

    def is_checkbox_checked(self, checkbox):
        checkbox_element = self.find_element(checkbox)
        checkbox_attributes = self.get_element_attributes(checkbox_element)
        assert checkbox_attributes['checked'] == 'checked'

    def tick_checkbox(self, checkbox):
        checkbox_element = self.find_element(checkbox)
        checkbox_element.click()