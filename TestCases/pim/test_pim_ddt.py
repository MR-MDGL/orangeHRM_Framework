import pytest
import os
from PageObject.pim.orange_pim_page import PIMPage
from utility.readProperties import ReadConfig
from utility.XLUtils import getRowCount, readData, writeData, fillGreenColor, fillRedColor
from utility.log_instance import logger

@pytest.mark.usefixtures("setup")
class TestPIMDDT:
    def test_add_multiple_employees(self):
        logger.info("===== Starting test_add_multiple_employees =====")
        try:
            base_url = ReadConfig.getApplicationURL()
            logger.info(f"Navigating to base URL: {base_url}")
            self.driver.get(base_url)

            excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../TestData/employees.xlsx'))
            logger.info(f"Using Excel data file: {excel_path}")

            if not os.path.exists(excel_path):
                logger.error(f"Excel file not found: {excel_path}")
                pytest.fail(f"Excel file not found: {excel_path}")

            pim = PIMPage(self.driver, self.wait)
            logger.info("Logging in and navigating to PIM page")
            pim.login_and_navigate_to_pim()

            rows = getRowCount(excel_path, "Sheet1")
            logger.info(f"Found {rows} employees to add in Excel file")
            status_col = 5  # Column E for status

            for r in range(2, rows + 1):
                first_name = readData(excel_path, "Sheet1", r, 1)
                last_name = readData(excel_path, "Sheet1", r, 2)
                emp_id = readData(excel_path, "Sheet1", r, 3)

                logger.info(f"Adding employee: {first_name} {last_name} (ID: {emp_id})")
                try:
                    pim.add_employee(first_name, last_name, emp_id)
                    logger.info(f"Successfully added employee: {first_name} {last_name}")
                    writeData(excel_path, "Sheet1", r, status_col, "Pass")
                    fillGreenColor(excel_path, "Sheet1", r, status_col)
                except Exception as e:
                    logger.error(f"Failed to add employee {first_name} {last_name}: {str(e)}")
                    writeData(excel_path, "Sheet1", r, status_col, "Fail")
                    fillRedColor(excel_path, "Sheet1", r, status_col)

            logger.info("Completed adding all employees from Excel file")

        except Exception as e:
            logger.error(f"Error in test_add_multiple_employees: {str(e)}")
            raise

        finally:
            logger.info("===== Finished test_add_multiple_employees =====\n")
