from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("http://www.way2automation.com/")
driver.maximize_window()
driver.implicitly_wait(1)


menu = driver.find_element("id","menu-item-27617")
subMenu = driver.find_element("id","menu-item-27619")

action = ActionChains(driver)
action.move_to_element(menu).move_to_element(subMenu).click().perform()

