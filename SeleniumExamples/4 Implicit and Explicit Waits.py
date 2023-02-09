import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://gmail.com")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)

# username = driver.find_element_by_id("identifierId")
# username.send_keys("trainer@way2automation.com")


driver.find_element("id","identifierId").send_keys("trainer@way2automation.com")
driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

element = wait.until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id=\"password\"]/div[1]/div/div[1]/input")))

element.send_keys("ksfbksndfsjkdfj")

driver.find_element("id","passwordNext").click()

