from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_local_path = "C:\Development"
driver = webdriver.Chrome(executable_path=chrome_local_path)


driver.get("https://www.appbrewery.co/courses")

# more_courses_link = driver.find_element(By.CSS_SELECTOR, "li .fedora-navbar-link")
# facebook_link = driver.find_element(
#     By.XPATH, '//*[@id="contentTable"]/tbody/tr/td/table/tbody/tr[18]/td/a[2]'
# )
# # for link in more_courses_link:
# print(facebook_link.get_attribute("href"))

search = driver.find_element(By.NAME, "query")
search.send_keys("web")
search.send_keys(Keys.ENTER)

while True:
    pass
