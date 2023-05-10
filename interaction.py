from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_local_path = "C:\Development"
driver = webdriver.Chrome(executable_path=chrome_local_path)


driver.get("https://en.wikipedia.org/wiki/Main_Page")

link = driver.find_element(By.LINK_TEXT, "World Health Organization")
link.click()
