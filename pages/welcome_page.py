from pages.base_page import BasePage
from selenium.webdriver.common.by import By

user_name = 'Aaa'
user_name_text = (By.CSS_SELECTOR, '.text-2xl.text-center')
create_list = (By.XPATH, '/html/body/div[2]/main/section[2]/div/div[1]/span[3]/a')
create_list_link = "https://www.giftster.com/list/new/"
start_a_group = (By.XPATH, '/html/body/div[2]/main/section[2]/div/div[2]/span[3]/a')
start_a_group_link = "https://www.giftster.com/group/new/"
join_a_group = (By.XPATH, '/html/body/div[2]/main/section[2]/div/div[3]/span[3]/a')
join_a_group_link = "https://www.giftster.com/search/"


class WelcomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def is_username_correct(self):
        user_name_text_element = self.find_element(user_name_text)
        name_in_username_text_element = user_name_text_element.text[9:]
        print(name_in_username_text_element)
        assert name_in_username_text_element == user_name

    def are_main_elements_present_on_welcome_page(self):
        create_list_element = self.find_element(create_list)
        assert create_list_element.get_attribute('href') == create_list_link
        start_a_group_element = self.find_element(start_a_group)
        assert start_a_group_element.get_attribute('href') == start_a_group_link
        join_a_group_element = self.find_element(join_a_group)
        assert join_a_group_element.get_attribute('href') == join_a_group_link





