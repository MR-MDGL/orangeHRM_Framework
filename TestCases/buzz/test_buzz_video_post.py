import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.login.orange_launch_page import LaunchPage
from PageObject.buzz.orange_buzz_page import BuzzPage
from utility.readProperties import ReadConfig
import time
from utility.log_instance import logger

@pytest.mark.usefixtures("setup")
class TestBuzzVideoPost:
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

    def test_post_with_video_url(self):
        logger.info("===== Starting test_post_with_video_url =====")
        try:
            base_url = ReadConfig.getApplicationURL()
            logger.info(f"Navigating to base URL: {base_url}")
            self.driver.get(base_url)

            buzz = BuzzPage(self.driver, self.wait)
            logger.info("Logging in and navigating to Buzz page")
            buzz.login_and_navigate_to_buzz()

            # Create video post
            video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            post_text = "Check out this awesome video!"
            logger.info(f"Creating video post with URL: {video_url}")
            buzz.create_video_post(video_url, post_text)
            logger.info("Video post created successfully")

            # Verify post
            logger.info("Verifying video post")
            latest_post = buzz.get_latest_post()
            assert video_url in latest_post, "Video URL not found in latest post"
            assert post_text in latest_post, "Post text not found in latest post"
            logger.info("Video post verified successfully")

        except Exception as e:
            logger.error(f"Error in test_post_with_video_url: {str(e)}")
            raise

        finally:
            logger.info("===== Finished test_post_with_video_url =====\n") 