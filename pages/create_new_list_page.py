from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.create_new_list_locators import create_new_list_button, simple_red_color_button
from pages.testing_data.create_new_list_test_data import create_new_list_url


class CreateNewListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_new_list_page(self):
        self.driver.get(create_new_list_url)

    def create_new_list(self):
        create_new_list_button_element = self.find_element(create_new_list_button)
        create_new_list_button_element.click()

    def choose_simple_color_of_list(self):
        simple_red_color_button_element = self.find_element(simple_red_color_button)
        simple_red_color_button_element.click()

    def choose_privacy_of_list(self, privacy):
        privacy_element = self.find_element(privacy)
        privacy_element.click()

    def choose_public_search_options(self, option):
        option_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(option))
        option_element.click()
