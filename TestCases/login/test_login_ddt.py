import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
from datetime import datetime
import os

from PageObject.login.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig
from utility.XLUtils import getRowCount, readData, writeData, fillGreenColor, fillRedColor


@pytest.mark.usefixtures("setup")
class TestLoginDDT:

    @allure.step("Taking screenshot: {name}")
    def take_screenshot(self, name):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_name = f"fail screenshot login_{timestamp}.png"
        screenshot_path = os.path.join("Screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        # Attach screenshot to Allure report
        with open(screenshot_path, "rb") as file:
            allure.attach(
                file.read(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG
            )
        return screenshot_path

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Login Data Driven Test")
    @allure.description("Test login functionality with different credentials from Excel file")
    def test_login_ddt(self):
        try:
            base_url = ReadConfig.getApplicationURL()
            self.driver.get(base_url)

            # Use relative path for Excel file
            excel_path = os.path.join("TestData", "orangehrm.xlsx")
            lp = LaunchPage(self.driver, self.wait)
            rows = getRowCount(excel_path, "Sheet1")
            results_list = []
            actual_result_col = 4

            for r in range(2, rows + 1):
                with allure.step(f"Testing login with data from row {r}"):
                    username = readData(excel_path, "Sheet1", r, 1)
                    password = readData(excel_path, "Sheet1", r, 2)
                    expected = readData(excel_path, "Sheet1", r, 3)

                    # Validate data from Excel
                    if username is None or password is None or expected is None or \
                       str(username).strip() == "" or str(password).strip() == "" or str(expected).strip() == "":
                        error_msg = f"Missing data in row {r}: Username={username}, Password={password}, Expected={expected}"
                        allure.attach(error_msg, name=f"Data Validation Error Row {r}", attachment_type=allure.attachment_type.TEXT)
                        self.take_screenshot("fail")
                        results_list.append("Fail")
                        writeData(excel_path, "Sheet1", r, actual_result_col, "Fail - Missing Data")
                        fillRedColor(excel_path, "Sheet1", r, actual_result_col)
                        continue

                    allure.attach(
                        f"Username: {username}\nPassword: {password}\nExpected: {expected}",
                        name=f"Test Data Row {r}",
                        attachment_type=allure.attachment_type.TEXT
                    )

                    try:
                        lp.enter_username(username)
                        lp.enter_password(password)
                        lp.click_login()

                        wait = WebDriverWait(self.driver, 5)
                        dashboard_xpath = "//span[text()='Dashboard']"
                        wait.until(EC.presence_of_element_located((By.XPATH, dashboard_xpath)))

                        current_url = self.driver.current_url.lower()

                        if expected.lower() == "valid" and "dashboard" in current_url:
                            results_list.append("Pass")
                            writeData(excel_path, "Sheet1", r, actual_result_col, "Pass")
                            fillGreenColor(excel_path, "Sheet1", r, actual_result_col)
                            allure.attach("Login successful", name=f"Step Result Row {r}", attachment_type=allure.attachment_type.TEXT)
                        else:
                            # Take screenshot only if login succeeded when it shouldn't have
                            if "dashboard" in current_url:
                                self.take_screenshot("fail")
                            results_list.append("Fail")
                            writeData(excel_path, "Sheet1", r, actual_result_col, "Fail")
                            fillRedColor(excel_path, "Sheet1", r, actual_result_col)
                            allure.attach(
                                f"Expected: {expected}\nActual: Got to dashboard when shouldn't have",
                                name=f"Failure Details Row {r}",
                                attachment_type=allure.attachment_type.TEXT
                            )

                    except TimeoutException:
                        current_url = self.driver.current_url.lower()
                        
                        if expected.lower() == "invalid" and "dashboard" not in current_url:
                            results_list.append("Pass")
                            writeData(excel_path, "Sheet1", r, actual_result_col, "Pass")
                            fillGreenColor(excel_path, "Sheet1", r, actual_result_col)
                            allure.attach("Invalid login blocked as expected", name=f"Step Result Row {r}", attachment_type=allure.attachment_type.TEXT)
                        else:
                            # Take screenshot only if login failed when it should have succeeded
                            if "dashboard" not in current_url and expected.lower() == "valid":
                                self.take_screenshot("fail")
                            results_list.append("Fail")
                            writeData(excel_path, "Sheet1", r, actual_result_col, "Fail")
                            fillRedColor(excel_path, "Sheet1", r, actual_result_col)
                            allure.attach(
                                f"Expected: {expected}\nActual: Could not reach dashboard when should have",
                                name=f"Failure Details Row {r}",
                                attachment_type=allure.attachment_type.TEXT
                            )

                    finally:
                        self.driver.delete_all_cookies()
                        self.driver.get(base_url)

            if "Fail" in results_list:
                failed_rows = [i+2 for i, result in enumerate(results_list) if result == "Fail"]
                error_message = f"Data-Driven Test Failed for rows: {failed_rows}"
                allure.attach(error_message, name="Test Failure Summary", attachment_type=allure.attachment_type.TEXT)
                pytest.fail(error_message)

        except Exception as e:
            self.take_screenshot("fail")
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            raise
