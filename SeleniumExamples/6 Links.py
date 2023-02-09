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


# Getting all links
options= driver.find_elements("tag name","a")
for anyOption in options:
    print("Text value is: "+anyOption.text)

print(len(options))  # Print total of dropdown items
print("----------------------------------------------------------------------")

# Getting all links from a section of a page

section=driver.find_element("xpath","//*[@id='www-wikipedia-org']/div[7]/div[3]")
sectionLinks=section.find_elements("tag name","a")
for anyLink in sectionLinks:
    print("Link is: "+anyLink.text)

print("----------------------------------------------------------------------")

# printing an item at an index, selecting from a list
print(driver.find_elements("xpath", "//option").__getitem__(0).text)
print(driver.find_elements("tag name","a").__getitem__(0).text)







#input()