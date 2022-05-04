from pages.create_new_list_page import CreateNewListPage
from pages.create_new_list_page import name_of_list_field
from pages.create_new_list_page import add_a_note_field
from pages.mylist_page import MyListPage
from pages.create_new_list_page import create_new_list_url
from time import sleep
from pages.create_new_list_page import first_group_checkbox
from pages.create_new_list_page import public_search_option_gifster_and_google
from pages.create_new_list_page import public_search_option_gifster
from pages.create_new_list_page import public_search_option_share_link
from pages.create_new_list_page import private_list_button
from pages.create_new_list_page import public_list_button
from pages.create_new_list_page import group_list_button
from pages.mylist_page import private_label_in_the_left_menu_text
from pages.mylist_page import public_label_in_the_left_menu_text
from pages.mylist_page import shared_label_in_the_left_menu_text
from pages.mylist_page import private_label_near_settings_text
from pages.mylist_page import public_label_near_settings_text
from pages.mylist_page import shared_label_near_settings_text


name_of_list_text = 'MyList3'
note_text = 'Important Note'


def test_create_list_with_name_obligatory_field(driver_teardown_remove_list):
    create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver_teardown_remove_list)
    my_list_page.is_list_contains_correct_name(name_of_list_text)


def test_create_list_with_name_obligatory_and_note_optional_fields(driver_teardown_remove_list):
    create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.fill_in_field(add_a_note_field, note_text)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver_teardown_remove_list)
    my_list_page.is_list_contains_correct_name(name_of_list_text)
    my_list_page.is_list_contains_correct_note(note_text)


def test_create_list_with_different_background_color(driver_teardown_remove_list):
    create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_simple_color_of_list()
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver_teardown_remove_list)
    my_list_page.is_color_of_list_changed()


def test_ability_to_create_private_list(driver_teardown_remove_list):
    create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_privacy_of_list(private_list_button)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver_teardown_remove_list)
    my_list_page.is_privacy_label_correct(private_label_in_the_left_menu_text, private_label_near_settings_text)


def test_ability_to_create_public_list_with_gifster_and_google_search_option(driver_teardown_remove_list):
    create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_privacy_of_list(public_list_button)
    create_new_list_page.choose_public_search_options(public_search_option_gifster_and_google)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver_teardown_remove_list)
    my_list_page.is_privacy_label_correct(public_label_in_the_left_menu_text, public_label_near_settings_text)


def test_ability_to_create_public_list_with_gifster_search_option(driver_teardown_remove_list):
    create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_privacy_of_list(public_list_button)
    create_new_list_page.is_checkbox_checked(first_group_checkbox)
    create_new_list_page.choose_public_search_options(public_search_option_gifster)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver_teardown_remove_list)
    my_list_page.is_privacy_label_correct(public_label_in_the_left_menu_text, public_label_near_settings_text)


def test_ability_to_create_public_list_with_share_link_option(driver_teardown_remove_list):
    create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_privacy_of_list(public_list_button)
    create_new_list_page.is_checkbox_checked(first_group_checkbox)
    create_new_list_page.choose_public_search_options(public_search_option_gifster)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver_teardown_remove_list)
    my_list_page.is_privacy_label_correct(public_label_in_the_left_menu_text, public_label_near_settings_text)


def test_create_list_with_empty_fields(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.create_new_list()
    create_new_list_page.is_url_correct(create_new_list_url)


def test_create_list_with_empty_name_and_filled_note_field(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(add_a_note_field, note_text)
    create_new_list_page.create_new_list()
    create_new_list_page.is_url_correct(create_new_list_url)


def test_ability_to_create_list_with_chosen_shared_group(driver_teardown_remove_list):
    create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_privacy_of_list(group_list_button)
    create_new_list_page.is_checkbox_checked(first_group_checkbox)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver_teardown_remove_list)
    my_list_page.is_privacy_label_correct(shared_label_in_the_left_menu_text, shared_label_near_settings_text)


def test_ability_to_create_list_with_shared_group_but_group_not_chosen(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_privacy_of_list(group_list_button)
    create_new_list_page.tick_checkbox(first_group_checkbox)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.is_privacy_label_correct(private_label_in_the_left_menu_text, private_label_near_settings_text)



