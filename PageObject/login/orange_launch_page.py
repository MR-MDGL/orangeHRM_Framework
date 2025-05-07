from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.log_instance import logger

class LaunchPage:
    username_input_xpath = "//input[@name='username']"
    password_input_xpath = "//input[@name='password']"
    login_button_xpath = "//button[@type='submit']"
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        logger.info("LaunchPage object initialized")
    
    def enter_username(self, username):
        """Enter username in the login form"""
        logger.info(f"Entering username: {username}")
        username_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_input_xpath)))
        username_field.clear()
        username_field.send_keys(username)
    
    def enter_password(self, password):
        """Enter password in the login form"""
        logger.info("Entering password")
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.password_input_xpath)))
        password_field.clear()
        password_field.send_keys(password)
    
    def click_login(self):
        """Click the login button"""
        logger.info("Clicking login button")
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button_xpath)))
        login_button.click()
