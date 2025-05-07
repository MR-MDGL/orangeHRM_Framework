import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.login.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig
from utility.log_instance import logger

@pytest.mark.usefixtures("setup")
class TestLoginWithLogging:
    
    def test_login_with_valid_credentials(self):
        """Test login with valid credentials"""
        logger.info("===== Starting test_login_with_valid_credentials =====")
        
        try:
            # Get base URL
            base_url = ReadConfig.getApplicationURL()
            logger.info(f"Navigating to base URL: {base_url}")
            self.driver.get(base_url)
            
            # Initialize page object
            logger.info("Initializing login page object")
            lp = LaunchPage(self.driver, self.wait)
            
            # Enter credentials
            logger.info("Entering username and password")
            lp.enter_username(ReadConfig.getUsername())
            lp.enter_password(ReadConfig.getPassword())
            
            # Click login
            logger.info("Clicking login button")
            lp.click_login()
            
            # Verify login success
            logger.info("Verifying successful login")
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']")))
                logger.info("Validation passed: Login successful")
                assert True
            except Exception as e:
                logger.error(f"Validation failed: Login unsuccessful - {str(e)}")
                assert False
                
        except Exception as e:
            logger.error(f"Test failed with error: {str(e)}")
            raise
            
        finally:
            logger.info("===== Finished test_login_with_valid_credentials =====\n") 