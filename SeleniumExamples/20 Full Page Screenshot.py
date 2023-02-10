import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# To get full page screenshot, chrome must run in headless mode
chrome_options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)

driver.get("http://www.way2automation.com/")
driver.maximize_window()
driver.implicitly_wait(1)


S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
driver.set_window_size(S('Width'),S('Height'))

driver.find_element("tag name",'body').screenshot('./screenshot/fullpage.png')


