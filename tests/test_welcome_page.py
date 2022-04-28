from pages.welcome_page import WelcomePage


def main_elements_presence_on_welcome_page(driver):
    welcome_page = WelcomePage(driver)
    welcome_page.are_main_elements_present_on_welcome_page()