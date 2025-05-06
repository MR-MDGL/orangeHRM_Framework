# import os
# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from PageObject.login.orange_launch_page import LaunchPage
# from utility.readProperties import ReadConfig
# from utility.XLUtils import getRowCount, readData
#
#
# @pytest.mark.usefixtures("setup")
# class TestLoginDDT:
#
#     def test_login_ddt(self):
#         base_url = ReadConfig.getApplicationURL()
#         self.driver.get(base_url)
#
#         # Construct the absolute path for the Excel file
#         excel_path = os.path.join(os.path.dirname(__file__), '../../TestData/orangehrm.xlsx')
#         excel_path = os.path.abspath(excel_path)
#
#         # Check if the file exists
#         if not os.path.exists(excel_path):
#             pytest.fail(f"Excel file not found: {excel_path}")
#
#         lp = LaunchPage(self.driver, self.wait)
#         rows = getRowCount(excel_path, "Sheet1")
#
#         for r in range(2, rows + 1):
#             username = readData(excel_path, "Sheet1", r, 1)
#             password = readData(excel_path, "Sheet1", r, 2)
#
#             # Skip rows with missing data
#             if not username or not password:
#                 continue
#
#             lp.enter_username(username)
#             lp.enter_password(password)
#             lp.click_login()
#
#             # Wait for the dashboard or login failure
#             try:
#                 WebDriverWait(self.driver, 5).until(
#                     EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
#                 )
#                 print(f"Row {r}: Login successful for username: {username}")
#             except:
#                 print(f"Row {r}: Login failed for username: {username}")
#
#             # Reset for the next iteration
#             self.driver.delete_all_cookies()
#             self.driver.get(base_url)
#












import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PageObject.login.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig
from utility.XLUtils import getRowCount, readData, writeData, fillGreenColor, fillRedColor
@pytest.mark.usefixtures("setup")
class TestLoginDDT:

    def test_login_ddt(self):
        base_url = ReadConfig.getApplicationURL()
        self.driver.get(base_url)

        excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../TestData/orangehrm.xlsx'))

        if not os.path.exists(excel_path):
            pytest.fail(f"Excel file not found: {excel_path}")

        lp = LaunchPage(self.driver, self.wait)
        rows = getRowCount(excel_path, "Sheet1")
        actual_col = 4  # Column D (index starts at 1)

        for r in range(2, rows + 1):
            username = readData(excel_path, "Sheet1", r, 1)
            password = readData(excel_path, "Sheet1", r, 2)
            expected = readData(excel_path, "Sheet1", r, 3)

            if not username or not password or not expected:
                writeData(excel_path, "Sheet1", r, actual_col, "Fail - Missing Data")
                fillRedColor(excel_path, "Sheet1", r, actual_col)
                continue

            lp.enter_username(username)
            lp.enter_password(password)
            lp.click_login()

            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
                )
                actual_result = "Valid"
            except:
                actual_result = "Invalid"

            if actual_result == expected:
                writeData(excel_path, "Sheet1", r, actual_col, "Pass")
                fillGreenColor(excel_path, "Sheet1", r, actual_col)
            else:
                writeData(excel_path, "Sheet1", r, actual_col, "Fail")
                fillRedColor(excel_path, "Sheet1", r, actual_col)

            self.driver.delete_all_cookies()
            self.driver.get(base_url)
