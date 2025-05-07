import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
import allure

@pytest.fixture(scope='class')
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    request.cls.driver = driver
    request.cls.wait = wait
    
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    yield driver
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, 'driver', None)
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), 'Screenshots')
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            test_name = item.nodeid.replace('::', '_').replace('/', '_').replace('\\', '_')
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)
            driver.save_screenshot(filepath)
            with open(filepath, "rb") as image_file:
                allure.attach(image_file.read(), name=filename, attachment_type=allure.attachment_type.PNG)
