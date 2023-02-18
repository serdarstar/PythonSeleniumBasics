# Support for Chrome DevTools
# https://www.selenium.dev/documentation/en/support_packages/chrome_devtools/
# WebDriver implementation for CDP in Selenium 4
# https://github.com/SeleniumHQ/selenium/blob/4c5b92bac07b17e223917c31caddf7035c120ea7/py/selenium/webdriver/chromium/webdriver.py#L133
# Emulating GeoLocation with Python in Selenium 4
# CDP is only available for local WebDriver (on Chrome/Chromium)
# https://github.com/SeleniumHQ/selenium/blob/474d11671452ffc6830e3b9603d6e438c9cce8fd/py/selenium/webdriver/chromium/webdriver.py
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
import urllib3
import warnings
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_cdp_command():
        web_driver = webdriver.Chrome()
        web_driver.maximize_window()
        time.sleep(2)
        map_coord = {
                "latitude": 42.1408845,
                "longitude": -72.5033907,
                "accuracy": 100
        }
        web_driver.execute_cdp_cmd('Emulation.setGeolocationOverride', {
                "latitude": map_coord['latitude'],
                "longitude": map_coord['longitude'],
                "accuracy": map_coord['accuracy']
        })
        web_driver.get('https://locations.dennys.com/search.html/')
        time.sleep(2)
        location_icon = web_driver.find_element(By.CSS_SELECTOR, "button[class='c-location-finder__find-me'] span")

        time.sleep(2)
        location_icon.click()
        time.sleep(5)
        # Release resources held by the Selenium WebDriver
        web_driver.quit()
        print("Geolocation testing with Selenium is complete")

def test_cdp_command2():
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    map_coord = {
        "latitude": 42.1408845,
        "longitude": -72.5033907,
        "accuracy": 100
    }
    web_driver.execute_cdp_cmd("Emulation.setGeolocationOverride", map_coord)
    #time.sleep(2)
    web_driver.get("https://maps.google.com")
    search_elem = WebDriverWait(web_driver, 20).until(
            EC.presence_of_element_located((By.ID, "sVuEFc")))
    search_elem.click()
    time.sleep(10)
    # Release resources held by the Selenium WebDriver
    web_driver.quit()
    print("Geolocation testing with Selenium is complete")