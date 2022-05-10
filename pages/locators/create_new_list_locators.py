from selenium.webdriver.common.by import By

name_of_list_field = (By.ID, 'id_privacy-title')
add_a_note_field = (By.ID, 'id_privacy-description')
create_new_list_button = (By.CSS_SELECTOR, '.btn.btn-red-600.btn-snug')
simple_red_color_button = (By.CSS_SELECTOR, ".flex.flex-wrap.justify-center.md\:ml-7>li:nth-child(4)>button")
private_list_button = (By.CSS_SELECTOR, '.flex.border>button:nth-child(1)')
group_list_button = (By.CSS_SELECTOR, '.flex.border>button:nth-child(2)')
public_list_button = (By.CSS_SELECTOR, '.flex.border>button:nth-child(3)')
first_group_checkbox = (By.ID, 'id_perms-group_0')
public_search_option_gifster_and_google = (By.ID, 'id_privacy-search_visibility_2')
public_search_option_gifster = (By.ID, 'id_privacy-search_visibility_1')
public_search_option_share_link = (By.ID, 'id_privacy-search_visibility_0')