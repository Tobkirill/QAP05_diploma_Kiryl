from pages.mylist_page import MyListPage
from pages.create_new_list_page import create_new_list_url
from pages.mylist_page import gift_name
from pages.mylist_page import gift_name_text
from pages.mylist_page import quantity_of_stars_to_rate
from pages.create_new_list_page import CreateNewListPage
from pages.create_new_list_page import name_of_list_field
from pages.create_new_list_page import name_of_list_text
from pages.mylist_page import price_of_item_text
from pages.mylist_page import price_of_item_field
from time import sleep


def test_ability_to_start_creation_of_new_list_from_my_list_page(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.start_creation_of_new_list_from_my_page()
    my_list_page.is_url_correct(create_new_list_url)


def test_ability_to_share_link_to_the_list(driver):
    my_list_page = MyListPage(driver)
    my_list_page.share_list()
    my_list_page.is_share_link_correct()


def test_ability_to_add_item_only_with_filled_obligatory_gift_name(driver):
    my_list_page = MyListPage(driver)
    my_list_page.start_to_add_new_item_to_list()
    my_list_page.fill_in_field(gift_name, gift_name_text)
    my_list_page.save_adding_new_item()
    my_list_page.is_adding_new_item_info_message_present()
    my_list_page.is_gift_name_in_items_section_correct(gift_name_text)


def test_ability_to_edit_item(driver):
    my_list_page = MyListPage(driver)
    my_list_page.start_to_edit_added_item()
    my_list_page.is_edit_mode_contains_new_elements()


def test_ability_to_remove_item_from_list(driver):
    my_list_page = MyListPage(driver)
    my_list_page.start_to_edit_added_item()
    my_list_page.remove_added_item()
    my_list_page.is_removed_item_not_displayed()


def test_ability_to_add_item_with_stars_rating(driver_teardown_remove_item):
    my_list_page = MyListPage(driver_teardown_remove_item)
    my_list_page.fill_in_field(gift_name, gift_name_text)
    my_list_page.rate_item_with_stars(quantity_of_stars_to_rate)
    my_list_page.save_adding_new_item()
    my_list_page.is_star_rating_correct(quantity_of_stars_to_rate)


def test_ability_to_add_item_with_price(driver_teardown_remove_item):
    my_list_page = MyListPage(driver_teardown_remove_item)
    my_list_page.fill_in_field(gift_name, gift_name_text)
    my_list_page.fill_in_field(price_of_item_field, price_of_item_text)
    my_list_page.save_adding_new_item()
    my_list_page.is_price_of_item_correct_and_displayed(price_of_item_text)




