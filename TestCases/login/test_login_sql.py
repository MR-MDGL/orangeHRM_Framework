# import pytest
# import mysql.connector
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from PageObject.login.orange_launch_page import LaunchPage
# from utility.readProperties import ReadConfig
# from utility.log_instance import logger
#
# @pytest.mark.usefixtures("setup")
# class TestLoginSQL:
#     def test_login_db(self):
#         """Test login functionality using test data from MySQL database"""
#         logger.info("===== Starting test_login_db =====")
#
#         connection = None
#         try:
#             base_url = ReadConfig.getApplicationURL()
#             logger.info(f"Connecting to MySQL database")
#             connection = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="root",
#                 database="orange_hrm"
#             )
#             cursor = connection.cursor()
#
#             logger.info("Fetching test users from database")
#             cursor.execute("SELECT username, password FROM test_users")
#             results = []
#
#             for username, password in cursor.fetchall():
#                 logger.info(f"Testing login with username: {username}")
#                 self.driver.get(base_url)
#                 lp = LaunchPage(self.driver, self.wait)
#                 time.sleep(1)
#
#                 lp.enter_username(username)
#                 lp.enter_password(password)
#                 lp.click_login()
#
#                 try:
#                     alert = self.driver.switch_to.alert
#                     alert.accept()
#                     logger.info("Alert detected and accepted")
#                     time.sleep(1)
#                 except Exception:
#                     logger.debug("No alert present")
#                     pass
#
#                 try:
#                     WebDriverWait(self.driver, 5).until(
#                         EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
#                     )
#                     logger.info(f"Login successful for user: {username}")
#                     results.append((username, "PASS"))
#                 except Exception:
#                     try:
#                         WebDriverWait(self.driver, 2).until(
#                             EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Invalid credentials')]"))
#                         )
#                         logger.info(f"Login failed as expected for user: {username}")
#                         results.append((username, "FAIL"))
#                     except Exception:
#                         logger.warning(f"Unexpected state for user: {username}")
#                         self.driver.save_screenshot(f"login_unknown_{username}.png")
#                         results.append((username, "UNKNOWN"))
#
#                 self.driver.delete_all_cookies()
#
#             # Log results summary
#             passes = sum(1 for _, result in results if result == "PASS")
#             fails = sum(1 for _, result in results if result == "FAIL")
#             unknowns = sum(1 for _, result in results if result == "UNKNOWN")
#             logger.info(f"Test Results Summary - Passed: {passes}, Failed: {fails}, Unknown: {unknowns}")
#
#             for username, result in results:
#                 logger.info(f"Final Result - User: {username}, Status: {result}")
#
#             assert all(result == "PASS" for username, result in results), "Some logins failed"
#
#         except Exception as e:
#             logger.error(f"Error in test_login_db: {str(e)}")
#             raise
#
#         finally:
#             if connection:
#                 connection.close()
#                 logger.info("Database connection closed")
#             logger.info("===== Finished test_login_db =====\n")




