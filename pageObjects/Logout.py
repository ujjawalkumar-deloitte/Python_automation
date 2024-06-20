from selenium.webdriver.common.by import By
from testData.locators import Logout
import time


class LogoutPage:

    def __init__(self, driver):
        self.driver = driver
    

    def click_logout(self):
        self.driver.find_element(By.XPATH, Logout["logout_button"]).click()
        time.sleep(5)