from pages.mylist_page import MyListPage
from pages.mylist_page import MyListPageAddItem
from pages.mylist_page import MyListPageEditItem
from pages.create_new_list_page import CreateNewListPage
from pages.locators import my_list_page_locators
from pages.testing_data import my_list_page_test_data
from pages.locators import create_new_list_locators
from pages.testing_data import create_new_list_test_data
from time import sleep
import allure
import pytest


@allure.feature('Create new list')
def test_ability_to_start_creation_of_new_list_from_my_list_page(driver):
    with allure.step('Open create new list page'):
        create_new_list_page = CreateNewListPage(driver)
        create_new_list_page.open_new_list_page()
    with allure.step('Fill in "Name of list" field'):
        create_new_list_page.fill_in_field(create_new_list_locators.name_of_list_field,
                                           create_new_list_test_data.name_of_list_text)
    with allure.step('Create list'):
        create_new_list_page.create_new_list()
        my_list_page = MyListPage(driver)
    with allure.step('Start creation of new list from My list page and verify current page url'):
        my_list_page.start_creation_of_new_list_from_my_page()
        my_list_page.is_url_correct(create_new_list_test_data.create_new_list_url)


@allure.feature('Create new list')
def test_ability_to_share_link_to_the_list(driver):
    with allure.step('Open my list page'):
        my_list_page = MyListPage(driver)
    with allure.step('Click on "Share list" button'):
        my_list_page.share_list()
    with allure.step('Verify share link'):
        my_list_page.is_share_link_correct()


@allure.feature('Add item to list')
def test_ability_to_add_item_only_with_filled_obligatory_gift_name(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify info message'):
        my_list_page.is_adding_new_item_info_message_present()
    with allure.step('Verify gift name'):
        my_list_page.is_gift_name_in_items_section_correct(my_list_page_test_data.gift_name_text)


@allure.feature('Edit item')
def test_ability_to_start_to_edit_item(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageEditItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to edit item'):
        my_list_page.start_to_edit_added_item()
    with allure.step('Verify elements in edit mode'):
        my_list_page.is_edit_mode_contains_new_elements()


@allure.feature('Edit item')
def test_ability_to_cancel_edit_of_item(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageEditItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to edit item'):
        my_list_page.start_to_edit_added_item()
    with allure.step('Change values in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field_in_edition_mode,
                                   my_list_page_test_data.new_gift_name_for_edition)
    with allure.step('Cancel edition'):
        my_list_page.cancel_edition_of_item()
    with allure.step('Verify display of item section'):
        my_list_page.is_item_section_displayed()
    with allure.step('Verify gift name in items section'):
        my_list_page.is_gift_name_in_items_section_correct(my_list_page_test_data.gift_name_text)


@allure.feature('Edit item')
def test_ability_to_remove_item_from_list(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageEditItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to edit item'):
        my_list_page.start_to_edit_added_item()
    with allure.step('Remove added item'):
        my_list_page.remove_added_item()
    with allure.step('Verify display of recently removed item'):
        my_list_page.is_removed_item_not_displayed()


@allure.feature('Add item to list')
def test_ability_to_add_item_with_stars_rating(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Rate with 3 stars'):
        my_list_page.rate_item_with_stars(my_list_page_test_data.rating_3_stars)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify rating of added item in items section'):
        my_list_page.is_star_rating_correct(my_list_page_test_data.rating_3_stars)


@allure.feature('Add item to list')
def test_ability_to_add_item_with_price(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Fill in "Price" field'):
        my_list_page.fill_in_field(my_list_page_locators.price_of_item_field, my_list_page_test_data.price_of_item_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify price of added item'):
        my_list_page.is_price_of_item_correct_and_displayed()


@allure.feature('Add item to list')
def test_ability_to_add_item_with_increased_quantity(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Set quantity'):
        my_list_page.set_quantity_of_items(my_list_page_test_data.quantity_of_items)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify display of quantity of added item in items section'):
        my_list_page.is_quantity_of_items_displayed_correct()


@allure.feature('Add item to list')
def test_ability_to_add_item_with_where_to_buy_info(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Fill in "Where to buy" field'):
        my_list_page.fill_in_field(my_list_page_locators.where_to_by_field,
                                   my_list_page_test_data.where_to_buy_field_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify display of item section'):
        my_list_page.is_item_section_displayed()


@allure.feature('Add item to list')
def test_ability_to_add_item_with_description(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Fill in "Description" field'):
        my_list_page.fill_in_field(my_list_page_locators.description_field,
                                   my_list_page_test_data.description_of_item_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify display of item section'):
        my_list_page.is_item_section_displayed()


@allure.feature('Add item to list')
def test_ability_to_add_item_with_image(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Start to add image'):
        my_list_page.start_to_add_image()
    with allure.step('Search image by keyword'):
        my_list_page.search_image(my_list_page_test_data.keyword_image_to_search)
    with allure.step('Choose found image'):
        my_list_page.choose_image_in_search(my_list_page_test_data.number_of_image)
    with allure.step('Upload chosen image'):
        my_list_page.upload_chosen_image()
    with allure.step('Close add image pop-up'):
        my_list_page.close_add_image_pop_up()
    with allure.step('Get expected image url'):
        image_of_url_expected = my_list_page.get_src_url_of_uploaded_image()
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify display of items section'):
        my_list_page.is_item_section_displayed()
    with allure.step('Verify url of image in items section'):
        my_list_page.is_image_in_items_section_correct(image_of_url_expected)


@allure.feature('Add item to list')
def test_ability_to_create_item_only_with_optional_fields(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Price" field'):
        my_list_page.fill_in_field(my_list_page_locators.price_of_item_field, my_list_page_test_data.price_of_item_text)
    with allure.step('Fill in "Where to buy" field'):
        my_list_page.fill_in_field(my_list_page_locators.where_to_by_field,
                                   my_list_page_test_data.where_to_buy_field_text)
    with allure.step('Fill in "Description" field'):
        my_list_page.fill_in_field(my_list_page_locators.description_field,
                                   my_list_page_test_data.description_of_item_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify validation pop-up'):
        my_list_page.is_validation_pop_up_with_correct_warning_appeared()


@allure.feature('Add item to list')
@pytest.mark.xfail(reson='Price of item is not fetching')
def test_ability_to_fetch_web_link(driver):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver)
    with allure.step('Web link" field'):
        my_list_page.fill_in_field(my_list_page_locators.web_link_field, my_list_page_test_data.web_link_to_fetch)
    with allure.step('Fetch link'):
        my_list_page.fetch_link_of_item()
    with allure.step('Verify how fields populated with values'):
        sleep(3)
        my_list_page.is_add_item_form_populated_with_correct_values()


@allure.feature('Add item to list')
def test_ability_to_add_item_with_fetched_link(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Web link" field'):
        my_list_page.fill_in_field(my_list_page_locators.web_link_field, my_list_page_test_data.web_link_to_fetch)
    with allure.step('Fetch link'):
        my_list_page.fetch_link_of_item()
    with allure.step('Save new item'):
        sleep(3)
        my_list_page.save_adding_new_item()
    with allure.step('Verify display of items section'):
        my_list_page.is_item_section_displayed()
    with allure.step('Verify display gift name in items section'):
        my_list_page.is_gift_name_in_items_section_correct(my_list_page_test_data.name_of_fetched_item)


@allure.feature('Add item to list')
def test_ability_to_add_more_than_one_item(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to add one more item'):
        sleep(3)
        my_list_page.start_to_add_one_more_item()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Verify count of items in items section'):
        sleep(3)
        my_list_page.is_item_section_contains_correct_count_of_items(2)


@allure.feature('Add item to list')
def test_ability_to_cancel_of_adding_item(driver):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver)
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Cancel of adding new item'):
        my_list_page.cancel_adding_new_item()
    with allure.step('Verify display of items section'):
        my_list_page.is_item_section_not_displayed()


@allure.feature('Edit item')
def test_ability_to_save_changes_after_edition_of_item(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageEditItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to edit item'):
        my_list_page.start_to_edit_added_item()
    with allure.step('Change value in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field_in_edition_mode,
                                   my_list_page_test_data.new_gift_name_for_edition)
    with allure.step('Save edition item'):
        my_list_page.save_edition_of_item()
    with allure.step('Refresh page'):
        sleep(1)
        my_list_page.driver.refresh()
    with allure.step('Verify edited gift name in items section'):
        my_list_page.is_edited_gift_name_correct_in_item_section()


@allure.feature('Edit item')
def test_ability_to_copy_item_to_the_same_list(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageEditItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Set quantity of items'):
        my_list_page.set_quantity_of_items(my_list_page_test_data.quantity_of_items)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to edit item'):
        my_list_page.start_to_edit_added_item()
    with allure.step('Copy item in edit mode'):
        my_list_page.copy_item_in_edit_mode()
    with allure.step('Confirm copy item'):
        my_list_page.confirm_of_copying_item()
    with allure.step('Refresh page'):
        sleep(2)
        my_list_page.driver.refresh()
    with allure.step('Verify is item copied'):
        my_list_page.is_item_copied()


@allure.feature('Sort items')
def test_ability_to_sort_items_by_stars(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Select "Star rating" sorting option'):
        my_list_page.select_sorting_option(my_list_page_test_data.star_rank_sorting_option)
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_with_3_stars)
    with allure.step('Rate item with stars'):
        my_list_page.rate_item_with_stars(my_list_page_test_data.rating_3_stars)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to add one more item'):
        sleep(3)
        my_list_page.start_to_add_one_more_item()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_with_1_star)
    with allure.step('Rate item with stars'):
        my_list_page.rate_item_with_stars(my_list_page_test_data.rating_1_star)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to add one more item'):
        sleep(3)
        my_list_page.start_to_add_one_more_item()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_with_5_stars)
    with allure.step('Rate item with stars'):
        my_list_page.rate_item_with_stars(my_list_page_test_data.rating_5_stars)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Sort items'):
        sleep(3)
        my_list_page.sort_items()
    with allure.step('Verify sorted items by rating'):
        my_list_page.is_items_sorted_correct([my_list_page_test_data.gift_name_with_5_stars,
                                              my_list_page_test_data.gift_name_with_3_stars,
                                              my_list_page_test_data.gift_name_with_1_star])


@allure.feature('Sort items')
def test_ability_to_sort_items_by_newest(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Select "Newest" sorting option'):
        my_list_page.select_sorting_option(my_list_page_test_data.newest_sorting_option)
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_a)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to add one more item'):
        sleep(3)
        my_list_page.start_to_add_one_more_item()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_b)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to add one more item'):
        sleep(3)
        my_list_page.start_to_add_one_more_item()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_c)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Sort items'):
        sleep(3)
        my_list_page.sort_items()
    with allure.step('Verify sorted items by newest'):
        my_list_page.is_items_sorted_correct([my_list_page_test_data.gift_name_c,
                                              my_list_page_test_data.gift_name_b,
                                              my_list_page_test_data.gift_name_a])


@allure.feature('Sort items')
def test_ability_to_sort_items_by_item_name(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageAddItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Select "Item name" sorting option'):
        my_list_page.select_sorting_option(my_list_page_test_data.item_name_sorting_option)
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_b)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to add one more item'):
        sleep(3)
        my_list_page.start_to_add_one_more_item()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_c)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to add one more item'):
        sleep(3)
        my_list_page.start_to_add_one_more_item()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_a)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Sort items'):
        sleep(3)
        my_list_page.sort_items()
    with allure.step('Verify sorted items by item name'):
        my_list_page.is_items_sorted_correct([my_list_page_test_data.gift_name_a,
                                              my_list_page_test_data.gift_name_b,
                                              my_list_page_test_data.gift_name_c])


@allure.feature('Edit item')
def test_interruption_of_editing_item(driver_teardown_remove_item):
    with allure.step('Open my list page'):
        my_list_page = MyListPageEditItem(driver_teardown_remove_item)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to edit item'):
        my_list_page.start_to_edit_added_item()
    with allure.step('Change value of "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field_in_edition_mode,
                                   my_list_page_test_data.new_gift_name_for_edition)
    with allure.step('Refresh page'):
        my_list_page.driver.refresh()
    with allure.step('Verify display of alert and ability to accept'):
        my_list_page.is_alert_displayed_and_could_be_accepted()


@allure.feature('Edit item')
def test_ability_to_set_item_as_i_got_this_item(driver):
    with allure.step('Open my list page'):
        my_list_page = MyListPageEditItem(driver)
    with allure.step('Start to add new item'):
        my_list_page.start_to_add_new_item_to_list()
    with allure.step('Fill in "Gift name" field'):
        my_list_page.fill_in_field(my_list_page_locators.gift_name_field, my_list_page_test_data.gift_name_text)
    with allure.step('Save new item'):
        my_list_page.save_adding_new_item()
    with allure.step('Start to edit item'):
        my_list_page.start_to_edit_added_item()
    with allure.step('Start I got this process'):
        my_list_page.start_i_got_this_process()
    with allure.step('Verify display of item section'):
        my_list_page.is_item_section_not_displayed()
    with allure.step('Refresh page'):
        my_list_page.driver.refresh()
    with allure.step('Open "I got it" list'):
        my_list_page.open_i_got_it_list()
    with allure.step('Verify display of items section'):
        my_list_page.is_item_section_displayed()
    with allure.step('Verify name of item section'):
        my_list_page.is_gift_name_in_items_section_correct(my_list_page_test_data.gift_name_text)
