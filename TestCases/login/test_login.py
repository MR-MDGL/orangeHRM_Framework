import pytest
from PageObject.login.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig
from utility.log_instance import logger

@pytest.mark.usefixtures("setup")
class TestLogin:
    
    def test_login(self):
        logger.info("===== Starting test_login =====")
        try:
            base_url = ReadConfig.getApplicationURL()
            logger.info(f"Navigating to base URL: {base_url}")
            self.driver.get(base_url)

            lp = LaunchPage(self.driver, self.wait)
            logger.info("Entering login credentials")
            lp.enter_username(ReadConfig.getUsername())
            lp.enter_password(ReadConfig.getPassword())
            lp.click_login()

            logger.info("===== Finished test_login =====\n")
        except Exception as e:
            logger.error(f"Error in test_login: {e}")
            raise
