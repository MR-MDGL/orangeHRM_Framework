#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class PimPage():
#     pim_menu_xpath = "//span[text()='PIM']/ancestor::a"
#     add_btn_xpath = "//button[normalize-space()='Add']"
#     first_name_xpath = "//input[@placeholder='First Name']"
#     middle_name_xpath = "//input[@placeholder='Middle Name']"
#     last_name_xpath = "//input[@placeholder='Last Name']"
#     emp_id_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
#     save_btn_xpath = "//button[@type='submit']"
#
#     # Search locators
#     search_emp_id_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
#     search_btn_xpath = "//button[@type='submit']"
#
#     def __init__(self, driver, wait):
#         self.driver = driver
#         self.wait = wait
#
#     def click_pim_menu(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_menu_xpath))).click()
#
#     def click_add_button(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_btn_xpath))).click()
#
#     def enter_first_name(self, first_name):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, self.first_name_xpath))).send_keys(first_name)
#
#     def enter_middle_name(self, middle_name):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, self.middle_name_xpath))).send_keys(middle_name)
#
#     def enter_last_name(self, last_name):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, self.last_name_xpath))).send_keys(last_name)
#
#     def enter_employee_id(self, emp_id):
#         emp_id_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.emp_id_xpath)))
#
#         # Use JavaScript to clear field after delay
#         self.wait.until(lambda driver: emp_id_field.get_attribute("value") != "")  # Wait until the field is auto-filled
#         self.driver.execute_script("arguments[0].value = '';", emp_id_field)  # Clear with JS
#         emp_id_field.send_keys(emp_id)
#
#     def click_save(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_btn_xpath))).click()
#
#     def enter_search_employee_id(self, emp_id):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_emp_id_xpath))).clear()
#         self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_emp_id_xpath))).send_keys(emp_id)
#
#     def click_search_button(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_btn_xpath))).click()




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class PimPage():
    pim_menu_xpath = "//span[text()='PIM']/ancestor::a"
    add_btn_xpath = "//button[normalize-space()='Add']"
    first_name_xpath = "//input[@placeholder='First Name']"
    middle_name_xpath = "//input[@placeholder='Middle Name']"
    last_name_xpath = "//input[@placeholder='Last Name']"
    emp_id_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    save_btn_xpath = "//button[@type='submit']"

    search_emp_id_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    search_btn_xpath = "//button[@type='submit']"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def clear_field(self, element):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)

    def click_pim_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_menu_xpath))).click()

    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_btn_xpath))).click()

    def enter_first_name(self, first_name):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.first_name_xpath)))
        self.clear_field(field)
        field.send_keys(first_name)

    def enter_middle_name(self, middle_name):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.middle_name_xpath)))
        self.clear_field(field)
        field.send_keys(middle_name)

    def enter_last_name(self, last_name):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.last_name_xpath)))
        self.clear_field(field)
        field.send_keys(last_name)

    def enter_employee_id(self, emp_id):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.emp_id_xpath)))
        self.clear_field(field)
        field.send_keys(emp_id)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_btn_xpath))).click()

    def enter_search_employee_id(self, emp_id):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_emp_id_xpath)))
        self.clear_field(field)
        field.send_keys(emp_id)

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_btn_xpath))).click()
