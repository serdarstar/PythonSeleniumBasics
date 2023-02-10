from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.w3schools.com/")
driver.maximize_window()
driver.implicitly_wait(1)

print(driver.find_element("xpath","//h1[@class='learntocodeh1']").value_of_css_property("font-size"))

print(driver.find_element("xpath","//h1[@class='learntocodeh1']").value_of_css_property("color"))

print(driver.find_element("xpath","//h1[@class='learntocodeh1']").value_of_css_property("font-family"))