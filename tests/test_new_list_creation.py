from pages.create_new_list_page import CreateNewListPage
from pages.create_new_list_page import name_of_list_field
from pages.create_new_list_page import add_a_note_field
from pages.mylist_page import MyListPage
from time import sleep

name_of_list_text = 'Testing_name'
note_text = 'Test note'


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

