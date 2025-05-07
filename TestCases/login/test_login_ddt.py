import os
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PageObject.login.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig
from utility.XLUtils import getRowCount, readData, writeData, fillGreenColor, fillRedColor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


@pytest.mark.usefixtures("setup")
class TestLoginDDT:

    def test_login_ddt(self):
        base_url = ReadConfig.getApplicationURL()
        logger.info(f"Navigating to base URL: {base_url}")
        self.driver.get(base_url)

        excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../TestData/orangehrm.xlsx'))

        if not os.path.exists(excel_path):
            logger.error(f"Excel file not found: {excel_path}")
            pytest.fail(f"Excel file not found: {excel_path}")

        logger.info(f"Reading data from Excel file: {excel_path}")
        lp = LaunchPage(self.driver, self.wait)
        rows = getRowCount(excel_path, "Sheet1")
        actual_col = 4  # Column D (index starts at 1)
        logger.info(f"Found {rows} rows of test data in the Excel file")

        for r in range(2, rows + 1):
            username = readData(excel_path, "Sheet1", r, 1)
            password = readData(excel_path, "Sheet1", r, 2)
            expected = readData(excel_path, "Sheet1", r, 3)

            if not username or not password or not expected:
                logger.warning(f"Missing data for row {r}: Username, Password, or Expected result is empty")
                writeData(excel_path, "Sheet1", r, actual_col, "Fail - Missing Data")
                fillRedColor(excel_path, "Sheet1", r, actual_col)
                continue

            logger.info(f"Testing credentials - Username: {username}, Expected: {expected}")
            lp.enter_username(username)
            lp.enter_password(password)
            lp.click_login()

            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
                )
                actual_result = "Valid"
                logger.info(f"Login successful for {username}. Dashboard found.")
            except:
                actual_result = "Invalid"
                logger.warning(f"Login failed for {username}. Dashboard not found.")

            if actual_result == expected:
                logger.info(f"Test passed for {username}. Expected: {expected}, Actual: {actual_result}")
                writeData(excel_path, "Sheet1", r, actual_col, "Pass")
                fillGreenColor(excel_path, "Sheet1", r, actual_col)
            else:
                logger.error(f"Test failed for {username}. Expected: {expected}, Actual: {actual_result}")
                writeData(excel_path, "Sheet1", r, actual_col, "Fail")
                fillRedColor(excel_path, "Sheet1", r, actual_col)

            logger.info(f"Clearing cookies and restarting for next test case.")
            self.driver.delete_all_cookies()
            self.driver.get(base_url)
