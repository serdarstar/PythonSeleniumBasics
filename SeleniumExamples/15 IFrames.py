import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def capture_screenshot(d, path):
    file_name = path + "screenshot_" + time.asctime().replace(":", "_") + ".png"
    d.save_screenshot(file_name)


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element("id", "accept-choices").click()

driver.save_screenshot("./screenshot/error.jpg")

driver.switch_to.frame("iframeResult")
driver.find_element("xpath", "/html/body/button").click()

driver.switch_to.window(driver.window_handles[0])

frames = driver.find_elements("tag name", "iframe")

for frame in frames:
    print(frame.get_attribute("id"))

print(len(frames))

capture_screenshot(driver, "./screenshot/")
