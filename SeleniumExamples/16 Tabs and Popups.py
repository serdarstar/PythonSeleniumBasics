import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(1)


driver.find_element("xpath","//button[@id='openwindow']").click()

windows = driver.window_handles

for window in windows:
    print(window)

driver.switch_to.window(driver.window_handles[1])

driver.find_element("xpath","//a[normalize-space()='Home']").click()

driver.close()

driver.switch_to.window(driver.window_handles[0])

driver.close()