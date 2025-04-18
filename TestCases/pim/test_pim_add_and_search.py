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
        first_name = "John"
        middle_name = "M"
        last_name = "Doe"
        employee_id = "1234"
        
        # Add new employee
        self.pp.add_new_employee(first_name, middle_name, last_name, employee_id)
        
        # Verify employee was added by searching
        self.pp.navigate_to_pim()
        self.pp.search_employee(first_name)
        self.pp.click_search()
        
        assert self.pp.verify_employee_exists(first_name), "Employee not found after adding"
    
    def test_search_employee(self):
        """Test case to search for an existing employee"""
        # First add an employee to search for
        first_name = "Jane"
        middle_name = "K"
        last_name = "Smith"
        employee_id = "5678"
        
        # Add new employee first
        self.pp.add_new_employee(first_name, middle_name, last_name, employee_id)
        
        # Now test the search functionality
        self.pp.navigate_to_pim()
        self.pp.search_employee(first_name)
        self.pp.click_search()
        
        assert self.pp.verify_employee_exists(first_name), "Employee not found after search"
