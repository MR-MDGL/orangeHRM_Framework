import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.login.orange_launch_page import LaunchPage
from PageObject.myInfo.my_info_page import MyInfoPage
from utility.readProperties import ReadConfig

@pytest.mark.usefixtures("setup")
class TestMyInfo:
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver, self.wait)
        self.mip = MyInfoPage(self.driver, self.wait)
        
        self.username = ReadConfig.getUsername()
        self.password = ReadConfig.getPassword()
        
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='My Info']")))
    
    def test_update_personal_details(self):
        first_name = "John"
        middle_name = "M"
        last_name = "Doe"
        employee_id = "1234"
        
        self.mip.update_personal_details(first_name, middle_name, last_name, employee_id)
        
        self.mip.navigate_to_my_info()
        time.sleep(2)
        
        first_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.mip.first_name_xpath)))
        assert first_name_field.get_attribute("value") == first_name, "First name not updated correctly"