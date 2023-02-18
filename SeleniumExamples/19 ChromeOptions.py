import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chromeOptions=webdriver.ChromeOptions()
# Disables push notifications
prefs = {"profile.default_content_setting_values.notifications" : 2}
chromeOptions.add_experimental_option("prefs", prefs)
# Prevents Chrome is being controlled by automated test software message
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
# Open in headless mode
#chromeOptions.headless = True


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chromeOptions)
driver.get("https://www.lowbrowcustoms.com/")

print(driver.title)

isHeadless=chromeOptions.headless
if (isHeadless):
    print("Running headless")


time.sleep(5)