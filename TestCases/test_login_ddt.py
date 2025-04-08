import os
import time
import pytest
from PageObject.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig
from utility.XLUtils import getRowCount, readData


@pytest.mark.usefixtures("setup")
class TestLoginDDT:
    def test_login_ddt(self):
        base_url = ReadConfig.getApplicationURL()
        self.driver.get(base_url)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        excel_path = os.path.join(project_root, "TestData", "orangehrm_login.xlsx")
        lp = LaunchPage(self.driver, self.wait)
        rows = getRowCount(excel_path, "Sheet1")
        results_list = []                   # to store final results passed of failed
        for r in range(2, rows + 1):        #iterating over the table
            username = readData(excel_path, "Sheet1", r, 1)
            password = readData(excel_path, "Sheet1", r, 2)
            expected = readData(excel_path, "Sheet1", r, 3)

            lp.enter_username(username)
            lp.enter_password(password)
            lp.click_login()
            time.sleep(2)

            if expected.lower() == "valid":
                if "dashboard" in self.driver.current_url.lower():
                    results_list.append("Pass")
                    self.driver.get(base_url)
                else:
                    results_list.append("Fail")
            elif expected.lower() == "invalid":
                if "dashboard" in self.driver.current_url.lower():
                    results_list.append("Fail")
                    self.driver.get(base_url)
                else:
                    results_list.append("Pass")

            self.driver.delete_all_cookies() # to delete cookies created during execution

        if "Fail" in results_list:  #if fail into the list then testcase fails else pass
            assert False, "Data-Driven Test Failed"
        else:
            assert True, "Data-Driven Test Passed"
