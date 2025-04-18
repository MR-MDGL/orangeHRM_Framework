from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class PimPage:
    pim_menu_xpath = "//span[text()='PIM']"
    add_employee_xpath = "//a[text()='Add Employee']"
    first_name_xpath = "//input[@name='firstName']"
    middle_name_xpath = "//input[@name='middleName']"
    last_name_xpath = "//input[@name='lastName']"
    employee_id_xpath = "//div[contains(@class,'oxd-input-group')]//input[@class='oxd-input oxd-input--active']"
    save_button_xpath = "//button[@type='submit']"
    search_employee_xpath = "//input[@placeholder='Type for hints...']"
    search_button_xpath = "//button[@type='submit']"
    employee_list_xpath = "//div[@class='oxd-table-body']"
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def navigate_to_pim(self):
        pim_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_menu_xpath)))
        pim_menu.click()
    
    def click_add_employee(self):
        add_employee = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_employee_xpath)))
        add_employee.click()
    
    def enter_first_name(self, first_name):
        first_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.first_name_xpath)))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
    
    def enter_middle_name(self, middle_name):
        middle_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.middle_name_xpath)))
        middle_name_field.clear()
        middle_name_field.send_keys(middle_name)
    
    def enter_last_name(self, last_name):
        last_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.last_name_xpath)))
        last_name_field.clear()
        last_name_field.send_keys(last_name)
    
    def enter_employee_id(self, employee_id):
        employee_id_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.employee_id_xpath)))
        employee_id_field.clear()
        employee_id_field.send_keys(Keys.CONTROL + "a")
        employee_id_field.send_keys(Keys.BACKSPACE)
        employee_id_field.send_keys(employee_id)
    
    def click_save(self):
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath)))
        save_button.click()
        time.sleep(2)
    
    def add_new_employee(self, first_name, middle_name, last_name, employee_id):
        self.navigate_to_pim()
        self.click_add_employee()
        self.enter_first_name(first_name)
        self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        self.enter_employee_id(employee_id)
        self.click_save()
    
    def search_employee(self, employee_name):
        search_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_employee_xpath)))
        search_field.clear()
        search_field.send_keys(employee_name)
        time.sleep(1)
    
    def click_search(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_button_xpath)))
        search_button.click()
        time.sleep(2)
    
    def verify_employee_exists(self, employee_name):
        try:
            employee_list = self.wait.until(EC.presence_of_element_located((By.XPATH, self.employee_list_xpath)))
            return employee_name in employee_list.text
        except:
            return False
