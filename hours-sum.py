import re

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# --headless=new causes blank window bug
options.add_argument("--headless=old")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://wwtutoring.club/db/protected/pages/WWT_tutor_report_2023-24.php")
print("Page opened")


# Returns the element with the range of shown entries, unless the range contains the optional parameter.
def find_range(exc=""):
    return driver.find_element(
        By.XPATH,
        "/html/body/div/div/section/div[1]/div[2]/section/div/div[3]/div[1]/div[1]/p"
        + ("[not(text()=\"" + str(exc) + "\")]" if exc else "")
    )


init_range = find_range()
init_range_txt = init_range.get_attribute("innerHTML")

# filter by name
l_name_field = driver.find_element(By.ID, "NameFilter")
l_name_field.send_keys("kulikovskiy", Keys.ENTER)


# waits for the new range to be different
filtered_range = find_range(exc=init_range_txt)
if re.search(r"1 to (\d+) of \1", filtered_range.get_attribute("innerHTML")):
    print("Filtered\nShowing all entries")
else:
    print(filtered_range.get_attribute("innerHTML"))

table = driver.find_element(By.XPATH,
                            "/html/body/div/div/section/div[1]/div[2]/section/div/div[3]/div[3]/div/div/table/tbody")
total_hours = 0
for row in table.find_elements(By.XPATH, './tr'):
    if row.get_attribute("data-id") < "39363":
        continue
    else:
        data = row.find_element(By.XPATH, ".//td[5]").get_attribute("innerHTML").strip()
        if data:
            total_hours += int(data)

print(f"{total_hours} hours")
print(f"${round(total_hours * 17.5, 2)}")

driver.quit()

