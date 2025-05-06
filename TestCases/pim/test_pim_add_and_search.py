import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.login.orange_launch_page import LaunchPage
from PageObject.pim.pim_page import PimPage
from utility.readProperties import ReadConfig

@pytest.mark.usefixtures("setup")
class TestPim:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver, self.wait)
        self.pp = PimPage(self.driver, self.wait)

        self.username = ReadConfig.getUsername()
        self.password = ReadConfig.getPassword()

        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']")))

    def test_add_employee(self):
        """Test case to add a new employee"""
        first_name = "TONY"
        middle_name = "EDWARD"
        last_name = "STARK"
        employee_id = "10082555"

        # Add new employee
        self.pp.add_new_employee(first_name, middle_name, last_name, employee_id)





        assert True
