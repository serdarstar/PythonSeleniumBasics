import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.espncricinfo.com/series/a20-league-2020-21-1255254/points-table-standings")
driver.maximize_window()
driver.implicitly_wait(1)

rows=driver.find_elements("xpath","//tbody//tr[@class='ds-text-tight-s']")
totalRows=len(rows)

columns=driver.find_elements("xpath", "//tbody//tr[1]//td")
totalColumns=len(columns)
print(totalRows,totalColumns)

print("Total rows are : ", totalRows, " and total cols are : ", totalColumns)

for row in rows:
    print(row.text)

print("-----Second Way--------")

start_xpath = "//tbody/tr[@class='ds-text-tight-s']["
mid_xpath = "]/td["
end_xpath = "]"


for row in range(1, totalRows + 1):
    for col in range(1, totalColumns + 1):
        print(driver.find_element("xpath",start_xpath + str(row) + mid_xpath + str(col) + end_xpath).text, end=" ")
    print()


time.sleep(3)