import pytest
from PageObject.orange_launch_page import LaunchPage
from utility.readProperties import ReadConfig
USERNAME = ReadConfig.getUsername()
PASSWORD = ReadConfig.getPassword()
@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_login_valid(self):
        lp = LaunchPage(self.driver,self.wait)
        lp.enter_username(USERNAME)
        lp.enter_password(PASSWORD)
        lp.click_login()


        assert "dashboard" in self.driver.current_url.lower(), "Login failed with valid credentials"
