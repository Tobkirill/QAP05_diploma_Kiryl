import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages.login_page import LoginPage
from pages.login_page import email
from pages.login_page import password
from pages.mylist_page import MyListPage
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
    sleep(3)
    driver.quit()


@pytest.fixture(scope="function")
# @pytest.fixture(scope="session")
def driver_not_logged_in():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    sleep(3)
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
        my_list_page = MyListPage(driver)
        my_list_page.open_my_list_page()
        my_list_page.remove_all_added_items()
        sleep(3)
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
        my_list_page = MyListPage(driver)
        my_list_page.open_my_list_page()
        my_list_page.delete_list()
        sleep(3)
        driver.quit()
    except NoSuchElementException or TimeoutException:
        driver.quit()