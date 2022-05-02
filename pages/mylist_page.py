from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import re
from tkinter import Tk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

full_username = (By.CSS_SELECTOR, '.hidden.ml-2')
name_of_list_in_the_left_menu = (By.XPATH, '//*[@id="mylists-sidebar"]/div[1]/a[1]/span[1]/h3')
name_of_list_in_the_center = (By.CSS_SELECTOR, '.w-full.text-center>h2')
note_of_list_in_the_center = (By.CSS_SELECTOR, '.w-full.text-center>div>h3')
section_with_red_background_color = (By.CLASS_NAME, 'bg-image-simple-4')
privacy_label_in_the_left_menu = (By.CSS_SELECTOR, '[tabindex="-1"]>.privacy-text>span')
privacy_label_near_settings = (By.CSS_SELECTOR, 'p.flex.items-center.text-sm')
new_list_button = (By.CSS_SELECTOR, '.inline.mx-2')
create_new_list_from_my_list_page_button = (By.CLASS_NAME, 'btn-tan-200')
share_button = (By.CSS_SELECTOR, '[type=button]>.px-3')
copy_link_button = (By.CSS_SELECTOR, '.w-48.mt-3')
add_item_white_button = (By.CSS_SELECTOR, '.z-10.pl-2>button:nth-child(1)')
item_section = (By.CSS_SELECTOR, '.flex.w-full.h-20')
remove_item_button = (By.CSS_SELECTOR, '.w-full.ml-4')
copy_item_button = (By.CSS_SELECTOR, '.justify-center>[title="Copy item to another list"]')
i_got_this_button = (By.CSS_SELECTOR, '.justify-center>[title=" Delete and move item to I Got This list "]')
rate_1_stars_button = (By.CSS_SELECTOR, '.flex.mt-7>.px-3>.flex>span:nth-child(1)')
rate_2_stars_button = (By.CSS_SELECTOR, '.flex.mt-7>.px-3>.flex>span:nth-child(2)')
rate_3_stars_button = (By.CSS_SELECTOR, '.flex.mt-7>.px-3>.flex>span:nth-child(3)')
rate_4_stars_button = (By.CSS_SELECTOR, '.flex.mt-7>.px-3>.flex>span:nth-child(4)')
rate_5_stars_button = (By.CSS_SELECTOR, '.flex.mt-7>.px-3>.flex>span:nth-child(5)')
star_1_in_items_section = (By.CSS_SELECTOR, '.w-20.ml-5>.flex>span:nth-child(1)>svg>path')
star_2_in_items_section = (By.CSS_SELECTOR, '.w-20.ml-5>.flex>span:nth-child(2)>svg>path')
star_3_in_items_section = (By.CSS_SELECTOR, '.w-20.ml-5>.flex>span:nth-child(3)>svg>path')
star_4_in_items_section = (By.CSS_SELECTOR, '.w-20.ml-5>.flex>span:nth-child(4)>svg>path')
star_5_in_items_section = (By.CSS_SELECTOR, '.w-20.ml-5>.flex>span:nth-child(5)>svg>path')
stars_in_items_section = (star_1_in_items_section, star_2_in_items_section, star_3_in_items_section,
                          star_4_in_items_section, star_5_in_items_section)
price_of_item_field = (By.CSS_SELECTOR, '.px-3>span>input')
where_to_by_field = (By.CSS_SELECTOR, '.px-3>input')
price_of_item_in_items_section = (By.CSS_SELECTOR, '.mr-6>h2')

gift_name = (By.CSS_SELECTOR, '.flex.px-6>.rounded-md')
name_of_gift_in_items_section = (By.CSS_SELECTOR, '.text-sm.font-medium.ml-3')
save_adding_new_item_button = (By.XPATH, '//*[@id="createItemForm"]/div/div[2]/div[2]/div[1]/div[6]/div/button[1]')
adding_new_item_info_message = (By.CSS_SELECTOR, 'div>span.ml-3')

private_label_in_the_left_menu_text = 'private'
public_label_in_the_left_menu_text = 'public'
shared_label_in_the_left_menu_text = 'shared'
private_label_near_settings_text = 'private list'
public_label_near_settings_text = 'public list'
shared_label_near_settings_text = 'shared list'
full_username_text = 'dasasda sdadad'
gift_name_text = 'Phone'
adding_new_item_info_message_text = 'Awesome, you added your first item.'
quantity_of_stars_to_rate = 3
price_of_item_text = '20 dollars'


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

    def is_privacy_label_correct(self, privacy_label_in_the_left_menu_text, privacy_label_near_settings_element_text):
        privacy_label_in_the_left_menu_element = self.find_element(privacy_label_in_the_left_menu)
        assert privacy_label_in_the_left_menu_element.text == privacy_label_in_the_left_menu_text
        privacy_label_near_settings_element = self.find_element(privacy_label_near_settings)
        assert privacy_label_near_settings_element_text in privacy_label_near_settings_element.text

    def is_username_correct(self):
        user_name_element = self.find_element(full_username)
        assert user_name_element.text == full_username_text

    def start_creation_of_new_list_from_my_page(self):
        create_new_list_from_my_list_page_button_element = self.find_element(create_new_list_from_my_list_page_button)
        create_new_list_from_my_list_page_button_element.click()

    def share_list(self):
        share_button_element = self.find_element(share_button)
        share_button_element.click()

    def is_share_link_correct(self):
        copy_link_button_element = self.find_element(copy_link_button)
        copy_link_button_element.click()
        copied_text = Tk().clipboard_get()
        url_to_compare = self.driver.current_url.replace('list', 'gift')
        assert copied_text == url_to_compare

    def is_gift_name_in_items_section_correct(self, name_of_gift):
        name_of_gift_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(name_of_gift_in_items_section))
        assert name_of_gift_in_items_section_element.text == name_of_gift

    def start_to_add_new_item_to_list(self):
        add_item_white_button_element = self.find_element(add_item_white_button)
        add_item_white_button_element.click()

    def save_adding_new_item(self):
        save_adding_new_item_button_element = self.find_element(save_adding_new_item_button)
        save_adding_new_item_button_element.click()

    def is_adding_new_item_info_message_present(self):
        adding_new_item_info_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(adding_new_item_info_message))
        assert adding_new_item_info_message_element.text == adding_new_item_info_message_text

    def start_to_edit_added_item(self):
        item_element = self.find_element(item_section)
        item_element.click()

    def is_edit_mode_contains_new_elements(self):
        remove_item_button_element = self.find_element(remove_item_button)
        assert remove_item_button_element.is_displayed()
        copy_item_button_element = self.find_element(copy_item_button)
        assert copy_item_button_element.is_displayed()
        i_got_this_button_element = self.find_element(i_got_this_button)
        assert i_got_this_button_element.is_displayed()

    def remove_added_item(self):
        remove_item_button_element = self.find_element(remove_item_button)
        self.driver.execute_script("arguments[0].click();", remove_item_button_element)

    def is_removed_item_not_displayed(self):
        item_section_element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(item_section))
        assert item_section_element

    def rate_item_with_stars(self, quantity_of_stars):
        if quantity_of_stars == 1:
            rate_1_stars_button_element = self.find_element(rate_1_stars_button)
            rate_1_stars_button_element.click()
        if quantity_of_stars == 2:
            rate_2_stars_button_element = self.find_element(rate_2_stars_button)
            rate_2_stars_button_element.click()
        if quantity_of_stars == 3:
            rate_3_stars_button_element = self.find_element(rate_3_stars_button)
            rate_3_stars_button_element.click()
        if quantity_of_stars == 4:
            rate_4_stars_button_element = self.find_element(rate_4_stars_button)
            rate_4_stars_button_element.click()
        if quantity_of_stars == 5:
            rate_5_stars_button_element = self.find_element(rate_5_stars_button)
            rate_5_stars_button_element.click()

    def is_star_in_rating_active(self, star):
        star_element_attributes = self.get_element_attributes(star)
        if star_element_attributes['fill'] == 'currentColor':
            return True
        return False

    def quantity_of_stars_active(self):
        star_1_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(star_1_in_items_section))
        star_2_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(star_2_in_items_section))
        star_3_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(star_3_in_items_section))
        star_4_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(star_4_in_items_section))
        star_5_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(star_5_in_items_section))
        stars = (star_1_in_items_section_element, star_2_in_items_section_element, star_3_in_items_section_element,
                                            star_4_in_items_section_element, star_5_in_items_section_element)
        counter = 0
        for element in stars:
            if self.is_star_in_rating_active(element):
                counter += 1
        return counter

    def is_star_rating_correct(self, quantity_of_stars_expected):
        quantity_of_active_stars = self.quantity_of_stars_active()
        assert quantity_of_active_stars == quantity_of_stars_expected

    def is_price_of_item_correct_and_displayed(self, price_expected):
        price_of_item_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(price_of_item_in_items_section))
        assert price_of_item_in_items_section_element.text == price_expected

