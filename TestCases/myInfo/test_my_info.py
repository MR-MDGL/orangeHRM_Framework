import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.login.orange_launch_page import LaunchPage
from PageObject.myInfo.my_info_page import MyInfoPage
from utility.readProperties import ReadConfig
from utility.log_instance import logger

@pytest.mark.usefixtures("setup")
class TestMyInfo:
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver, self.wait)
        self.mip = MyInfoPage(self.driver, self.wait)
        
        self.username = ReadConfig.getUsername()
        self.password = ReadConfig.getPassword()
        
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='My Info']")))
    
    def test_update_personal_details(self):
        logger.info("===== Starting test_update_personal_details =====")
        try:
            base_url = ReadConfig.getApplicationURL()
            logger.info(f"Navigating to base URL: {base_url}")
            self.driver.get(base_url)

            my_info = MyInfoPage(self.driver, self.wait)
            logger.info("Logging in and navigating to MyInfo page")
            my_info.login_and_navigate_to_my_info()

            # Update personal details
            logger.info("Updating personal details")
            new_details = {
                "nickname": "Johnny",
                "other_id": "ID123",
                "license_number": "DL456",
                "license_expiry": "2025-12-31",
                "ssn": "123-45-6789",
                "sin": "987654321"
            }
            
            my_info.update_personal_details(new_details)
            logger.info("Personal details updated successfully")

            # Verify updates
            logger.info("Verifying updated details")
            current_details = my_info.get_personal_details()
            for key, value in new_details.items():
                assert current_details[key] == value, f"Mismatch in {key}"
            logger.info("All updates verified successfully")

        except Exception as e:
            logger.error(f"Error in test_update_personal_details: {str(e)}")
            raise

        finally:
            logger.info("===== Finished test_update_personal_details =====\n")
