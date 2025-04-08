from selenium.webdriver.common.by import By
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
    save_button_xpath = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']"

    def click_my_info_menu(self):
        self.driver.find_element(By.XPATH, self.my_info_menu_xpath).click()

    def set_first_name(self, fname):
        el = self.driver.find_element(By.XPATH, self.first_name_xpath)
        el.clear()
        el.send_keys(fname)

    def set_middle_name(self, mname):
        el = self.driver.find_element(By.XPATH, self.middle_name_xpath)
        el.clear()
        el.send_keys(mname)

    def set_last_name(self, lname):
        el = self.driver.find_element(By.XPATH, self.last_name_xpath)
        el.clear()
        el.send_keys(lname)

    def set_employee_id(self, empid):
        el = self.driver.find_element(By.XPATH, self.emp_id_xpath)
        el.clear()
        el.send_keys(empid)

    def set_other_id(self, otherid):
        el = self.driver.find_element(By.XPATH, self.other_id_xpath)
        el.clear()
        el.send_keys(otherid)

    def set_driver_license(self, license_num):
        el = self.driver.find_element(By.XPATH, self.driver_license_xpath)
        el.clear()
        el.send_keys(license_num)

    def set_license_expiry(self, expiry_date):
        expiry_field = self.driver.find_element(By.XPATH, self.license_expiry_xpath)
        # self.driver.execute_script("arguments[0].removeAttribute('readonly')", expiry_field)
        expiry_field.clear()
        expiry_field.send_keys(expiry_date)

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
