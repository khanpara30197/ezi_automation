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
    enter_email_address=driver.find_element(By.XPATH,"//div[@class='zip_label_div input-group input']//input[@id='email']").send_keys("khanpara30197@gmail.com")
    enter_password=driver.find_element(By.XPATH,"//div[@class='zip_label_div input-group input pwdbottom']//input[@id='password']").send_keys("testing@123")
    click_show_password=driver.find_element(By.XPATH,"//span[@id='show-password-toggle']").click()
    allure.attach(driver.get_screenshot_as_png(), name="email and password", attachment_type=allure.attachment_type.PNG)
    click_login_button=driver.find_element(By.XPATH,"//button[contains(text(),'Se connecter')]").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="after login", attachment_type=allure.attachment_type.PNG)
    click_my_appointment=driver.find_element(By.XPATH,"//ul[@class='mes_nav']//a[normalize-space()='Mes rendez-vous']").click()
    allure.attach(driver.get_screenshot_as_png(), name="my appointment page", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    click_past_appointment=driver.find_element(By.XPATH,"//a[@id='pills-profile-tab']").click()
    allure.attach(driver.get_screenshot_as_png(), name="past appointment page",attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    click_my_favourites=driver.find_element(By.XPATH,"//ul[@class='mes_nav']//a[normalize-space()='Mes favoris']").click()
    allure.attach(driver.get_screenshot_as_png(), name="my favourites page",attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    click_my_comment=driver.find_element(By.XPATH,"//ul[@class='mes_nav']//a[normalize-space()='Mes commentaires']").click()
    allure.attach(driver.get_screenshot_as_png(), name="my comment page", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    click_my_profile=driver.find_element(By.XPATH,"//ul[@class='mes_nav']//a[normalize-space()='Mon profil']").click()
    allure.attach(driver.get_screenshot_as_png(), name="my profile page", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    click_register_button=driver.find_element(By.XPATH,"//button[normalize-space()='Register']").click()
    allure.attach(driver.get_screenshot_as_png(), name="click register button", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    click_logo=driver.find_element(By.XPATH,"//img[@src='https://beta.ezi.ma/images/dark-logo.png']").click()
    allure.attach(driver.get_screenshot_as_png(), name="On click redirect to home page", attachment_type=allure.attachment_type.PNG)
    time.sleep(3)
    click_search_salon_button=driver.find_element(By.XPATH,"//input[@id='search_prestation']").send_keys("lipo")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="search salon",attachment_type=allure.attachment_type.PNG)
    click_search_name=driver.find_element(By.XPATH,"//li[@class='list-group-item formulation_concentration_item getData']").click()
    allure.attach(driver.get_screenshot_as_png(), name="search name",attachment_type=allure.attachment_type.PNG)
    click_search_icon=driver.find_element(By.XPATH,"//button[@id='search_home']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="redirect to search page",attachment_type=allure.attachment_type.PNG)
    click_hearticon=driver.find_element(By.XPATH,"//div[@class='heart']//*[name()='svg']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="selected hearicon",attachment_type=allure.attachment_type.PNG)
    #Selected service(s)Page
    click_haircut_reserver_button=driver.find_element(By.XPATH,"//a[@data-service='Hair Cut']").click()
    allure.attach(driver.get_screenshot_as_png(), name="haircut reserver button click",attachment_type=allure.attachment_type.PNG)
    select_professional=driver.find_element(By.XPATH,"//select[@id='selectedProfessional0']").click()
    allure.attach(driver.get_screenshot_as_png(), name="professional click",attachment_type=allure.attachment_type.PNG)
    select_professional_name=driver.find_element(By.XPATH,"//option[@value='Vishal Bhai']").click()
    allure.attach(driver.get_screenshot_as_png(), name="select professional name", attachment_type=allure.attachment_type.PNG)
    click_add_a_service_afterwards=driver.find_element(By.XPATH,"//a[normalize-space()='Ajouter une prestation à la suite']").click()
    allure.attach(driver.get_screenshot_as_png(), name="click_add_a_service_afterwards",attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    select_another_service_button=driver.find_element(By.XPATH,"//div[@class='selectize-input items not-full has-options']").click()
    select_another_service_option=driver.find_element(By.XPATH,"//div[normalize-space()='Clean Shave']").click()
    allure.attach(driver.get_screenshot_as_png(), name="select_another_service",attachment_type=allure.attachment_type.PNG)
    click_category=driver.find_element(By.XPATH,"//select[@aria-label='Default select example']").click()
    select_category_option=driver.find_element(By.XPATH,"//option[@value='face']").click()
    allure.attach(driver.get_screenshot_as_png(), name="select_category_option",attachment_type=allure.attachment_type.PNG)
    select_face_clean_shave=driver.find_element(By.XPATH,"//a[@data-service='Clean Shave']").click()
    allure.attach(driver.get_screenshot_as_png(), name="select_face_clean_shave", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    select_date=driver.find_element(By.XPATH,"//label[@for='08-May']").click()
    allure.attach(driver.get_screenshot_as_png(), name="select_date",attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    select_time=driver.find_element(By.XPATH,"//a[normalize-space()='11:15']")
    ActionChains(driver).click(select_time).perform()
    allure.attach(driver.get_screenshot_as_png(), name="select_time", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)
    click_date_modifier=driver.find_element(By.XPATH,"//a[@href='https://beta.ezi.ma/lipo-slim-centre/reservation']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="date modifier page", attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    click_complementry_textbox=driver.find_element(By.XPATH,"//textarea[@id='complement']").send_keys("I am Ravi Khanpara This is testing purpose")
    allure.attach(driver.get_screenshot_as_png(), name="click_complementry_textbox", attachment_type=allure.attachment_type.PNG)
    click_confirm_button=driver.find_element(By.XPATH,"//button[@id='Confirm_button']")
    ActionChains(driver).click(click_confirm_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_confirm",attachment_type=allure.attachment_type.PNG)
    click_show_appointment=driver.find_element(By.XPATH,"//a[@class='btns dark_btns']")
    ActionChains(driver).click(click_show_appointment).perform()
    allure.attach(driver.get_screenshot_as_png(), name="click_show_appointment", attachment_type=allure.attachment_type.PNG)
    logo_click=driver.find_element(By.XPATH,"//img[@src='https://beta.ezi.ma/images/dark-logo.png']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Redirect to home page",attachment_type=allure.attachment_type.PNG)
    #home page category select
    click_face_care_category=driver.find_element(By.XPATH,"//div[@class='link_bar']//a[normalize-space()='Face care']").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 2000);")
    allure.attach(driver.get_screenshot_as_png(), name="Redirect to face care category",attachment_type=allure.attachment_type.PNG)
    click_beautiful_see_all_service=driver.find_element(By.XPATH,"//a[@href='https://beta.ezi.ma/face-care/beautiful'][normalize-space()='Voir toutes les prestations']")
    ActionChains(driver).click(click_beautiful_see_all_service).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Redirect to beautiful service",attachment_type=allure.attachment_type.PNG)
    driver.execute_script("window.scrollBy(0, window.innerHeight/2);")
    allure.attach(driver.get_screenshot_as_png(), name="Beautiful services page ss",attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    #most sought after service
    click_physiotherapy=driver.find_element(By.XPATH,"//a[@href='https://beta.ezi.ma/physiotherapy']//div[@class='card-body']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="physiotherapy",attachment_type=allure.attachment_type.PNG)
    driver.back()
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

# pytest ezi_front_end_automation/test_user_flow.py --alluredir="./reports"