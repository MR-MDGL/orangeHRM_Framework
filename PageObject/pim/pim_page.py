import os
import time
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class PimPage:
    pim_menu_xpath = "//span[text()='PIM']"
    add_employee_xpath = "//a[text()='Add Employee']"
    first_name_xpath = "//input[@name='firstName']"
    middle_name_xpath = "//input[@name='middleName']"
    last_name_xpath = "//input[@name='lastName']"
    employee_id_xpath = "//div[contains(@class,'oxd-input-group')]//input[@class='oxd-input oxd-input--active']"
    file_input_xpath = "//input[@type='file']"
    save_button_xpath = "//button[@type='submit']"
    search_employee_xpath = "//input[@placeholder='Type for hints...']"
    search_button_xpath = "//button[@type='submit']"
    employee_list_xpath = "//div[@class='oxd-table-body']"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def clear_field(self, element):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)

    def navigate_to_pim(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_menu_xpath))).click()

    def click_add_employee(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_employee_xpath))).click()

    def enter_first_name(self, first_name):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.first_name_xpath)))
        field.clear()
        field.send_keys(first_name)

    def enter_middle_name(self, middle_name):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.middle_name_xpath)))
        field.clear()
        field.send_keys(middle_name)

    def enter_last_name(self, last_name):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.last_name_xpath)))
        field.clear()
        field.send_keys(last_name)

    def enter_employee_id(self, emp_id):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.employee_id_xpath)))
        self.clear_field(field)
        field.send_keys(emp_id)

    def upload_image(self):
        project_root = Path(__file__).resolve().parents[2]
        image_path = project_root / "TestData" / "profile.png"
        upload_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.file_input_xpath)))
        upload_input.send_keys(str(image_path))

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath))).click()
        time.sleep(1)

    def add_new_employee(self, first_name, middle_name, last_name, emp_id):
        self.navigate_to_pim()
        self.click_add_employee()
        self.enter_first_name(first_name)
        self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        self.enter_employee_id(emp_id)
        # self.upload_image()
        self.click_save()

    def search_employee(self, name):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_employee_xpath)))
        field.clear()
        field.send_keys(name)

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))).click()

    def verify_employee_exists(self, name):
        try:
            table = self.wait.until(EC.presence_of_element_located((By.XPATH, self.employee_list_xpath)))
            return name.lower() in table.text.lower()
        except:
            return False
