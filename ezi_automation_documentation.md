### services page
new employee add that time need to change in scripts
### Allure run commond after report create
 ex:pytest us_store/test_doctors_notes.py --alluredir="./reports"
### Allure report run comond
allure serve "./reports"
## Scroll down by the full height of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
## Scroll up by the full height of the page
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")

## Scroll halfway down
driver.execute_script("window.scrollBy(0, window.innerHeight/2);")
driver.execute_script("window.scrollBy(0, 3000);")

# Scroll halfway up
driver.execute_script("window.scrollBy(0, -window.innerHeight/2);")