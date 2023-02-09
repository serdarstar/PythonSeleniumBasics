import time

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver =webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
driver.get("https://www.amazon.co.uk")
driver.implicitly_wait(20)
driver.find_element("xpath","//*[@id='sp-cc-accept']").click()
driver.find_element("xpath","//*[@id='twotabsearchtextbox']").click()
driver.find_element("xpath","//*[@id='glow-ingress-line2']").click()

input()