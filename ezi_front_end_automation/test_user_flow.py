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
    click_register_button=driver.find_element(By.XPATH,"//button[normalize-space()='Register']")
    ActionChains(driver).click(click_register_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click register button", attachment_type=allure.attachment_type.PNG)
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
    time.sleep(2)
    select_another_service_option=driver.find_element(By.XPATH,"//div[normalize-space()='Clean Shave']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="select_another_service",attachment_type=allure.attachment_type.PNG)
    click_category=driver.find_element(By.CLASS_NAME,"form-select.form-select-category")
    select1=Select(click_category)
    select1.select_by_visible_text("face")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="select_category_option",attachment_type=allure.attachment_type.PNG)
    select_face_clean_shave=driver.find_element(By.XPATH,"//a[@data-service='Clean Shave']")
    ActionChains(driver).click(select_face_clean_shave).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="select_face_clean_shave", attachment_type=allure.attachment_type.PNG)
    select_date=driver.find_element(By.XPATH,"//label[@for='08-May']")
    ActionChains(driver).click(select_date).perform()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="select_date",attachment_type=allure.attachment_type.PNG)
    select_time=driver.find_element(By.XPATH,"//a[normalize-space()='11:15']")
    ActionChains(driver).click(select_time).perform()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="select_time", attachment_type=allure.attachment_type.PNG)
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
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_show_appointment", attachment_type=allure.attachment_type.PNG)
    logo_click=driver.find_element(By.XPATH,"//img[@src='https://beta.ezi.ma/images/dark-logo.png']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Redirect to home page",attachment_type=allure.attachment_type.PNG)
    #home page category select
    click_face_care_category=driver.find_element(By.XPATH,"//div[@class='link_bar']//a[normalize-space()='Face care']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Redirect to face care category",attachment_type=allure.attachment_type.PNG)
    click_beautiful_see_all_service=driver.find_element(By.XPATH,"//a[@href='https://beta.ezi.ma/face-care/beautiful'][normalize-space()='Voir toutes les prestations']")
    ActionChains(driver).click(click_beautiful_see_all_service).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Redirect to beautiful service",attachment_type=allure.attachment_type.PNG)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    allure.attach(driver.get_screenshot_as_png(), name="Beautiful services page ss",attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(3)
    #most sought after service
    click_physiotherapy=driver.find_element(By.XPATH,"//a[@href='https://beta.ezi.ma/physiotherapy']//div[@class='services_card_images']")
    ActionChains(driver).click(click_physiotherapy).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="physiotherapy",attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    click_search_now_button=driver.find_element(By.XPATH,"//a[normalize-space()='Chercher près de moi']")
    ActionChains(driver).click(click_search_now_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="On click search now button action", attachment_type=allure.attachment_type.PNG)
    click_not_now_button=driver.find_element(By.XPATH,"//a[normalize-space()='Pas maintenant']")
    ActionChains(driver).click(click_not_now_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="On click not now button action",attachment_type=allure.attachment_type.PNG)
    click_take_a_appointment_button=driver.find_element(By.XPATH,"//a[normalize-space()='Je prend rendez-vous']")
    ActionChains(driver).click(click_take_a_appointment_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="On click_take_a_appointment_button action",attachment_type=allure.attachment_type.PNG)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_newsletter_email_box=driver.find_element(By.XPATH,"//input[@placeholder='Entrez votre adresse e-mail']").send_keys("khanpara30197@gmail.com")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="newsletter email address write",attachment_type=allure.attachment_type.PNG)
    click_submit_button=driver.find_element(By.XPATH,"//button[contains(text(),'Je m’abonne')]")
    ActionChains(driver).click(click_submit_button).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="newsletter email submit successfully",attachment_type=allure.attachment_type.PNG)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    #footer section
    click_who_are_you=driver.find_element(By.XPATH,"//a[normalize-space()='Qui sommes nous ?']")
    ActionChains(driver).click(click_who_are_you).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="who are you page",attachment_type=allure.attachment_type.PNG)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    allure.attach(driver.get_screenshot_as_png(), name="who are you page scroll down", attachment_type=allure.attachment_type.PNG)
    time.sleep(3)
    click_contact_page=driver.find_element(By.XPATH,"//a[normalize-space()='Contactez-nous']")
    ActionChains(driver).click(click_contact_page).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="contact us page",attachment_type=allure.attachment_type.PNG)
    enter_phonenumber=driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("+6445184847215")
    enter_message=driver.find_element(By.XPATH,"//textarea[@id='message']").send_keys("I am ravi Khanpara I fill contact form for testing purpose")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="contact form details fill",attachment_type=allure.attachment_type.PNG)
    # click_send_information_button=driver.find_element(By.XPATH,"//button[normalize-space()='Send Information']")
    # ActionChains(driver).click(click_send_information_button).perform()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name="contact form submit successfully",attachment_type=allure.attachment_type.PNG)
    click_blog_page=driver.find_element(By.XPATH,"//a[normalize-space()='Blog']")
    ActionChains(driver).click(click_blog_page).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="blog page",attachment_type=allure.attachment_type.PNG)
    click_any_blog=driver.find_element(By.XPATH,"//a[@href='blogs/sit-dolores-quas']//div[@class='services_card_images']")
    ActionChains(driver).click(click_any_blog).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="open any blog page", attachment_type=allure.attachment_type.PNG)
    click_faq_page=driver.find_element(By.XPATH,"//a[normalize-space()='F.A.Q.']")
    ActionChains(driver).click(click_faq_page).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="click_faq_page", attachment_type=allure.attachment_type.PNG)
    click_any_faq=driver.find_element(By.XPATH,"//button[normalize-space()='Sunt natus maiores voluptatum dolore.']")
    ActionChains(driver).click(click_any_faq).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="slect any faq", attachment_type=allure.attachment_type.PNG)
    click_footer_partner_page=driver.find_element(By.XPATH,"//a[normalize-space()='Devenez partenaire']")
    ActionChains(driver).click(click_footer_partner_page).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="footer partner page", attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_footer_faq_partner=driver.find_element(By.XPATH,"//a[normalize-space()='F.A.Q. Partenaires']")
    ActionChains(driver).click(click_footer_faq_partner).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="footer faq partener page",attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_personal_data=driver.find_element(By.XPATH,"//a[normalize-space()='Données personnelles']")
    ActionChains(driver).click(click_personal_data).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="personal data page",attachment_type=allure.attachment_type.PNG)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_legal_notice=driver.find_element(By.XPATH,"//a[normalize-space()='Mentions légales']")
    ActionChains(driver).click(click_legal_notice).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Legal notice page", attachment_type=allure.attachment_type.PNG)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_insta = driver.find_element(By.XPATH, "//li[@class='social']//a[1]")
    ActionChains(driver).click(click_insta).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="instagram page", attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_facebookicon = driver.find_element(By.XPATH,"//body/div[@id='app']/footer[1]/div[1]/div[1]/div[4]/ul[1]/li[2]/a[2]/img[1]").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="facebook page", attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_tiktok = driver.find_element(By.XPATH,"//body/div[@id='app']/footer[1]/div[1]/div[1]/div[4]/ul[1]/li[2]/a[3]/img[1]").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Tiktok page", attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    click_linkdinicon = driver.find_element(By.XPATH,"//body/div[@id='app']/footer[1]/div[1]/div[1]/div[4]/ul[1]/li[2]/a[4]/img[1]").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Linkdin page", attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(3)
    click_header_instagram=driver.find_element(By.XPATH,"//div[@class='right_header']//li[1]//a[1]")
    ActionChains(driver).click(click_header_instagram).perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Header Instagram page", attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    click_header_facebook=driver.find_element(By.XPATH,"//header/div[1]/div[1]/ul[1]/li[2]/a[1]/img[1]").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Header facebook",attachment_type=allure.attachment_type.PNG)
    driver.back()
    time.sleep(2)
    click_header_tiktok=driver.find_element(By.XPATH,"//header/div[1]/div[1]/ul[1]/li[3]/a[1]/img[1]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Header tiktok", attachment_type=allure.attachment_type.PNG)
    click_header_linkdin=driver.find_element(By.XPATH,"//header/div[1]/div[1]/ul[1]/li[4]/a[1]/img[1]").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Header linkdin", attachment_type=allure.attachment_type.PNG)
    driver.back()
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