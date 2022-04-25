from pages.base_page import BasePage
from selenium.webdriver.common.by import By

name_of_list_field = (By.ID, 'id_privacy-title')
add_a_note_field = (By.ID, 'id_privacy-description')

name_of_list_text = 'Testing_name'
note_text = 'Test note'


class CreateNewListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_new_list_page(self):
        self.driver.get('https://www.giftster.com/list/new')

    def is_field_required(self, field):
        element = self.find_element(field)
        assert element.get_attribute('required') == 'required'

