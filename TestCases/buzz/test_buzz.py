import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.login.orange_launch_page import LaunchPage
from PageObject.buzz.orange_buzz_page import BuzzPage
from utility.readProperties import ReadConfig
from utility.log_instance import logger
import time

@pytest.mark.usefixtures("setup")
class TestBuzz:
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        try:
            self.lp = LaunchPage(self.driver, self.wait)
            self.bp = BuzzPage(self.driver, self.wait)
            time.sleep(3)
            self.username = ReadConfig.getUsername()
            self.password = ReadConfig.getPassword()
            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Buzz']")))

        except Exception as e:
            print(f"Error in class setup: {str(e)}")
            raise

    def test_create_text_post(self):
        logger.info("===== Starting test_create_text_post =====")
        try:
            base_url = ReadConfig.getApplicationURL()
            logger.info(f"Navigating to base URL: {base_url}")
            self.driver.get(base_url)

            buzz = BuzzPage(self.driver, self.wait)
            logger.info("Logging in and navigating to Buzz page")
            buzz.login_and_navigate_to_buzz()

            # Create text post
            post_text = "This is a test post from automated testing!"
            logger.info(f"Creating text post with content: {post_text}")
            buzz.create_text_post(post_text)
            logger.info("Text post created successfully")

            # Verify post
            logger.info("Verifying post creation")
            latest_post = buzz.get_latest_post()
            assert post_text in latest_post, "Post text not found in latest post"
            logger.info("Post verified successfully")

        except Exception as e:
            logger.error(f"Error in test_create_text_post: {str(e)}")
            raise

        finally:
            logger.info("===== Finished test_create_text_post =====\n")

   
