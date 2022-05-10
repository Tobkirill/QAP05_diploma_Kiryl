from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tkinter import Tk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from time import sleep
from selenium.webdriver.support.ui import Select
from pages.locators import my_list_page_locators
from pages.testing_data import my_list_page_test_data


class MyListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_my_list_page(self):
        self.driver.get('https://www.giftster.com/list/')

    def start_creation_of_new_list_from_my_page(self):
        self.find_element(my_list_page_locators.create_new_list_from_my_list_page_button).click()

    def share_list(self):
        self.find_element(my_list_page_locators.share_button).click()

    def is_share_link_correct(self):
        self.find_element(my_list_page_locators.copy_link_button).click()
        copied_text = Tk().clipboard_get()
        url_to_compare = self.driver.current_url.replace('list', 'gift')
        assert copied_text == url_to_compare, f'{copied_text} link is not equal to {url_to_compare}'

    def is_list_contains_correct_name(self, name_of_list):
        name_of_list_in_the_left_menu_element = self.find_element(my_list_page_locators.name_of_list_in_the_left_menu)
        assert name_of_list_in_the_left_menu_element.text == name_of_list, \
            f'{name_of_list_in_the_left_menu_element.text} is not equal to {name_of_list}'
        name_of_list_in_the_center_element = self.find_element(my_list_page_locators.name_of_list_in_the_center)
        assert name_of_list_in_the_center_element.text == name_of_list, \
            f'{name_of_list_in_the_left_menu_element.text} is not equal to {name_of_list}'

    def is_list_contains_correct_note(self, note_of_list):
        note_of_list_in_the_center_element = self.find_element(my_list_page_locators.note_of_list_in_the_center)
        assert note_of_list_in_the_center_element.text == note_of_list,\
            f'{note_of_list_in_the_center_element.text} is not equal to {note_of_list}'

    def is_color_of_list_changed(self):
        section_with_red_background_color_element = self.find_element(
            my_list_page_locators.section_with_red_background_color)
        assert section_with_red_background_color_element.is_displayed(),\
            f'{section_with_red_background_color_element} is not displayed'

    def is_privacy_label_correct(self, privacy_label_in_the_left_menu_text, privacy_label_near_settings_element_text):
        privacy_label_in_the_left_menu_element = self.find_element(my_list_page_locators.privacy_label_in_the_left_menu)
        assert privacy_label_in_the_left_menu_element.text == privacy_label_in_the_left_menu_text, \
            f'{privacy_label_in_the_left_menu_element.text} is not equal to {privacy_label_in_the_left_menu_text}'
        privacy_label_near_settings_element = self.find_element(my_list_page_locators.privacy_label_near_settings)
        assert privacy_label_near_settings_element_text in privacy_label_near_settings_element.text, \
            f'{privacy_label_in_the_left_menu_text} is not in {privacy_label_near_settings_element.text}'

    def is_username_correct(self):
        user_name_element = self.find_element(my_list_page_locators.full_username)
        assert user_name_element.text == my_list_page_test_data.full_username_text, \
            f'{user_name_element.text} is not equal to {my_list_page_test_data.full_username_text}'

    def delete_list(self):
        self.find_element(my_list_page_locators.settings_button).click()
        delete_list_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.delete_list_button))
        delete_list_button_element.click()
        yes_delete_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.yes_delete_button))
        yes_delete_button_element.click()


class MyListPageAddItem(MyListPage):
    def __init__(self, driver):
        self.driver = driver

    def start_of_creation_first_list(self):
        self.find_element(my_list_page_locators.new_list_button).click()

    def is_gift_name_in_items_section_correct(self, name_of_gift):
        name_of_gift_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.name_of_gift_in_items_section))
        assert name_of_gift_in_items_section_element.text == name_of_gift, \
            f'{name_of_gift_in_items_section_element.text} is not equal to {name_of_gift}'

    def start_to_add_new_item_to_list(self):
        add_item_white_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(my_list_page_locators.add_item_white_button))
        add_item_white_button_element.click()

    def start_to_add_one_more_item(self):
        add_item_red_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(my_list_page_locators.add_item_red_button))
        add_item_red_button_element.click()

    def save_adding_new_item(self):
        save_adding_new_item_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.save_adding_new_item_button))
        save_adding_new_item_button_element.click()

    def is_adding_new_item_info_message_present(self):
        adding_new_item_info_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.adding_new_item_info_message))
        assert adding_new_item_info_message_element.text == my_list_page_test_data.adding_new_item_info_message_text, \
            f'{adding_new_item_info_message_element.text} is not equal to ' \
            f'{my_list_page_test_data.adding_new_item_info_message_text}'

    def is_item_section_displayed(self):
        item_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.item_1_section))
        assert item_section_element, 'item_section_element is not displayed'

    def is_item_section_not_displayed(self):
        item_section_element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(my_list_page_locators.item_1_section))
        assert item_section_element, 'item_section_element is displayed'

    def is_item_section_contains_correct_count_of_items(self, expected_count):
        items_section_element = self.find_elements(my_list_page_locators.items_section)
        assert len(items_section_element) == expected_count, 'item_section_elements contains incorrect count of items'

    def rate_item_with_stars(self, quantity_of_stars):
        if quantity_of_stars == 1:
            rate_1_stars_button_element = self.find_element(my_list_page_locators.rate_1_stars_button)
            rate_1_stars_button_element.click()
        if quantity_of_stars == 2:
            rate_2_stars_button_element = self.find_element(my_list_page_locators.rate_2_stars_button)
            rate_2_stars_button_element.click()
        if quantity_of_stars == 3:
            rate_3_stars_button_element = self.find_element(my_list_page_locators.rate_3_stars_button)
            rate_3_stars_button_element.click()
        if quantity_of_stars == 4:
            rate_4_stars_button_element = self.find_element(my_list_page_locators.rate_4_stars_button)
            rate_4_stars_button_element.click()
        if quantity_of_stars == 5:
            rate_5_stars_button_element = self.find_element(my_list_page_locators.rate_5_stars_button)
            rate_5_stars_button_element.click()

    def is_star_in_rating_active(self, star):
        star_element_attributes = self.get_element_attributes(star)
        if star_element_attributes['fill'] == 'currentColor':
            return True
        return False

    def quantity_of_stars_active(self):
        star_1_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.star_1_in_items_section))
        star_2_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.star_2_in_items_section))
        star_3_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.star_3_in_items_section))
        star_4_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.star_4_in_items_section))
        star_5_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.star_5_in_items_section))
        stars = (star_1_in_items_section_element, star_2_in_items_section_element, star_3_in_items_section_element,
                 star_4_in_items_section_element, star_5_in_items_section_element)
        counter = 0
        for element in stars:
            if self.is_star_in_rating_active(element):
                counter += 1
        return counter

    def is_star_rating_correct(self, quantity_of_stars_expected):
        quantity_of_active_stars = self.quantity_of_stars_active()
        assert quantity_of_active_stars == quantity_of_stars_expected, \
            f'{quantity_of_active_stars} is not equal to {quantity_of_stars_expected}'

    def is_price_of_item_correct_and_displayed(self):
        price_of_item_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.price_of_item_in_items_section))
        assert price_of_item_in_items_section_element.text == my_list_page_test_data.price_of_item_text, \
            f'{price_of_item_in_items_section_element.text} is not equal to {my_list_page_test_data.price_of_item_text}'

    def set_quantity_of_items(self, quantity):
        quantity_field_element = self.find_element(my_list_page_locators.quantity_field)
        quantity_field_element.clear()
        quantity_field_element.send_keys(quantity)

    def is_quantity_of_items_displayed_correct(self):
        quantity_of_items_in_items_section_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.quantity_of_items_in_items_section))
        assert quantity_of_items_in_items_section_element.text == my_list_page_test_data.quantity_of_items, \
            f'{quantity_of_items_in_items_section_element.text} is not equal to ' \
            f'{my_list_page_test_data.quantity_of_items}'

    def fetch_link_of_item(self):
        self.find_element(my_list_page_locators.fetch_button).click()

    def is_images_links_fetched_correctly(self):
        image_of_fetched_item_in_the_right_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.image_of_fetched_item_in_the_right))
        assert image_of_fetched_item_in_the_right_element.get_attribute('src') == \
               my_list_page_test_data.image_link_of_fetched_item, \
               f'{image_of_fetched_item_in_the_right_element.get_attribute("src")} is not equal to' \
               f'{my_list_page_test_data.image_link_of_fetched_item}'
        image_of_fetched_item_in_the_below_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.image_of_fetched_item_in_the_below))
        image_of_fetched_item_in_the_below_element.get_attribute('src')
        assert image_of_fetched_item_in_the_below_element.get_attribute('src') == \
               my_list_page_test_data.image_link_of_fetched_item, \
               f'{image_of_fetched_item_in_the_below_element.get_attribute("src")} is not equal to' \
               f'{my_list_page_test_data.image_link_of_fetched_item}'

    def is_add_item_form_populated_with_correct_values(self):
        self.is_field_populated_with_value(my_list_page_locators.web_link_field,
                                           my_list_page_test_data.web_link_to_fetch)
        self.is_field_populated_with_value(my_list_page_locators.gift_name_field,
                                           my_list_page_test_data.name_of_fetched_item)
        self.is_field_populated_with_value(my_list_page_locators.price_of_item_field,
                                           my_list_page_test_data.price_of_fetched_item)
        self.is_field_populated_with_value(my_list_page_locators.where_to_by_field,
                                           my_list_page_test_data.where_to_buy_fetched_item)
        self.is_field_populated_with_value(my_list_page_locators.description_field,
                                           my_list_page_test_data.description_of_fetched_item)
        self.is_images_links_fetched_correctly()

    def cancel_adding_new_item(self):
        self.find_element(my_list_page_locators.cancel_adding_new_item_button).click()

    def get_quantity_of_items_in_list(self):
        try:
            self.driver.switch_to.alert.dismiss()
        except NoAlertPresentException:
            pass
        items_section_element = self.find_elements(my_list_page_locators.items_section)
        return len(items_section_element)

    def start_to_add_image(self):
        self.find_element(my_list_page_locators.add_image_section).click()

    def search_image(self, keyword_for_search):
        web_search_field_in_add_image_pop_up_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.web_search_field_in_add_image_pop_up))
        web_search_field_in_add_image_pop_up_element.send_keys(keyword_for_search)
        start_search_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.start_search_button))
        start_search_button_element.click()

    def choose_image_in_search(self, number_of_image_to_add):
        search_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(my_list_page_locators.search_results))
        sleep(3)
        search_elements[number_of_image_to_add-1].click()

    def upload_chosen_image(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.image_in_the_last_step_of_upload))
        upload_image_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.upload_image_button))
        sleep(5)
        upload_image_button_element.click()

    def close_add_image_pop_up(self):
        try:
            close_add_image_pop_up_button_element = self.find_element(
                my_list_page_locators.close_add_image_pop_up_button)
            close_add_image_pop_up_button_element.click()
        except NoSuchElementException:
            pass

    def get_src_url_of_uploaded_image(self):
        uploaded_image_section_element = self.find_element(my_list_page_locators.uploaded_image_section)
        src_of_uploaded_img = uploaded_image_section_element.get_attribute('src')
        return src_of_uploaded_img

    def is_image_in_items_section_correct(self, expected_url_of_img):
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'[src="{expected_url_of_img}"]'))), \
            'image in items section is incorrect'

    def is_validation_pop_up_with_correct_warning_appeared(self):
        validation_warning_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.validation_warning))
        assert validation_warning_element.text == 'Please enter an item name', \
            "validation pop-up warning is incorrect warning or not appeared"

    def is_alert_displayed_and_could_be_accepted(self):
        assert WebDriverWait(self.driver, 5).until(EC.alert_is_present()), 'alert is not displayed'
        self.driver.switch_to.alert.accept()

    def select_sorting_option(self, option):
        select = Select(self.driver.find_element_by_css_selector('span>select'))
        select.select_by_value(option)

    def sort_items(self):
        sort_items_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.sort_items_button))
        sort_items_button_element.click()

    def is_items_sorted_correct(self, expected_order_of_items):
        elements = self.find_elements(my_list_page_locators.items_section)
        item_names_in_elements = []
        for element in elements:
            item_names_in_elements.append(element.text.split('\n')[0])
        assert item_names_in_elements == expected_order_of_items, \
            f'{item_names_in_elements} is not equal to {expected_order_of_items}'


class MyListPageEditItem(MyListPageAddItem):
    def __init__(self, driver):
        self.driver = driver

    def start_to_edit_added_item(self):
        sleep(1)
        item_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.item_1_section))
        item_element.click()

    def is_edit_mode_contains_new_elements(self):
        remove_item_button_element = self.find_element(my_list_page_locators.remove_item_button)
        assert remove_item_button_element.is_displayed(), 'remove_item_button_element is not displayed'
        copy_item_button_element = self.find_element(my_list_page_locators.copy_item_button)
        assert copy_item_button_element.is_displayed(), 'copy_item_element is not displayed'
        i_got_this_button_element = self.find_element(my_list_page_locators.i_got_this_button)
        assert i_got_this_button_element.is_displayed(), 'i_got_this_button_element is not displayed'

    def remove_added_item(self):
        remove_item_button_element = self.find_element(my_list_page_locators.remove_item_button)
        self.driver.execute_script("arguments[0].click();", remove_item_button_element)

    def is_removed_item_not_displayed(self):
        item_section_element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(my_list_page_locators.item_1_section))
        assert item_section_element, 'item_section_element is not displayed'

    def copy_item_in_edit_mode(self):
        self.find_element(my_list_page_locators.copy_item_button).click()

    def remove_all_added_items(self):
        for i in range(self.get_quantity_of_items_in_list()):
            self.start_to_edit_added_item()
            self.remove_added_item()
            sleep(3)

    def confirm_of_copying_item(self):
        confirm_copy_item_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.confirm_copy_item_button))
        sleep(3)
        confirm_copy_item_button_element.click()

    def is_item_copied(self):
        assert self.get_quantity_of_items_in_list() == 2
        items_in_items_section = self.find_elements(my_list_page_locators.items_section)
        for item in items_in_items_section:
            assert item.text == my_list_page_test_data.gift_name_text +\
                   '\n' + my_list_page_test_data.quantity_of_items,\
                   f'{item.text} is not equal to {my_list_page_test_data.gift_name_text}' \
                   f' + "\n" + {my_list_page_test_data.quantity_of_items}'

    def start_i_got_this_process(self):
        self.find_element(my_list_page_locators.i_got_this_button).click()

    def open_i_got_it_list(self):
        self.find_element(my_list_page_locators.i_got_it_list).click()

    def save_edition_of_item(self):
        self.find_element(my_list_page_locators.save_edition_button).click()

    def cancel_edition_of_item(self):
        self.find_element(my_list_page_locators.cancel_edition_button).click()

    def is_edited_gift_name_correct_in_item_section(self):
        edited_name_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_list_page_locators.name_of_gift_in_items_section))
        assert edited_name_element.text == my_list_page_test_data.new_gift_name_for_edition, \
            f'{edited_name_element.text} is not equal to {my_list_page_test_data.new_gift_name_for_edition}'
