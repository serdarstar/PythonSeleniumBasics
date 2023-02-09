import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element("id","accept-choices").click()


driver.switch_to.frame("iframeResult")
# driver.find_element_by_xpath("/html/body/button").click()
driver.execute_script("myFunction()")

elem = driver.find_element("id","mySubmit")
elem.screenshot("./screenshot/elem.png")
driver.execute_script("arguments[0].style.border='3px solid red'", elem)

driver.switch_to.default_content()

# driver.switch_to.window(driver.window_handles[0])

frames = driver.find_elements("tag name","iframe")

for frame in frames:
    print(frame.get_attribute("id"))

print(len(frames))



