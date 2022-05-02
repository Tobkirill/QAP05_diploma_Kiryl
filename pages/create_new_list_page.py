from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name_of_list_field = (By.ID, 'id_privacy-title')
add_a_note_field = (By.ID, 'id_privacy-description')
create_new_list_button = (By.CSS_SELECTOR, '.btn.btn-red-600.btn-snug')
simple_red_color_button = (By.CSS_SELECTOR, ".flex.flex-wrap.justify-center.md\:ml-7>li:nth-child(4)>button")
private_list_button = (By.CSS_SELECTOR, '.flex.border>button:nth-child(1)')
group_list_button = (By.CSS_SELECTOR, '.flex.border>button:nth-child(2)')
public_list_button = (By.CSS_SELECTOR, '.flex.border>button:nth-child(3)')
first_group_checkbox = (By.ID, 'id_perms-group_0')
public_search_option_gifster_and_google = (By.ID, 'id_privacy-search_visibility_2')
public_search_option_gifster = (By.ID, 'id_privacy-search_visibility_1')
public_search_option_share_link = (By.ID, 'id_privacy-search_visibility_0')

create_new_list_url = 'https://www.giftster.com/list/new/'
name_of_list_text = 'MyList3'
note_text = 'Important Note'


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




