import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

# Initialize Faker
fake = Faker()

# Create custom markers for Allure report categories (optional)
def pytest_html_report_title(report):
    report.title = "Automation Report"

@pytest.fixture(scope="session")
def pytest_allure_adaptor_exporter_args(parser):
    parser.addoption("--allure-severity", action="store", default=None, help="Set Allure severity label")

# Apply Allure categories to tests using custom markers (optional)
def pytest_collection_modifyitems(config, items):
    for item in items:
        if item.get_closest_marker("severity") is not None:
            severity = item.get_closest_marker("severity").args[0]
            item.add_marker(pytest.mark.allure_label(severity=severity))

# Define a helper function to maximize the browser window and execute tests
def execute_test_with_maximized_screen(driver):
    # Maximize the browser window
    driver.maximize_window()

    driver.get("https://beta.ezi.ma/")
    allure.attach(driver.get_screenshot_as_png(), name="siteload", attachment_type=allure.attachment_type.PNG)

    # Implicit wait
    driver.implicitly_wait(10)

    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_insta=driver.find_element(By.XPATH,"//li[@class='social']//a[1]")
    ActionChains(driver).click(click_insta).perform()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_facebookicon=driver.find_element(By.XPATH,"//body/div[@id='app']/footer[1]/div[1]/div[1]/div[4]/ul[1]/li[2]/a[2]/img[1]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_tiktok=driver.find_element(By.XPATH,"//body/div[@id='app']/footer[1]/div[1]/div[1]/div[4]/ul[1]/li[2]/a[3]/img[1]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_linkdinicon=driver.find_element(By.XPATH,"//body/div[@id='app']/footer[1]/div[1]/div[1]/div[4]/ul[1]/li[2]/a[4]/img[1]").click()
    time.sleep(2)
    driver.back()

    time.sleep(5)

def test_user_flow():
    # Initialize the WebDriver (change the driver path as needed)
    driver = webdriver.Chrome()

    try:
        execute_test_with_maximized_screen(driver)
    finally:
        driver.quit()