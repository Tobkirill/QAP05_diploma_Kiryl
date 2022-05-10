from pages.base_page import BasePage
from pages.locators.login_page_locators import email_field, password_field, login_button


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.giftster.com/account/login/')

    def login(self):
        login_button_element = self.find_element(login_button)
        login_button_element.click()

    def fill_in_form_and_login(self, email_to_login, password_to_login):
        self.fill_in_field(email_field, email_to_login)
        self.fill_in_field(password_field, password_to_login)
        self.login()


