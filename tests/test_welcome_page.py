from pages.welcome_page import WelcomePage


def test_name_on_welcome_page(driver):
    welcome_page = WelcomePage(driver)
    welcome_page.is_username_correct()


def test_main_elements_presence_on_welcome_page(driver):
    welcome_page = WelcomePage(driver)
    welcome_page.are_main_elements_present_on_welcome_page()