from pages.create_new_list_page import CreateNewListPage
from pages.create_new_list_page import name_of_list_field

name_of_list_text = 'Testing_name'
note_text = 'Test note'


def test_create__list_with_obligatory_field(driver):
    create_new_list_page = CreateNewListPage(driver)
    create_new_list_page.fill_in_field(name_of_list_field, name_of_list_text)
