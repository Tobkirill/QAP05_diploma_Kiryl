from pages.create_new_list_page import CreateNewListPage
from pages.create_new_list_page import name_of_list_field
from pages.create_new_list_page import add_a_note_field
from pages.mylist_page import MyListPage
from pages.create_new_list_page import create_new_list_url
from time import sleep
from pages.create_new_list_page import first_group_checkbox

name_of_list_text = 'MyList'
note_text = 'Important Note'


def test_create_list_with_name_obligatory_field(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.is_list_contains_correct_name(name_of_list_text)


def test_create_list_with_name_obligatory_and_note_optional_fields(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.fill_in_field(add_a_note_field, note_text)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.is_list_contains_correct_name(name_of_list_text)
    my_list_page.is_list_contains_correct_note(note_text)


def test_create_list_with_different_background_color(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_simple_color_of_list()
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.is_color_of_list_changed()


def test_ability_to_create_private_list(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_private_list()
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.is_private_label_displayed()


def test_ability_to_create_public_list(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_public_list()
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.is_public_label_displayed()


def test_create_list_with_empty_fields(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.create_new_list()
    create_new_list_page.is_url_remains(create_new_list_url)


def test_create_list_with_empty_name_and_filled_note_field(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(add_a_note_field, note_text)
    create_new_list_page.create_new_list()
    create_new_list_page.is_url_remains(create_new_list_url)


def test_ability_to_create_list_with_chosen_shared_group(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_shared_list()
    create_new_list_page.is_checkbox_checked(first_group_checkbox)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.is_shared_label_displayed()


def test_ability_to_create_list_with_shared_group_and_group_not_chosen(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.open_new_list_page()
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
    create_new_list_page.choose_shared_list()
    create_new_list_page.tick_checkbox(first_group_checkbox)
    create_new_list_page.create_new_list()
    my_list_page = MyListPage(driver)
    my_list_page.is_private_label_displayed()



