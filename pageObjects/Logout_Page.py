from selenium.webdriver.common.by import By
import time
from testData.locators import Logout_Page

class Logout:
    def __init__(self, driver):
        self.driver = driver


    def click_logout(self):
        self.driver.find_element(By.XPATH, Logout_Page["click_logout"]).click()
        time.sleep(5)