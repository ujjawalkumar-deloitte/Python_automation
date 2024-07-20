from testData.locators import log_file_path, checkout
from utilities.logger import LoggerUtils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



class Checkout_Page:

    def __init__(self, driver):
        self.driver = driver
        self.log = LoggerUtils(log_file_path)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    
    def click_checkout(self):
        # try:
        #     self.log.log_info("clicking checkout button...")
        self.driver.find_element(By.XPATH, checkout["click_checkout"]).click()
        time.sleep(10)
        # except Exception as e:
        #     self.log.log_error(f"An error occurred: {str(e)}")
