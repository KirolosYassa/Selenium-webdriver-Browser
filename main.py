from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_local_path = "C:\Development"
driver = webdriver.Chrome(executable_path=chrome_local_path)


driver.get("https://www.python.org/")

times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in times:
    print(time.text)

titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for title in titles:
    print(title.text)

upComing_dict = {}
for index in range(0, 5):
    upComing_dict.update(
        {index: {"time": times[index].text, "name": titles[index].text}}
    )


print(upComing_dict)


# driver.close()
