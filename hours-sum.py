import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument()

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://wwtutoring.club/db/protected/pages/WWT_tutor_report_2023-24.php")


# Returns the element with the range of shown entries, unless the range contains the optional parameter.
def find_range(exc=""):
    return driver.find_element(By.XPATH,
                               "/html/body/div/div/section/div[1]/div[2]/section/div/div[3]/div[1]/div[1]/p" +
                               ("[not(text()=\"" + str(exc) + "\")]" if exc else ""))
# p[not(text()="Showing 1 to 200 of 3025 entries")]


init_range = find_range()
init_range_txt = init_range.get_attribute("innerHTML")

# filter by name
l_name_field = driver.find_element(By.ID, "NameFilter")
l_name_field.send_keys("kulikovskiy", Keys.ENTER)

# waits for the new range to be different
print(find_range(exc=init_range_txt).get_attribute("innerHTML"))

time.sleep(5)
