from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyInfoPage:
    def __init__(self, driver):
        self.driver = driver

    my_info_menu_xpath = "//span[normalize-space()='My Info']"
    first_name_xpath = "//input[@placeholder='First Name']"
    middle_name_xpath = "//input[@placeholder='Middle Name']"
    last_name_xpath = "//input[@placeholder='Last Name']"
    emp_id_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]"
    other_id_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]"
    driver_license_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]"
    license_expiry_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    nationality_dropdown_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
    marital_status_dropdown_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    gender_male_xpath = "//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']"
    gender_female_xpath = "//label[normalize-space()='Female']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']"
    save_button_xpath = "//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"

    def click_my_info_menu(self):
        self.driver.find_element(By.XPATH, self.my_info_menu_xpath).click()

    def clear_and_input_text(self, xpath, text):
        el = self.driver.find_element(By.XPATH, xpath)
        el.send_keys(Keys.CONTROL + "a")   # Select all text
        el.send_keys(Keys.BACKSPACE)         # Delete selected text
        el.send_keys(text)

    def set_first_name(self, fname):
        self.clear_and_input_text(self.first_name_xpath, fname)

    def set_middle_name(self, mname):
        self.clear_and_input_text(self.middle_name_xpath, mname)

    def set_last_name(self, lname):
        self.clear_and_input_text(self.last_name_xpath, lname)

    def set_employee_id(self, empid):
        self.clear_and_input_text(self.emp_id_xpath, empid)

    def set_other_id(self, otherid):
        self.clear_and_input_text(self.other_id_xpath, otherid)

    def set_driver_license(self, license_num):
        self.clear_and_input_text(self.driver_license_xpath, license_num)

    def set_license_expiry(self, expiry_date):
        # Remove readonly attribute if needed; then use key combo to clear & input text
        expiry_field = self.driver.find_element(By.XPATH, self.license_expiry_xpath)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", expiry_field)
        self.clear_and_input_text(self.license_expiry_xpath, expiry_date)

    def select_nationality(self):
        self.driver.find_element(By.XPATH, self.nationality_dropdown_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='option']//span[text()='Indian']"))
        )
        self.driver.find_element(By.XPATH, "//div[@role='option']//span[text()='Indian']").click()

    def select_marital_status(self):
        self.driver.find_element(By.XPATH, self.marital_status_dropdown_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='option']//span[text()='Unmarried']"))
        )
        self.driver.find_element(By.XPATH, "//div[@role='option']//span[text()='Unmarried']").click()

    def select_gender_male(self):
        self.driver.find_element(By.XPATH, self.gender_male_xpath).click()

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
