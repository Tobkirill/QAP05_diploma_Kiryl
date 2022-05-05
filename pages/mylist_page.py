from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import re
from tkinter import Tk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
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
item_1_section = (By.CSS_SELECTOR, 'ul.-mt-5>li:nth-child(1)')
item_2_section = (By.CSS_SELECTOR, 'ul.-mt-5>li:nth-child(2)')
items_section = (By.CSS_SELECTOR, 'ul.-mt-5>li')
add_image_section = (By.CSS_SELECTOR, 'div.hidden>div>div>.border-dashed')
web_search_field_in_add_image_pop_up = (By.CLASS_NAME, 'fsp-url-source__input')
start_search_button = (By.CLASS_NAME, 'fsp-url-source__submit-button')
search_results = (By.CLASS_NAME, 'fsp-image-grid__image')
upload_image_button = (By.CSS_SELECTOR, '[title="Upload"]')
close_add_image_pop_up_button = (By.CLASS_NAME, 'fsp-picker__close-button')
image_in_the_last_step_of_upload = (By.CSS_SELECTOR, 'img.cropper-hidden')
uploaded_image_section = (By.CSS_SELECTOR, 'div.hidden>div>div>img')
remove_item_button = (By.CSS_SELECTOR, '.w-full.ml-4')
copy_item_button = (By.CSS_SELECTOR, '.justify-center>[title="Copy item to another list"]')
confirm_copy_item_button = (By.CSS_SELECTOR, '.btn-yellow-400.btn-sm')
choose_list_dropdown = (By.CSS_SELECTOR, '[name="list"]')
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
quantity_field = (By.CSS_SELECTOR, '.mt-2>.flex.items-center>:nth-child(2)')
quantity_of_items_in_items_section = (By.CSS_SELECTOR, '.mr-7.w-18>h2')
where_to_buy_field = (By.CSS_SELECTOR, '.px-3.mb-5>input')
description_field = (By.CSS_SELECTOR, 'textarea.h-20')
settings_button = (By.CSS_SELECTOR, 'p>a')
delete_list_button = (By.CSS_SELECTOR, '.text-red-600.underline')
yes_delete_button = (By.CSS_SELECTOR, '[name="confirm"]')
gift_name_field = (By.CSS_SELECTOR, '.flex.px-6>.rounded-md')
gift_name_field_in_edition_mode = (By.CSS_SELECTOR, '.px-5>input')
name_of_gift_in_items_section = (By.CSS_SELECTOR, '.w-48>h2')
# save_adding_new_item_button = (By.CSS_SELECTOR, '.mt-5>button:nth-child(1)')
save_adding_new_item_button = (
    By.XPATH, '/html/body/div[2]/main/section[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[6]/div/button[1]')
save_edition_button = (
    By.XPATH, '/html/body/div[2]/main/section[2]/div[1]/ul/li/div[2]/div[2]/div/div[1]/div[7]/div/button[1]'
)
cancel_adding_new_item_button = (
    By.XPATH, '/html/body/div[2]/main/section[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[6]/div/button[2]')
cancel_edition_button = (
    By.XPATH, '/html/body/div[2]/main/section[2]/div[1]/ul/li/div[2]/div[2]/div/div[1]/div[7]/div/button[3]'
)
adding_new_item_info_message = (By.CSS_SELECTOR, 'div>span.ml-3')
i_got_it_list = (By.CSS_SELECTOR, '[href="/list/i-got-this/"]')
validation_warning = (By.CSS_SELECTOR, 'p.my-3')


fetch_button = (By.CSS_SELECTOR, '.hidden>.py-0.pl-5')
web_link_field = (By.CLASS_NAME, 'link')
image_of_fetched_item_in_the_right = (By.XPATH, '/html/body/div[2]/main/section[2]/div[2]/div/div/div[2]'
                                                '/div[2]/div[2]/div/div/img')
image_of_fetched_item_in_the_below = (By.CSS_SELECTOR, '[style="max-height: 500px;"]')

private_label_in_the_left_menu_text = 'private'
public_label_in_the_left_menu_text = 'public'
shared_label_in_the_left_menu_text = 'shared'
private_label_near_settings_text = 'private list'
public_label_near_settings_text = 'public list'
shared_label_near_settings_text = 'shared list'
full_username_text = 'dasasda sdadad'
gift_name_text = 'Laptop'
adding_new_item_info_message_text = 'Awesome, you added your first item.'
quantity_of_stars_to_rate = 3
price_of_item_text = '20 dollars'
quantity_of_items = '5'
where_to_buy_field_text = 'City mall'
description_of_item_text = 'Very cool item'

web_link_to_fetch = 'https://www.amazon.com/HP-Touch-Screen-Quad-Core-i7-10510U-15-EB0043DX/dp/B08CS48VZR/ref=' \
                    'psdc_13896609011_t1_B08RRSVW52'
name_of_fetched_item = 'HP Spectre X360 15.6 Inch 4K UHD Touch-Screen 512GB SSD + 32GB Optane 1.8GHz i7 2-in-1 Laptop' \
                       ' (16GB RAM, Quad-Core i7-10510U, GeForce MX330, Windows 10 Home) Nightfall Black 15-EB0043DX'

price_of_fetched_item = '$2196.99'
where_to_buy_fetched_item = 'see web link'
description_of_fetched_item = '''360° Flip-and-Fold Design, 1.8GHz 10th Gen Intel i7-10510U Quad-Core (up to 4.9GHz)

15.6" Diagonal 4K UHD WLED Touch Display (3840 x 2160) 340 nits, intel GPU (2GB)

512GB SSD + 32GB Intel Optane, 16GB DDR4 SDRAM, SD Card Reader, Bang & Olufsen Quad speakers'''

image_link_of_fetched_item = 'https://m.media-amazon.com/images/I/41WbnO94WUL._SL500_.jpg'
number_of_image = 1
link_of_image_to_add = \
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR6G_V7PZUtl0jWV315SnVXJXnQZD0Cygi4M9hWezGBNE8nb0O6Zhv8Co&s'
keyword_image_to_search = 'laptop'
new_gift_name_for_edition = 'Phone'

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
        save_adding_new_item_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(save_adding_new_item_button))
        save_adding_new_item_button_element.click()

    def is_adding_new_item_info_message_present(self):
        adding_new_item_info_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(adding_new_item_info_message))
        assert adding_new_item_info_message_element.text == adding_new_item_info_message_text

    def is_item_section_displayed(self):
        item_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(item_1_section))
        assert item_section_element

    def is_item_section_not_displayed(self):
        item_section_element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(item_1_section))
        assert item_section_element

    def start_to_edit_added_item(self):
        sleep(1)
        item_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(item_1_section))
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
            EC.invisibility_of_element_located(item_1_section))
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

    def is_star_rating_correct(self):
        quantity_of_active_stars = self.quantity_of_stars_active()
        assert quantity_of_active_stars == quantity_of_stars_to_rate

    def is_price_of_item_correct_and_displayed(self):
        price_of_item_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(price_of_item_in_items_section))
        assert price_of_item_in_items_section_element.text == price_of_item_text

    def set_quantity_of_items(self, quantity):
        quantity_field_element = self.find_element(quantity_field)
        quantity_field_element.clear()
        quantity_field_element.send_keys(quantity)

    def is_quantity_of_items_displayed_correct(self):
        quantity_of_items_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(quantity_of_items_in_items_section))
        assert quantity_of_items_in_items_section_element.text == quantity_of_items

    def fetch_link_of_item(self):
        fetch_button_element = self.find_element(fetch_button)
        fetch_button_element.click()

    def is_images_links_fetched_correctly(self):
        image_of_fetched_item_in_the_right_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(image_of_fetched_item_in_the_right))
        assert image_of_fetched_item_in_the_right_element.get_attribute('src') == image_link_of_fetched_item
        image_of_fetched_item_in_the_below_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(image_of_fetched_item_in_the_below))
        image_of_fetched_item_in_the_below_element.get_attribute('src')
        assert image_of_fetched_item_in_the_below_element.get_attribute('src') == image_link_of_fetched_item

    def is_add_item_form_populated_with_correct_values(self):
        self.is_field_populated_with_value(web_link_field, web_link_to_fetch)
        self.is_field_populated_with_value(gift_name_field, name_of_fetched_item)
        self.is_field_populated_with_value(price_of_item_field, price_of_fetched_item)
        self.is_field_populated_with_value(where_to_by_field, where_to_buy_fetched_item)
        self.is_field_populated_with_value(description_field, description_of_fetched_item)
        self.is_images_links_fetched_correctly()

    def cancel_adding_new_item(self):
        cancel_adding_new_item_button_element = self.find_element(cancel_adding_new_item_button)
        cancel_adding_new_item_button_element.click()

    def copy_item_in_edit_mode(self):
        copy_item_button_element = self.find_element(copy_item_button)
        copy_item_button_element.click()

    def get_quantity_of_items_in_list(self):
        try:
            self.driver.switch_to.alert.dismiss()
        except NoAlertPresentException:
            pass
        items_section_element = self.find_elements(items_section)
        return len(items_section_element)

    def remove_all_added_items(self):
        for i in range(self.get_quantity_of_items_in_list()):
            self.start_to_edit_added_item()
            self.remove_added_item()
            sleep(3)

    def delete_list(self):
        settings_button_element = self.find_element(settings_button)
        settings_button_element.click()
        delete_list_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(delete_list_button))
        delete_list_button_element.click()
        yes_delete_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(yes_delete_button))
        yes_delete_button_element.click()

    def confirm_of_copying_item(self):
        confirm_copy_item_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(confirm_copy_item_button))
        sleep(3)
        confirm_copy_item_button_element.click()

    def is_item_copied(self):
        assert self.get_quantity_of_items_in_list() == 2
        items_in_items_section = self.find_elements(items_section)
        for item in items_in_items_section:
            assert item.text == gift_name_text + '\n' + quantity_of_items

    def start_i_got_this_process(self):
        i_got_this_button_element = self.find_element(i_got_this_button)
        i_got_this_button_element.click()

    def open_i_got_it_list(self):
        i_got_it_list_element = self.find_element(i_got_it_list)
        i_got_it_list_element.click()

    def start_to_add_image(self):
        add_image_section_element = self.find_element(add_image_section)
        add_image_section_element.click()

    def search_image(self, keyword_for_search):
        web_search_field_in_add_image_pop_up_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(web_search_field_in_add_image_pop_up))
        web_search_field_in_add_image_pop_up_element.send_keys(keyword_for_search)
        start_search_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(start_search_button))
        start_search_button_element.click()

    def choose_image_in_search(self, number_of_image_to_add):
        search_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(search_results))
        sleep(3)
        search_elements[number_of_image_to_add-1].click()

    def upload_chosen_image(self):
        image_in_the_last_step_of_upload_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(image_in_the_last_step_of_upload))
        upload_image_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(upload_image_button))
        sleep(5)
        upload_image_button_element.click()

    def close_add_image_pop_up(self):
        try:
            close_add_image_pop_up_button_element = self.find_element(close_add_image_pop_up_button)
            close_add_image_pop_up_button_element.click()
        except NoSuchElementException:
            pass

    def get_src_url_of_uploaded_image(self):
        uploaded_image_section_element = self.find_element(uploaded_image_section)
        src_of_uploaded_img = uploaded_image_section_element.get_attribute('src')
        return src_of_uploaded_img

    def is_image_in_items_section_correct(self, expected_url_of_img):
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'[src="{expected_url_of_img}"]')))

    def is_validation_pop_up_with_correct_warning_appeared(self):
        validation_warning_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(validation_warning))
        assert validation_warning_element.text == 'Please enter an item name'

    def save_edition_of_item(self):
        save_edition_button_element = self.find_element(save_edition_button)
        save_edition_button_element.click()

    def cancel_edition_of_item(self):
        cancel_edition_button_element = self.find_element(cancel_edition_button)
        cancel_edition_button_element.click()

    def is_edited_gift_name_correct_in_item_section(self):
        edited_name_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(name_of_gift_in_items_section))
        print(edited_name_element.text)
        assert edited_name_element.text == new_gift_name_for_edition
