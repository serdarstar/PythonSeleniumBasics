from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# I am not giving the path for chromedriver.exe since I put it under scripts folder
driver =webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.amazon.co.uk")

title= driver.title
print(title)

assert "Amazon" in title

