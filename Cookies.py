from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time


def extract_num_from_string(string: str):
    return "".join(re.findall("\d", string))


chrome_local_path = "C:\Development"
driver = webdriver.Chrome(executable_path=chrome_local_path)


driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
cookie.click()
money = driver.find_element(By.CSS_SELECTOR, "#money")
money = float(money.text)


def punchCookie(money):
    print(f"momey = {money}")
    for i in range(int(money)):
        cookie.click()
    make_shopping(money=money)


def make_shopping(money=money):
    buyGrandma_text = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
    buyGrandma_cost = float(extract_num_from_string(buyGrandma_text.text))
    print(buyGrandma_cost)

    buyFactory = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
    buyFactory_cost = float(extract_num_from_string(buyFactory.text))
    print(buyFactory_cost)

    buyMine = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
    buyMine_cost = float(extract_num_from_string(buyMine.text))
    print(buyMine_cost)

    buyShipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
    buyShipment_cost = float(extract_num_from_string(buyShipment.text))
    print(buyShipment_cost)

    buyAlchemy = driver.find_element(By.CSS_SELECTOR, "[id='buyAlchemy lab'] b")
    buyAlchemy_cost = float(extract_num_from_string(buyAlchemy.text))
    print(buyAlchemy_cost)

    buyPortal = driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
    buyPortal_cost = float(extract_num_from_string(buyPortal.text))
    print(buyPortal_cost)

    buyTime_machine = driver.find_element(By.CSS_SELECTOR, "[id='buyTime machine'] b")
    buyTime_machine_cost = float(extract_num_from_string(buyTime_machine.text))
    print(buyTime_machine_cost)
    print(type(buyTime_machine_cost))
    money = driver.find_element(By.CSS_SELECTOR, "#money")
    money = int(money.text)
    if money >= buyTime_machine_cost:
        buyTime_machine.click()
    elif money >= buyPortal_cost:
        buyPortal.click()
    elif money >= buyAlchemy_cost:
        buyAlchemy.click()
    elif money >= buyShipment_cost:
        buyShipment.click()
    elif money >= buyMine_cost:
        buyMine.click()
    elif money >= buyFactory_cost:
        buyFactory.click()
    elif money >= buyGrandma_cost:
        buyGrandma_text.click()

    punchCookie(money=money)


punchCookie(money=money)
