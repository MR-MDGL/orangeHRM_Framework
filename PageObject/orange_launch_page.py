from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LaunchPage():
    username_path="//input[@placeholder='Username']"
    password_path="//input[@placeholder='Password']"
    loginBtn_path="//button[@type='submit']"
    def __init__(self,driver,wait):     # driver and wait from my fixture
        self.driver=driver
        self.wait=wait


    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_path)))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.password_path)))
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.loginBtn_path)))
        login_button.click()

