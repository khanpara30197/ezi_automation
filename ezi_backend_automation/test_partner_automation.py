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

    #click login button
    click_login_button=driver.find_element(By.XPATH,"//button[@class='btns user_btn']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_login_button", attachment_type=allure.attachment_type.PNG)
    enter_email_address=driver.find_element(By.XPATH,"//div[@class='zip_label_div input-group input']//input[@id='email']").send_keys("partner@ezi.ma")
    enter_password=driver.find_element(By.XPATH,"//div[@class='zip_label_div input-group input pwdbottom']//input[@id='password']").send_keys("ezipartner@2023!")
    click_show_password=driver.find_element(By.XPATH,"//span[@id='show-password-toggle']").click()
    allure.attach(driver.get_screenshot_as_png(), name="email and password", attachment_type=allure.attachment_type.PNG)
    click_login_button=driver.find_element(By.XPATH,"//button[contains(text(),'Se connecter')]").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="after login", attachment_type=allure.attachment_type.PNG)
    click_employee_drawer=driver.find_element(By.XPATH,"//select[@id='employee']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_employee drawer", attachment_type=allure.attachment_type.PNG)
    select_employee_name=driver.find_element(By.XPATH,"//option[normalize-space()='Vishal bhai']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="select_employee_name",attachment_type=allure.attachment_type.PNG)
    click_month_wise_sorting=driver.find_element(By.XPATH,"//button[normalize-space()='month']")
    ActionChains(driver).click(click_month_wise_sorting).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="select_employee_name",attachment_type=allure.attachment_type.PNG)
    # click_month_date=driver.find_element(By.XPATH,"//tbody/tr[4]/td[1]")
    # ActionChains(driver).click(click_month_date).perform()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="Month date select",attachment_type=allure.attachment_type.PNG)
    # click_user_drawer=driver.find_element(By.XPATH,"//select[@id='custmourselect']").click()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="click_user_drawer", attachment_type=allure.attachment_type.PNG)
    # select_user_name=driver.find_element(By.XPATH,"//option[@value='197']").click()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="select_user_name", attachment_type=allure.attachment_type.PNG)
    # click_service_drawer=driver.find_element(By.XPATH,"//select[@name='servicename[]']").click()
    # # ActionChains(driver).click(click_service_drawer).perform()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="click_service_drawer", attachment_type=allure.attachment_type.PNG)
    # select_service_name=driver.find_element(By.XPATH,"//option[@value='4']").click()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="select_service_name",attachment_type=allure.attachment_type.PNG)
    # click_employeedrawer=driver.find_element(By.XPATH,"//select[@name='employee[]']")
    # ActionChains(driver).click(click_employeedrawer).perform()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="click_employeedrawer",attachment_type=allure.attachment_type.PNG)
    # select_employee_name_in_event=driver.find_element(By.XPATH,"//option[normalize-space()='Ezi Vishal bhai']").click()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="select_employee_name_in_event",attachment_type=allure.attachment_type.PNG)
    # click_timing_drawer=driver.find_element(By.XPATH,"//select[@name='stafftime[]']").click()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="click_timing_drawer",attachment_type=allure.attachment_type.PNG)
    # select_time=driver.find_element(By.XPATH,"//option[@value='11:30']").click()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="select_time",attachment_type=allure.attachment_type.PNG)
    # click_add_more_event_button=driver.find_element(By.XPATH,"//button[normalize-space()='Add More Event']")
    # ActionChains(driver).click(click_add_more_event_button).perform()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="click_add_more_event_button", attachment_type=allure.attachment_type.PNG)
    # click_delete_icon=driver.find_element(By.XPATH,"//img[@src='https://beta.ezi.ma/images/delete.png']")
    # ActionChains(driver).click(click_delete_icon).perform()
    # allure.attach(driver.get_screenshot_as_png(), name="click delete icon",attachment_type=allure.attachment_type.PNG)
    # click_save_button=driver.find_element(By.XPATH,"//button[normalize-space()='Save']")
    # ActionChains(driver).click(click_save_button).perform()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="save event", attachment_type=allure.attachment_type.PNG)
    # click_cancel_button=driver.find_element(By.XPATH,"//button[@id='closeModalBtn']")
    # ActionChains(driver).click(click_cancel_button).perform()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="click_cancel_button", attachment_type=allure.attachment_type.PNG)
    click_customer_button=driver.find_element(By.XPATH,"//a[contains(@href,'https://beta.ezi.ma/admin/client')]//div[contains(@class,'image')]//img")
    ActionChains(driver).click(click_customer_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_customer_button",attachment_type=allure.attachment_type.PNG)
    click_importer_button=driver.find_element(By.XPATH,"//button[@id='pills-Importer-tab']")
    ActionChains(driver).click(click_importer_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_importer_button",attachment_type=allure.attachment_type.PNG)
    click_download_button=driver.find_element(By.XPATH,"//a[@id='DownloadCsv']")
    ActionChains(driver).click(click_download_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_download_button",attachment_type=allure.attachment_type.PNG)
    click_clients_button=driver.find_element(By.XPATH,"//button[@id='pills-Clients-tab']")
    ActionChains(driver).click(click_clients_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_client button",attachment_type=allure.attachment_type.PNG)


    time.sleep(5)
    driver.delete_all_cookies()
def test_user_flow():
    # Initialize the WebDriver (change the driver path as needed)
    driver = webdriver.Chrome()

    try:
        execute_test_with_maximized_screen(driver)
    finally:
        driver.quit()