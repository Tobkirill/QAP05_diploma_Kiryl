from pages.create_new_list_page import CreateNewListPage
from pages.locators import create_new_list_locators
from pages.mylist_page import MyListPage
from pages.testing_data import my_list_page_test_data
from pages.testing_data.create_new_list_test_data import name_of_list_text, note_text, create_new_list_url
import allure


@allure.feature('Create new list')
def test_create_list_with_name_obligatory_field(driver_teardown_remove_list):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Create list and verify name'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver_teardown_remove_list)
        my_list_page.is_list_contains_correct_name(name_of_list_text)


@allure.feature('Create new list')
def test_create_list_with_name_obligatory_and_note_optional_fields(driver_teardown_remove_list):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Fill in "Note" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.add_a_note_field, note_text)
    with allure.step('Create list and verify name and note'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver_teardown_remove_list)
        my_list_page.is_list_contains_correct_name(name_of_list_text)
        my_list_page.is_list_contains_correct_note(note_text)


@allure.feature('Create new list')
def test_create_list_with_different_background_color(driver_teardown_remove_list):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Choose simple color'):
        create_new_list_page.choose_simple_color_of_list()
    with allure.step('Create list and verify background color'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver_teardown_remove_list)
        my_list_page.is_color_of_list_changed()


@allure.feature('Create new list')
def test_ability_to_create_private_list(driver_teardown_remove_list):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Choose private option'):
        create_new_list_page.choose_privacy_of_list(create_new_list_locators.private_list_button)
    with allure.step('Create list and verify privacy of list'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver_teardown_remove_list)
        my_list_page.is_privacy_label_correct(my_list_page_test_data.private_label_in_the_left_menu_text,
                                              my_list_page_test_data.private_label_near_settings_text)


@allure.feature('Create new list')
def test_ability_to_create_public_list_with_gifster_and_google_search_option(driver_teardown_remove_list):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Choose public option'):
        create_new_list_page.choose_privacy_of_list(create_new_list_locators.public_list_button)
    with allure.step('Choose gifster and google search option'):
        create_new_list_page.choose_public_search_options(
            create_new_list_locators.public_search_option_gifster_and_google)
    with allure.step('Create list and verify privacy of list'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver_teardown_remove_list)
        my_list_page.is_privacy_label_correct(my_list_page_test_data.public_label_in_the_left_menu_text,
                                              my_list_page_test_data.public_label_near_settings_text)


@allure.feature('Create new list')
def test_ability_to_create_public_list_with_gifster_search_option(driver_teardown_remove_list):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Choose public option'):
        create_new_list_page.choose_privacy_of_list(create_new_list_locators.public_list_button)
    with allure.step('Choose gifster search option'):
        create_new_list_page.choose_public_search_options(create_new_list_locators.public_search_option_gifster)
    with allure.step('Create list and verify privacy of list'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver_teardown_remove_list)
        my_list_page.is_privacy_label_correct(my_list_page_test_data.public_label_in_the_left_menu_text,
                                              my_list_page_test_data.public_label_near_settings_text)


@allure.feature('Create new list')
def test_ability_to_create_public_list_with_share_link_option(driver_teardown_remove_list):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Choose public option'):
        create_new_list_page.choose_privacy_of_list(create_new_list_locators.public_list_button)
    with allure.step('Choose share link option'):
        create_new_list_page.choose_public_search_options(create_new_list_locators.public_search_option_share_link)
    with allure.step('Create list and verify privacy of list'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver_teardown_remove_list)
        my_list_page.is_privacy_label_correct(my_list_page_test_data.public_label_in_the_left_menu_text,
                                              my_list_page_test_data.public_label_near_settings_text)


@allure.feature('Create new list')
def test_ability_to_create_list_with_chosen_shared_group(driver_teardown_remove_list):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver_teardown_remove_list)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Choose group option'):
        create_new_list_page.choose_privacy_of_list(create_new_list_locators.group_list_button)
    with allure.step('Choose first group'):
        create_new_list_page.is_checkbox_checked(create_new_list_locators.first_group_checkbox)
    with allure.step('Create list and verify privacy of list'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver_teardown_remove_list)
        my_list_page.is_privacy_label_correct(my_list_page_test_data.shared_label_in_the_left_menu_text,
                                              my_list_page_test_data.shared_label_near_settings_text)


@allure.feature('Create new list')
def test_ability_to_create_list_with_shared_group_but_group_not_chosen(driver):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field, name_of_list_text)
    with allure.step('Choose group option'):
        create_new_list_page.choose_privacy_of_list(create_new_list_locators.group_list_button)
    with allure.step('Untick first group checkbox'):
        create_new_list_page.tick_checkbox(create_new_list_locators.first_group_checkbox)
    with allure.step('Create list and verify privacy of list'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver)
        my_list_page.is_privacy_label_correct(my_list_page_test_data.private_label_in_the_left_menu_text,
                                              my_list_page_test_data.private_label_near_settings_text)


@allure.feature('Create new list')
def test_create_list_with_empty_fields(driver):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver)
        create_new_list_page.open_new_list_page()
    with allure.step('Create list with empty fields and verify current page'):
        create_new_list_page.create_new_list()
        create_new_list_page.is_url_correct(create_new_list_url)


@allure.feature('Create new list')
def test_create_list_with_empty_name_and_filled_note_field(driver):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Note" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.add_a_note_field, note_text)
    with allure.step('Create list with empty fields and verify current page'):
        create_new_list_page.create_new_list()
        create_new_list_page.is_url_correct(create_new_list_url)
