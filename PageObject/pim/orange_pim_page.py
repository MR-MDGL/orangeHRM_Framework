from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.login.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig
from utility.log_instance import logger

class PIMPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        logger.info("PIMPage object initialized")

    def login_and_navigate_to_pim(self):
        """Login and navigate to PIM page"""
        try:
            lp = LaunchPage(self.driver, self.wait)
            lp.enter_username(ReadConfig.getUsername())
            lp.enter_password(ReadConfig.getPassword())
            lp.click_login()
            
            logger.info("Navigating to PIM page")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']"))).click()
            return True
        except Exception as e:
            logger.error(f"Error in login_and_navigate_to_pim: {str(e)}")
            raise

    def add_employee(self, first_name, last_name, emp_id):
        """Add a new employee"""
        try:
            logger.info(f"Adding employee: {first_name} {last_name}")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()=' Add ']"))).click()
            
            # Enter employee details
            self.wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
            self.wait.until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(last_name)
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='oxd-input oxd-input--active']"))).send_keys(emp_id)
            
            # Save employee
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
            logger.info("Employee details saved")
            
            return emp_id
        except Exception as e:
            logger.error(f"Error in add_employee: {str(e)}")
            raise

    def search_employee(self, emp_id):
        """Search for an employee by ID"""
        try:
            logger.info(f"Searching for employee with ID: {emp_id}")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))).send_keys(emp_id)
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
            
            # Get search results
            results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-card']")))
            logger.info(f"Found {len(results)} search results")
            return results
        except Exception as e:
            logger.error(f"Error in search_employee: {str(e)}")
            raise 