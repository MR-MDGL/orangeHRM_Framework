import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()
