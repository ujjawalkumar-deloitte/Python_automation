from selenium.webdriver.common.by import By
from testData.locators import loginXpath


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
    
    def click_login(self):
        self.driver.find_element(By.XPATH, loginXpath["click_login"]).click()
    
    def setUsername(self,username):
        self.driver.find_element(By.XPATH, loginXpath["enter_username"]).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, loginXpath["enter_password"]).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element(By.XPATH, loginXpath["click_loginbuttons"]).click()