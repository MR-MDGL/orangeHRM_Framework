import time

import pytest
from PageObject.orange_launch_page import LaunchPage
from PageObject.pim_page import PimPage
from utility.readProperties import ReadConfig

USERNAME = ReadConfig.getUsername()
PASSWORD = ReadConfig.getPassword()

@pytest.mark.usefixtures('setup')
class TestPim:

    def test_add_and_search_employee(self):
        # Step 1: Login
        lp = LaunchPage(self.driver, self.wait)
        lp.enter_username(USERNAME)
        lp.enter_password(PASSWORD)
        lp.click_login()
        assert "dashboard" in self.driver.current_url.lower(), "Login failed with valid credentials"

        # Step 2: Navigate to PIM
        pim = PimPage(self.driver, self.wait)
        pim.click_pim_menu()

        # Step 3: Add Employee
        pim.click_add_button()
        pim.enter_first_name("temporary employee creation")
        pim.enter_middle_name("testt")
        pim.enter_last_name("Test")
        time.sleep(1)

        pim.enter_employee_id("123")
        time.sleep(1)
        pim.click_save()
        time.sleep(1)

        # Step 4: Go back to PIM (search page)
        pim.click_pim_menu()

        # Step 5: Search employee by ID
        pim.enter_search_employee_id("002")
        pim.click_search_button()
        time.sleep(1)

        # Step 6: Verify employee appears in results
        assert "002" in self.driver.page_source, "Employee ID 002 not found in search results"
