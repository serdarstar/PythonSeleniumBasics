import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
driver.implicitly_wait(1)

driver.find_element("xpath","//input[@name='alert']").click()

alert = driver.switch_to.alert

print(alert.text)
time.sleep(3)
alert.accept()