from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import re

full_username = (By.CSS_SELECTOR, '.hidden.ml-2')
name_of_list_in_the_left_menu = (By.XPATH, '//*[@id="mylists-sidebar"]/div[1]/a[1]/span[1]/h3')
name_of_list_in_the_center = (By.CSS_SELECTOR, '.w-full.text-center>h2')
note_of_list_in_the_center = (By.CSS_SELECTOR, '.w-full.text-center>div>h3')
section_with_red_background_color = (By.CLASS_NAME, 'bg-image-simple-4')
privacy_label_in_the_left_menu = (By.CSS_SELECTOR, '[tabindex="-1"]>.privacy-text>span')
privacy_label_in_the_left_near_settings = (By.CSS_SELECTOR, 'p.flex.items-center.text-sm')
new_list_button = (By.CSS_SELECTOR, '.inline.mx-2')

private_label_in_the_left_menu_text = 'private'
public_label_in_the_left_menu_text = 'public'
shared_label_in_the_left_menu_text = 'shared'
private_label_in_the_left_near_settings_text = 'private list'
public_label_in_the_left_near_settings_text = 'public list'
shared_label_in_the_left_near_settings_text = 'shared list'
full_username_text = 'dasasda sdadad'



class MyListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_my_list_page(self):
        self.driver.get('https://www.giftster.com/list/')

    def start_of_creation_first_list(self):
        new_list_button_element = self.find_element(new_list_button)
        new_list_button_element.click()

    def is_list_contains_correct_name(self, name_of_list):
        name_of_list_in_the_left_menu_element = self.find_element(name_of_list_in_the_left_menu)
        assert name_of_list_in_the_left_menu_element.text == name_of_list
        name_of_list_in_the_center_element = self.find_element(name_of_list_in_the_center)
        assert name_of_list_in_the_center_element.text == name_of_list

    def is_list_contains_correct_note(self, note_of_list):
        note_of_list_in_the_center_element = self.find_element(note_of_list_in_the_center)
        assert note_of_list_in_the_center_element.text == note_of_list

    def is_color_of_list_changed(self):
        section_with_red_background_color_element = self.find_element(section_with_red_background_color)
        assert section_with_red_background_color_element.is_displayed()

    def is_private_label_displayed(self):
        private_label_in_the_left_menu_element = self.find_element(privacy_label_in_the_left_menu)
        assert private_label_in_the_left_menu_element.text == private_label_in_the_left_menu_text
        private_label_in_the_left_near_settings_element = self.find_element(privacy_label_in_the_left_near_settings)
        assert private_label_in_the_left_near_settings_text in private_label_in_the_left_near_settings_element.text

    def is_public_label_displayed(self):
        public_label_in_the_left_menu_element = self.find_element(privacy_label_in_the_left_menu)
        assert public_label_in_the_left_menu_element.text == public_label_in_the_left_menu_text
        public_label_in_the_left_near_settings_element = self.find_element(privacy_label_in_the_left_near_settings)
        assert public_label_in_the_left_near_settings_text in public_label_in_the_left_near_settings_element.text

    def is_shared_label_displayed(self):
        shared_label_in_the_left_menu_element = self.find_element(privacy_label_in_the_left_menu)
        print(shared_label_in_the_left_menu_element.text)
        assert shared_label_in_the_left_menu_element.text == shared_label_in_the_left_menu_text
        shared_label_in_the_left_near_settings_element = self.find_element(privacy_label_in_the_left_near_settings)
        assert shared_label_in_the_left_near_settings_text in shared_label_in_the_left_near_settings_element.text

    def is_username_correct(self):
        user_name_element = self.find_element(full_username)
        assert user_name_element.text == full_username_text






