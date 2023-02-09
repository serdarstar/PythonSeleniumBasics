from selenium import webdriver
# I am not giving the path for chromedriver.exe since I put it under scripts folder
driver =webdriver.Chrome()
driver.get("https://www.amazon.co.uk")

title= driver.title
print(title)

assert "Amazon" in title

