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

    click_search_salon_button = driver.find_element(By.XPATH, "//input[@id='search_prestation']").send_keys("lipo")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="search salon", attachment_type=allure.attachment_type.PNG)
    click_search_name = driver.find_element(By.XPATH, "//li[@class='list-group-item formulation_concentration_item getData']").click()
    allure.attach(driver.get_screenshot_as_png(), name="search name", attachment_type=allure.attachment_type.PNG)
    click_search_icon = driver.find_element(By.XPATH, "//button[@id='search_home']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="redirect to search page",attachment_type=allure.attachment_type.PNG)
    # Selected service(s)Page
    click_haircut_reserver_button = driver.find_element(By.XPATH, "//a[@data-service='Hair Cut']").click()
    allure.attach(driver.get_screenshot_as_png(), name="haircut reserver button click",attachment_type=allure.attachment_type.PNG)
    select_professional = driver.find_element(By.XPATH, "//select[@id='selectedProfessional0']").click()
    allure.attach(driver.get_screenshot_as_png(), name="professional click", attachment_type=allure.attachment_type.PNG)
    select_professional_name = driver.find_element(By.XPATH, "//option[@value='Vishal Bhai']").click()
    allure.attach(driver.get_screenshot_as_png(), name="select professional name",attachment_type=allure.attachment_type.PNG)
    click_add_a_service_afterwards = driver.find_element(By.CLASS_NAME,"btns.dark_btns.add_service").click()
    allure.attach(driver.get_screenshot_as_png(), name="click_add_a_service_afterwards",attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    select_another_category=driver.find_element(By.CLASS_NAME,"selectize-input.items.not-full.has-options").click()
    allure.attach(driver.get_screenshot_as_png(), name="select_another_category",attachment_type=allure.attachment_type.PNG)
    select_category=driver.find_element(By.XPATH,"//div[normalize-space()='Clean Shave']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="select_category",attachment_type=allure.attachment_type.PNG)
    click_category = driver.find_element(By.CLASS_NAME,"form-select.form-select-category")
    select1 = Select(click_category)
    select1.select_by_visible_text("face")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="select_category_option",attachment_type=allure.attachment_type.PNG)
    select_face_clean_shave = driver.find_element(By.XPATH, "//a[@data-service='Clean Shave']")
    ActionChains(driver).click(select_face_clean_shave).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="select_face_clean_shave",attachment_type=allure.attachment_type.PNG)
    select_date = driver.find_element(By.XPATH, "//label[@for='18-May']")
    ActionChains(driver).click(select_date).perform()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="select_date", attachment_type=allure.attachment_type.PNG)
    select_time = driver.find_element(By.XPATH, "//a[normalize-space()='09:00']")
    ActionChains(driver).click(select_time).perform()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="select_time", attachment_type=allure.attachment_type.PNG)
    click_date_modifier = driver.find_element(By.XPATH,"//a[@href='https://beta.ezi.ma/lipo-slim-centre/reservation']").click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="date modifier page", attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(5)
    click_login_button=driver.find_element(By.XPATH,"//a[@id='hidealready']")
    ActionChains(driver).click(click_login_button).perform()
    allure.attach(driver.get_screenshot_as_png(), name="click_login_button",attachment_type=allure.attachment_type.PNG)
    click_email_filled = driver.find_element(By.XPATH,"//form[@id='loginform']//input[@name='email']").send_keys("khanpara30197@gmail.com")
    click_password_filled=driver.find_element(By.ID,"password_other").send_keys("testing@123")
    click_view_password=driver.find_element(By.ID,"show-password-toggle").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="login details show", attachment_type=allure.attachment_type.PNG)
    click_login_button=driver.find_element(By.CLASS_NAME,"card_dark_btn.loginbtn").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_login_button", attachment_type=allure.attachment_type.PNG)
    click_complementry_textbox = driver.find_element(By.ID,"complement").send_keys("I am Ravi Khanpara This is testing purpose")
    allure.attach(driver.get_screenshot_as_png(), name="click_complementry_textbox",attachment_type=allure.attachment_type.PNG)
    click_identification_modifier=driver.find_element(By.XPATH,"//a[@class='editregisterdata']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name=" click_identification_modifier",attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    click_confirmer_button=driver.find_element(By.CLASS_NAME,"btns.dark_btns.alreadylogin").click()
    allure.attach(driver.get_screenshot_as_png(), name=" click_confirmer_button",attachment_type=allure.attachment_type.PNG)
    click_confirm_appointment=driver.find_element(By.XPATH,"//a[@class='btns dark_btns']")
    ActionChains(driver).click(click_confirmer_button).perform()
    allure.attach(driver.get_screenshot_as_png(), name="click_confirm_appointment",attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

    time.sleep(10)
    driver.delete_all_cookies()


def test_user_flow():
    # Initialize the WebDriver (change the driver path as needed)
    driver = webdriver.Chrome()

    try:
        execute_test_with_maximized_screen(driver)
    finally:
        driver.quit()