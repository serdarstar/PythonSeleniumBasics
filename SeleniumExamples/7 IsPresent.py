from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.gmail.com/")

# following code will return false and break the program since is_displayed is checking only Visibility
# print(driver.find_element("xpath", "identifierId").is_displayed())

# CHECKING PRESENCE
# METHOD 1

idElement = "identifierId"


def isElementPresent(idElement):
    try:
        driver.find_element("id", idElement)
        return True
    except NoSuchElementException:
        return False


# METHOD 2

def isElementPresent2(how, what):
    try:
        driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException:
        return False


# METHOD 3 Adding elements into a list
def isElementPresent3(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True


print(isElementPresent(idElement))
print(isElementPresent2(By.ID, "identifierId"))
print(isElementPresent2(By.ID, "identifierId11"))
print(isElementPresent3(By.ID, "identifierId"))
print(isElementPresent3(By.ID, "identifierId11"))
