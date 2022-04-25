from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import re


name_of_list_in_the_left_menu = (By.XPATH, '//*[@id="mylists-sidebar"]/div[1]/a[1]/span[1]/h3')
name_of_list_in_the_center = (By.CSS_SELECTOR, '.w-full.text-center>h2')

name_of_list_text = 'Testing_name'
note_text = 'Test note'

new_list_button = (By.CSS_SELECTOR, '.inline.mx-2')


class MyListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_my_list_page(self):
        self.driver.get('https://www.giftster.com/list/')

    def start_of_creation_first_list(self):
        new_list_button_element = self.find_element(new_list_button)
        new_list_button_element.click()

    def is_list_contains_correct_name(self):
        name_of_list_in_the_left_menu_element = self.find_element(name_of_list_in_the_left_menu)
        assert name_of_list_in_the_left_menu_element.text == name_of_list_text
        name_of_list_in_the_center_element = self.find_element(name_of_list_in_the_center)
        assert name_of_list_in_the_center_element == name_of_list_text




