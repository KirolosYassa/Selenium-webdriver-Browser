from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_local_path = "C:\Development"
driver = webdriver.Chrome(executable_path=chrome_local_path)


driver.get("https://www.python.org/")

title = driver.find_elements(By.CSS_SELECTOR, ".widget-title")
print(title.text)
# titles = driver.find_elements(By.CSS_SELECTOR, ".widget-title")
# for title in titles:
#     print(title.text)
# driver.close()
