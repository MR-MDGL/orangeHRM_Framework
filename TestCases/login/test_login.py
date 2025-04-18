import pytest
from PageObject.login.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig

@pytest.mark.usefixtures("setup")
class TestLogin:
    
    def test_login(self):
        lp = LaunchPage(self.driver, self.wait)
        username = ReadConfig.getUsername()
        password = ReadConfig.getPassword()
        lp.enter_username(username)
        lp.enter_password(password)
        lp.click_login()
