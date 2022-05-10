from selenium.webdriver.common.by import By

login_page_url = 'https://www.giftster.com/account/login/'
email_field = (By.ID, 'id_username')
password_field = (By.ID, 'id_password')
login_button = (By.CLASS_NAME, 'btn-red-600')
