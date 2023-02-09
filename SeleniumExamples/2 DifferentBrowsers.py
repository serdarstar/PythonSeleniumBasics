from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver =webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver =webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
driver.get("https://www.amazon.co.uk")

title= driver.title
print(title)
driver.close()

# instead of doing all these things, we can put .exe files for browsers under Scripts folder, and call them directly