import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import os
from datetime import datetime
import allure

@pytest.fixture(scope='class')
def setup(request):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    
    # Initialize the Chrome driver with options
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    # Set up the driver and wait for the class
    request.cls.driver = driver
    request.cls.wait = wait
    
    # Navigate to the application
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Return the driver for cleanup
    yield driver
    
    # Quit the browser
    driver.quit()

def pytest_runtest_logstart(nodeid, location):
    logging.info(f"START: {nodeid}")

def pytest_runtest_logfinish(nodeid, location):
    logging.info(f"END: {nodeid}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, 'driver', None)
        if driver:
            # Create Screenshots directory if it doesn't exist
            screenshots_dir = os.path.join(os.getcwd(), 'Screenshots')
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            # Create a unique filename
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            test_name = item.nodeid.replace('::', '_').replace('/', '_').replace('\\', '_')
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)
            driver.save_screenshot(filepath)
            logging.info(f"Screenshot saved to {filepath}")
            # Attach screenshot to Allure report
            with open(filepath, "rb") as image_file:
                allure.attach(image_file.read(), name=filename, attachment_type=allure.attachment_type.PNG)
