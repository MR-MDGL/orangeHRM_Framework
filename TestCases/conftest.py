import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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
