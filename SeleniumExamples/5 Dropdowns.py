import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)

# METHOD 1
# Select the dropdown element and use send_keys
driver.find_element("id","searchLanguage").send_keys("Dansk")

# Method 2
# Use Select class

dropdownItems=driver.find_element("id","searchLanguage")
select =Select(dropdownItems) # Create an object from Select class
select.select_by_value("af")

# Getting all values from a dropdown list
options= driver.find_elements("tag name","option")
for anyOption in options:
    print("Text value is: "+anyOption.text)

print(len(options))  # Print total of dropdown items



#input()