import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages.login_page import LoginPage
from pages.testing_data.login_page_test_data import email, password
from pages.mylist_page import MyListPageEditItem
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@pytest.fixture(scope="function")
# @pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_in_form_and_login(email, password)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
# @pytest.fixture(scope="session")
def driver_not_logged_in():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
# @pytest.fixture(scope="session")
def driver_teardown_remove_item():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_in_form_and_login(email, password)
    yield driver
    try:
        sleep(1)
        my_list_page = MyListPageEditItem(driver)
        my_list_page.open_my_list_page()
        my_list_page.remove_all_added_items()
        driver.quit()
    except NoSuchElementException or TimeoutException:
        driver.quit()


@pytest.fixture(scope="function")
# @pytest.fixture(scope="session")
def driver_teardown_remove_list():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_in_form_and_login(email, password)
    yield driver
    try:
        my_list_page = MyListPageEditItem(driver)
        my_list_page.open_my_list_page()
        my_list_page.delete_list()
        driver.quit()
    except NoSuchElementException or TimeoutException:
        driver.quit()
