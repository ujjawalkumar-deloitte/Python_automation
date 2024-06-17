from selenium.webdriver.common.by import By
from testData.locators import Login_Page
import time



class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        # self.log = LoggerUtils(log_file_path)

    
    def enter_email(self,email):
        self.driver.find_element(By.ID, Login_Page["enter_email"]).send_keys(email)
    
    def enter_password(self,password):
        self.driver.find_element(By.ID, Login_Page["enter_password"]).send_keys(password)
        time.sleep(5)

    def click_login(self):
        self.driver.find_element(By.XPATH, Login_Page["login_button"]).click()
        time.sleep(5)