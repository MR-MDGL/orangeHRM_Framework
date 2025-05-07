import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.login.orange_launch_page import LaunchPage
from PageObject.pim.pim_page import PimPage
from utility.readProperties import ReadConfig
from PageObject.pim.orange_pim_page import PIMPage
from utility.log_instance import logger

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

        self.pp.add_new_employee(first_name, middle_name, last_name, employee_id)

        assert True

    def test_add_and_search_employee(self):
        logger.info("===== Starting test_add_and_search_employee =====")
        try:
            base_url = ReadConfig.getApplicationURL()
            logger.info(f"Navigating to base URL: {base_url}")
            self.driver.get(base_url)

            pim = PIMPage(self.driver, self.wait)
            logger.info("Logging in and navigating to PIM page")
            pim.login_and_navigate_to_pim()

            # Add new employee
            logger.info("Adding new employee")
            emp_id = pim.add_employee("John", "Doe", "12345")
            logger.info(f"Employee added with ID: {emp_id}")

            # Search for the added employee
            logger.info(f"Searching for employee with ID: {emp_id}")
            search_results = pim.search_employee(emp_id)
            
            # Verify search results
            logger.info("Verifying search results")
            assert len(search_results) > 0, "Employee not found in search results"
            logger.info("Employee found in search results")

        except Exception as e:
            logger.error(f"Error in test_add_and_search_employee: {str(e)}")
            raise

        finally:
            logger.info("===== Finished test_add_and_search_employee =====\n")
