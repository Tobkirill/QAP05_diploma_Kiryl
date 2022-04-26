from pages.base_page import BasePage
from selenium.webdriver.common.by import By

name_of_list_field = (By.ID, 'id_privacy-title')
add_a_note_field = (By.ID, 'id_privacy-description')
create_new_list_button = (By.CSS_SELECTOR, '.btn.btn-red-600.btn-snug')
simple_red_color_button = (By.CSS_SELECTOR, ".flex.flex-wrap.justify-center.md\:ml-7>li:nth-child(4)>button")
private_list_button = (By.CSS_SELECTOR, '.flex.border>button:nth-child(1)')

create_new_list_url = 'https://www.giftster.com/list/new'
name_of_list_text = 'Testing_name'
note_text = 'Test note'


class CreateNewListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_new_list_page(self):
        self.driver.get(create_new_list_url)

    def is_field_required(self, field):
        element = self.find_element(field)
        assert element.get_attribute('required') == 'required'

    def is_url_remains(self):
        print(self.driver.current_url)
        assert self.driver.current_url == create_new_list_url

    def create_new_list(self):
        create_new_list_button_element = self.find_element(create_new_list_button)
        create_new_list_button_element.click()

    def choose_simple_color_of_list(self):
        simple_red_color_button_element = self.find_element(simple_red_color_button)
        simple_red_color_button_element.click()

    def choose_private_list(self):
        private_list_button_element = self.find_element(private_list_button)
        private_list_button_element.click()




