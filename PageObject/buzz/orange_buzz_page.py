from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class BuzzPage:
    buzz_menu_xpath = "//span[text()='Buzz']"
    post_input_xpath = "//textarea[@placeholder=\"What's on your mind?\"]"
    post_button_xpath = "//button[@type='submit']"
    post_text_xpath = "//div[contains(@class,'orangehrm-buzz-post')]//p[contains(@class,'orangehrm-buzz-post-body-text')]"
    post_container_xpath = "//div[contains(@class, 'oxd-grid-item')]//div[contains(@class, 'oxd-buzz-post')]"
    post_timestamp_xpath = ".//div[contains(@class, 'orangehrm-buzz-post-header')]//time"
    post_author_xpath = ".//div[contains(@class, 'orangehrm-buzz-post-header')]//p"
    share_photos_button_xpath = "//button[normalize-space()='Share Photos']"
    upload_area_xpath = "//div[@class='oxd-file-div oxd-file-div--active']"
    file_input_xpath = "//input[@type='file']"
    upload_modal_share_button_xpath = "//button[normalize-space()='Share']"
    upload_modal_input_xpath = "//div[@class='orangehrm-buzz-modal']//input[@placeholder=\"What's on your mind?\"] | //div[@class='orangehrm-buzz-modal']//textarea[@placeholder=\"What's on your mind?\"]"
    like_btn_xpath = "//div[@class='orangehrm-buzz-newsfeed']//div[1]//div[1]//div[3]//div[1]//div[1]//*[name()='svg']//*[name()='g' and @id='Group']//*[name()='path' and @id='heart']"
    share_icon_xpath = "//button[contains(@class, 'oxd-icon-button') and .//i[contains(@class, 'bi-share')]]"
    share_input_xpath = '//*[@class="oxd-buzz-post oxd-buzz-post--active"]//*[@class="oxd-buzz-post-input"]'
    share_btn_xpath = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/form/div[2]/button"


    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
        self.modal_caption_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[1]/div[2]/div/textarea'
        self.modal_video_url_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/textarea'
       

    def navigate_to_buzz(self):
        try:
            buzz_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.buzz_menu_xpath)))
            buzz_menu.click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.post_input_xpath)))
        except Exception as e:
            print(f"Error navigating to Buzz page: {str(e)}")
            raise

    def enter_post_text(self, text):
        try:
            post_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.post_input_xpath)))
            post_input.click()
            post_input.clear()
            post_input.send_keys(text)
        except Exception as e:
            print(f"Error entering post text: {str(e)}")
            raise

    def click_post_button(self):
        try:
            post_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.post_button_xpath)))
            post_button.click()
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.post_container_xpath)))
        except Exception as e:
            print(f"Error clicking post button: {str(e)}")
            raise

    def create_post(self, text):
        try:
            self.navigate_to_buzz()
            self.enter_post_text(text)
            self.click_post_button()
        except Exception as e:
            print(f"Error creating post: {str(e)}")
            raise

    def verify_post_exists(self, text):
        try:
            post_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, self.post_text_xpath))
            )
            for post in post_elements:
                if text in post.text:
                    print(f"Found post with text: {post.text}")
                    return True
            print(f"Post with text '{text}' not found")
            return False
        except Exception as e:
            print(f"Error verifying post: {str(e)}")
            return False

    def get_post_details(self, text):
        try:
            posts = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.post_container_xpath)))
            for post in posts:
                try:
                    post_text_element = post.find_element(By.XPATH, self.post_text_xpath)
                    if text in post_text_element.text:
                        timestamp = post.find_element(By.XPATH, self.post_timestamp_xpath).text
                        author = post.find_element(By.XPATH, self.post_author_xpath).text
                        return {
                            'text': post_text_element.text,
                            'timestamp': timestamp,
                            'author': author
                        }
                except:
                    continue
            return None
        except Exception as e:
            print(f"Error getting post details: {str(e)}")
            return None

    def verify_post_order(self, text):
        try:
            posts = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.post_container_xpath)))
            if posts:
                first_post = posts[0]
                post_text_element = first_post.find_element(By.XPATH, self.post_text_xpath)
                return text in post_text_element.text
            return False
        except Exception as e:
            print(f"Error verifying post order: {str(e)}")
            return False

    def upload_photo(self, image_path):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.share_photos_button_xpath))).click()
            upload_area = self.wait.until(EC.presence_of_element_located((By.XPATH, self.upload_area_xpath)))
            file_input = upload_area.find_element(By.XPATH, self.file_input_xpath)
            file_input.send_keys(image_path)
        except Exception as e:
            print(f"Error uploading photo: {str(e)}")
            raise

    def upload_photo_with_message(self, image_path, message):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.share_photos_button_xpath))).click()
            upload_area = self.wait.until(EC.presence_of_element_located((By.XPATH, self.upload_area_xpath)))
            file_input = upload_area.find_element(By.XPATH, self.file_input_xpath)
            file_input.send_keys(image_path)

            modal_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.upload_modal_input_xpath)))
            modal_input.click()
            modal_input.clear()
            modal_input.send_keys(message)

            share_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.upload_modal_share_button_xpath)))
            share_btn.click()
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.post_container_xpath)))
        except Exception as e:
            print(f"Error uploading photo with message: {str(e)}")
            raise

    def create_post_with_image(self, text, image_path):
        try:
            self.navigate_to_buzz()
            self.enter_post_text(text)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.share_photos_button_xpath))).click()
            upload_area = self.wait.until(EC.presence_of_element_located((By.XPATH, self.upload_area_xpath)))
            file_input = upload_area.find_element(By.XPATH, self.file_input_xpath)
            file_input.send_keys(image_path)
            share_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.upload_modal_share_button_xpath)))
            share_btn.click()
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.post_container_xpath)))
        except Exception as e:
            print(f"Error creating post with image: {str(e)}")
            raise

    def post_with_video_url(self, caption_text, video_url):
        try:
            self.navigate_to_buzz()
            time.sleep(2)
            self.click_share_video_button()
            time.sleep(2)
            caption_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.modal_caption_xpath)))
            caption_input.clear()
            caption_input.send_keys(caption_text)
            url_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.modal_video_url_xpath)))
            url_input.clear()
            url_input.send_keys(video_url)
            share_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.upload_modal_share_button_xpath)))
            share_btn.click()
            time.sleep(3)
            print("Video URL post created!")
        except Exception as e:
            print(f"Error posting with video URL: {str(e)}")
            raise

    def click_share_video_button(self):
        share_video_btn_xpath = "//button[normalize-space()='Share Video']"
        share_video_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, share_video_btn_xpath)))
        share_video_btn.click()

    def like_first_post(self):
        try:
            like_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.like_btn_xpath)))
            like_btn.click()
            print("Like button clicked for the first post!")
        except Exception as e:
            print(f"Error clicking like button: {str(e)}")
            raise

    def share_post(self, message):
        try:
            try:
                self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-toast-icon-container")))
            except Exception:
                pass
            buzz_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.buzz_menu_xpath)))
            buzz_menu.click()
            share_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.share_icon_xpath)))
            share_icon.click()
            # Use find_elements and select the second textarea
            share_inputs = self.wait.until(lambda d: d.find_elements(By.XPATH, self.share_input_xpath))
            if len(share_inputs) < 2:
                raise Exception("Could not find the second share input box.")
            share_input = share_inputs[1]
            self.wait.until(lambda d: share_input.is_displayed() and share_input.is_enabled())
            share_input.clear()
            share_input.send_keys(message)
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.share_btn_xpath)))
            share_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.share_btn_xpath)))
            share_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f"Error sharing post: {str(e)}")
            raise

