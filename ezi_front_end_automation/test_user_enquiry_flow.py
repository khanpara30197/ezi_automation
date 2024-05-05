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

    click_add_your_institue = driver.find_element(By.XPATH, "//a[normalize-space()='Ajoutez votre institut']")
    ActionChains(driver).click(click_add_your_institue).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Header Partner page",attachment_type=allure.attachment_type.PNG)
    click_ezi_for_customer_button=driver.find_element(By.XPATH,"//a[normalize-space()='ezi pour les clients']")
    ActionChains(driver).click(click_ezi_for_customer_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="redirect customer page", attachment_type=allure.attachment_type.PNG)
    click_email_box=driver.find_element(By.XPATH,"//input[@placeholder='Votre adresse e-mail']").send_keys(fake.email())
    click_notifyme_button=driver.find_element(By.XPATH,"//span[@id='basic-email']")
    ActionChains(driver).click(click_notifyme_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="email submit", attachment_type=allure.attachment_type.PNG)
    click_cancel_icon=driver.find_element(By.XPATH,"//button[@aria-label='Close']").click()
    time.sleep(2)
    click_footerparter_link=driver.find_element(By.XPATH,"//a[@href='https://beta.ezi.ma/partner']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Redirect to partner page", attachment_type=allure.attachment_type.PNG)
    #form 1
    click_discover_free_button=driver.find_element(By.XPATH,"//button[normalize-space()='Découcrir gratuitement']")
    ActionChains(driver).click(click_discover_free_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="enquiry form popup open", attachment_type=allure.attachment_type.PNG)
    enter_first_name=driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys(fake.first_name())
    enter_name_of_establsihment=driver.find_element(By.XPATH,"//input[@id='institute']").send_keys("This is testing purpose 1")
    enter_email=driver.find_element(By.XPATH,"//input[@id='email']").send_keys(fake.email())
    enter_phonenumber=driver.find_element(By.XPATH,"//input[@id='telephone_number']").send_keys(fake.phone_number())
    click_city_drop=driver.find_element(By.XPATH,"//select[@id='city_id']")
    select=Select(click_city_drop)
    select.select_by_visible_text("Ben Yakhlef")
    time.sleep(2)
    click_living_room=driver.find_element(By.XPATH,"//select[@id='business_category_id']")
    select1=Select(click_living_room)
    select1.select_by_visible_text("Physiotherapy")
    click_mouth=driver.find_element(By.XPATH,"//select[@id='source_platform_id']")
    select2=Select(click_mouth)
    select2.select_by_visible_text("Facebook")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="first form fill data 1 ",attachment_type=allure.attachment_type.PNG)
    click_submit_button=driver.find_element(By.XPATH,"//button[@type='submit']")
    ActionChains(driver).click(click_submit_button).perform()
    time.sleep(8)
    allure.attach(driver.get_screenshot_as_png(), name="First form submit 1",attachment_type=allure.attachment_type.PNG)
    click_customer_file=driver.find_element(By.XPATH,"//button[@id='pills-4-tab']//p[contains(text(),'Fichier clients')]")
    ActionChains(driver).click(click_customer_file).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_customer_file 1", attachment_type=allure.attachment_type.PNG)
    #form2
    click_try_free2=driver.find_element(By.XPATH,"//div[@id='pills-4']//button[@class='btns yellow_btn'][normalize-space()='Essayer gratuitement']")
    ActionChains(driver).click(click_try_free2).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_try_free2",attachment_type=allure.attachment_type.PNG)
    enter_first_name2 = driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(fake.first_name())
    enter_name_of_establsihment2 = driver.find_element(By.XPATH, "//input[@id='institute']").send_keys("This is testing purpose 2")
    enter_email2 = driver.find_element(By.XPATH, "//input[@id='email']").send_keys(fake.email())
    enter_phonenumber2 = driver.find_element(By.XPATH, "//input[@id='telephone_number']").send_keys(fake.phone_number())
    click_city_drop2 = driver.find_element(By.XPATH, "//select[@id='city_id']")
    select2 = Select(click_city_drop2)
    select2.select_by_visible_text("Casablanca")
    click_living_room2 = driver.find_element(By.XPATH, "//select[@id='business_category_id']")
    select3 = Select(click_living_room2)
    select3.select_by_visible_text("Face care")
    click_mouth2 = driver.find_element(By.XPATH, "//select[@id='source_platform_id']")
    select4 = Select(click_mouth2)
    select4.select_by_visible_text("Instagram")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="first form fill data 2 ",attachment_type=allure.attachment_type.PNG)
    click_submit_button2 = driver.find_element(By.XPATH, "//button[@type='submit']")
    ActionChains(driver).click(click_submit_button2).perform()
    time.sleep(8)
    allure.attach(driver.get_screenshot_as_png(), name="First form submit 2", attachment_type=allure.attachment_type.PNG)
    #form3
    click_try_free3 = driver.find_element(By.XPATH,"//div[@class='col-md-5 sub_admin_left']//button[@class='btns yellow_btn'][normalize-space()='Essayer gratuitement']")
    ActionChains(driver).click(click_try_free3).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_try_free3", attachment_type=allure.attachment_type.PNG)
    enter_first_name3 = driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(fake.first_name())
    enter_name_of_establsihment3 = driver.find_element(By.XPATH, "//input[@id='institute']").send_keys("This is testing purpose 3")
    enter_email3 = driver.find_element(By.XPATH, "//input[@id='email']").send_keys(fake.email())
    enter_phonenumber3 = driver.find_element(By.XPATH, "//input[@id='telephone_number']").send_keys(fake.phone_number())
    click_city_drop3 = driver.find_element(By.XPATH, "//select[@id='city_id']")
    select5 = Select(click_city_drop3)
    select5.select_by_visible_text("Médiouna")
    time.sleep(2)
    click_living_room3 = driver.find_element(By.XPATH, "//select[@id='business_category_id']")
    select6 = Select(click_living_room3)
    select6.select_by_visible_text("Hair Removal")
    click_mouth3 = driver.find_element(By.XPATH, "//select[@id='source_platform_id']")
    select7 = Select(click_mouth3)
    select7.select_by_visible_text("TikTok")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="first form fill data3 ",attachment_type=allure.attachment_type.PNG)
    click_submit_button3 = driver.find_element(By.XPATH, "//button[@type='submit']")
    ActionChains(driver).click(click_submit_button3).perform()
    time.sleep(8)
    allure.attach(driver.get_screenshot_as_png(), name="First form submit 3", attachment_type=allure.attachment_type.PNG)
    #form 4
    click_try_free4 = driver.find_element(By.XPATH,"//section[@class='solution_section']//button[@class='btns yellow_btn'][contains(text(),'Essayer')]")
    ActionChains(driver).click(click_try_free4).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_try_free4", attachment_type=allure.attachment_type.PNG)
    enter_first_name4 = driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(fake.first_name())
    enter_name_of_establsihment4 = driver.find_element(By.XPATH, "//input[@id='institute']").send_keys("This is testing purpose 4")
    enter_email4 = driver.find_element(By.XPATH, "//input[@id='email']").send_keys(fake.email())
    enter_phonenumber4 = driver.find_element(By.XPATH, "//input[@id='telephone_number']").send_keys(fake.phone_number())
    click_city_drop4 = driver.find_element(By.XPATH, "//select[@id='city_id']")
    select8 = Select(click_city_drop4)
    select8.select_by_visible_text("Médiouna")
    time.sleep(2)
    click_living_room4= driver.find_element(By.XPATH, "//select[@id='business_category_id']")
    select9 = Select(click_living_room4)
    select9.select_by_visible_text("English")
    click_mouth4 = driver.find_element(By.XPATH, "//select[@id='source_platform_id']")
    select10 = Select(click_mouth4)
    select10.select_by_visible_text("Youtube")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="first form fill data4 ", attachment_type=allure.attachment_type.PNG)
    click_submit_button4 = driver.find_element(By.XPATH, "//button[@type='submit']")
    ActionChains(driver).click(click_submit_button4).perform()
    time.sleep(8)
    allure.attach(driver.get_screenshot_as_png(), name="First form submit 4",attachment_type=allure.attachment_type.PNG)
    #form5
    click_try_free5 = driver.find_element(By.XPATH,"//div[@class='partner_sec']//button[@class='btns yellow_btn'][contains(text(),'Essayer')]")
    ActionChains(driver).click(click_try_free5).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_try_free5", attachment_type=allure.attachment_type.PNG)
    enter_first_name5 = driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(fake.first_name())
    enter_name_of_establsihment5 = driver.find_element(By.XPATH, "//input[@id='institute']").send_keys("This is testing purpose 5")
    enter_email5 = driver.find_element(By.XPATH, "//input[@id='email']").send_keys(fake.email())
    enter_phonenumber5= driver.find_element(By.XPATH, "//input[@id='telephone_number']").send_keys(fake.phone_number())
    click_city_drop5 = driver.find_element(By.XPATH, "//select[@id='city_id']")
    select11 = Select(click_city_drop5)
    select11.select_by_visible_text("Mohammadia")
    time.sleep(2)
    click_living_room5 = driver.find_element(By.XPATH, "//select[@id='business_category_id']")
    select12 = Select(click_living_room5)
    select12.select_by_visible_text("Aesthetic")
    click_mouth5 = driver.find_element(By.XPATH, "//select[@id='source_platform_id']")
    select13 = Select(click_mouth5)
    select13.select_by_visible_text("Linkedin")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="first form fill data5",attachment_type=allure.attachment_type.PNG)
    click_submit_button5 = driver.find_element(By.XPATH, "//button[@type='submit']")
    ActionChains(driver).click(click_submit_button5).perform()
    time.sleep(8)
    allure.attach(driver.get_screenshot_as_png(), name="First form submit 5", attachment_type=allure.attachment_type.PNG)
    #form6
    click_try_free6 = driver.find_element(By.XPATH,"//button[contains(text(),'Discuter avec un')]")
    ActionChains(driver).click(click_try_free6).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_try_free6", attachment_type=allure.attachment_type.PNG)
    enter_first_name6 = driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(fake.first_name())
    enter_name_of_establsihment6 = driver.find_element(By.XPATH, "//input[@id='institute']").send_keys("This is testing purpose 6")
    enter_email6 = driver.find_element(By.XPATH, "//input[@id='email']").send_keys(fake.email())
    enter_phonenumber6 = driver.find_element(By.XPATH, "//input[@id='telephone_number']").send_keys(fake.phone_number())
    click_city_drop6 = driver.find_element(By.XPATH, "//select[@id='city_id']")
    select14 = Select(click_city_drop6)
    select14.select_by_visible_text("Tit Mellil")
    time.sleep(2)
    click_living_room6 = driver.find_element(By.XPATH, "//select[@id='business_category_id']")
    select15 = Select(click_living_room6)
    select15.select_by_visible_text("Spa")
    click_mouth6 = driver.find_element(By.XPATH, "//select[@id='source_platform_id']")
    select16 = Select(click_mouth6)
    select16.select_by_visible_text("Autre")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="first form fill data6",attachment_type=allure.attachment_type.PNG)
    click_submit_button6 = driver.find_element(By.XPATH, "//button[@type='submit']")
    ActionChains(driver).click(click_submit_button5).perform()
    time.sleep(8)
    allure.attach(driver.get_screenshot_as_png(), name="First form submit 6",attachment_type=allure.attachment_type.PNG)
    #form 7
    click_try_free7= driver.find_element(By.XPATH, "//button[contains(text(),'Essayez')]")
    ActionChains(driver).click(click_try_free7).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_try_free7", attachment_type=allure.attachment_type.PNG)
    enter_first_name7 = driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(fake.first_name())
    enter_name_of_establsihment7 = driver.find_element(By.XPATH, "//input[@id='institute']").send_keys("This is testing purpose 7")
    enter_email7 = driver.find_element(By.XPATH, "//input[@id='email']").send_keys(fake.email())
    enter_phonenumber7 = driver.find_element(By.XPATH, "//input[@id='telephone_number']").send_keys(fake.phone_number())
    click_city_drop7 = driver.find_element(By.XPATH, "//select[@id='city_id']")
    select17 = Select(click_city_drop7)
    select17.select_by_visible_text("Guisser")
    time.sleep(2)
    click_living_room7 = driver.find_element(By.XPATH, "//select[@id='business_category_id']")
    select18 = Select(click_living_room7)
    select18.select_by_visible_text("masssage")
    click_mouth7 = driver.find_element(By.XPATH, "//select[@id='source_platform_id']")
    select19 = Select(click_mouth7)
    select19.select_by_visible_text("Google")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="first form fill data7",attachment_type=allure.attachment_type.PNG)
    click_submit_button7 = driver.find_element(By.XPATH, "//button[@type='submit']")
    ActionChains(driver).click(click_submit_button7).perform()
    time.sleep(8)
    allure.attach(driver.get_screenshot_as_png(), name="First form submit 7",attachment_type=allure.attachment_type.PNG)

    time.sleep(10)
    driver.delete_all_cookies()

def test_user_flow():
    # Initialize the WebDriver (change the driver path as needed)
    driver = webdriver.Chrome()

    try:
        execute_test_with_maximized_screen(driver)
    finally:
        driver.quit()
