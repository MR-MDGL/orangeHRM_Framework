import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PageObject.orange_launch_page import LaunchPage
from PageObject.my_info_page import MyInfoPage
from utility.readProperties import ReadConfig

USERNAME = ReadConfig.getUsername()
PASSWORD = ReadConfig.getPassword()


@pytest.mark.usefixtures('setup')
class TestMyInfo:
    def test_update_my_info(self):
        self.wait = WebDriverWait(self.driver, 10)

        # Login using LaunchPage
        lp = LaunchPage(self.driver, self.wait)
        lp.enter_username(USERNAME)
        lp.enter_password(PASSWORD)
        lp.click_login()
        assert "dashboard" in self.driver.current_url.lower(), "Login failed with valid credentials"


        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='My Info']")))


        my_info = MyInfoPage(self.driver)
        my_info.click_my_info_menu()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))


        self.wait.until(EC.presence_of_element_located((By.XPATH, my_info.emp_id_xpath)))


        my_info.set_first_name("987654")
        my_info.set_middle_name("987")
        my_info.set_last_name("654")
        my_info.set_employee_id("09263")
        my_info.set_other_id("456789")
        my_info.set_driver_license("12345")
        time.sleep(2)
        my_info.set_license_expiry("2025-01-01")
        time.sleep(2)
        my_info.select_nationality()
        time.sleep(2)
        my_info.select_marital_status()
        time.sleep(2)
        my_info.select_gender_male()
        time.sleep(2)
        my_info.click_save()

        # Wait until any saving process is complete (example: wait until the save button spinner disappears)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//button[@type='submit']//i")))
        assert True