from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LaunchPage:
    username_input_xpath = "//input[@name='username']"
    password_input_xpath = "//input[@name='password']"
    login_button_xpath = "//button[@type='submit']"
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_input_xpath)))
        username_field.clear()
        username_field.send_keys(username)
    
    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.password_input_xpath)))
        password_field.clear()
        password_field.send_keys(password)
    
    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button_xpath)))
        login_button.click()
