from selenium.webdriver.common.by import By
from testData.locators import Register_Page_locators
import time


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
    
    def click_MyAccount(self):
        self.driver.find_element(By.XPATH, Register_Page_locators["click_MyAccount"]).click()
    
    def click_Register_tab(self):
        self.driver.find_element(By.XPATH, Register_Page_locators["click_register"]).click()
    
    def enter_Firstname(self,firstName):
        self.driver.find_element(By.ID, Register_Page_locators["enter_firstname"]).send_keys(firstName)

    def enter_Lastname(self,lastName):
        self.driver.find_element(By.ID, Register_Page_locators["enter_lastname"]).send_keys(lastName)
    
    def enter_telephone(self, telephone):
        self.driver.find_element(By.ID, Register_Page_locators["enter_telephone"]).send_keys(telephone)
    
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, Register_Page_locators["enter_password"]).send_keys(password)

    def enter_Email(self, email):
        self.driver.find_element(By.ID, Register_Page_locators["enter_email"]).send_keys(email)
        time.sleep(10)
    
    def enterConfirmPassoword(self,confirmPassword):
        self.driver.find_element(By.XPATH, Register_Page_locators["enterConfirmPassword"]).send_keys(confirmPassword) 
    
    def click_checkbox(self):
        self.driver.find_element(By.XPATH, Register_Page_locators["click_checkbox"]).click()
        time.sleep(5)

    def click_continue(self):
        self.driver.find_element(By.XPATH, Register_Page_locators["click_continue_button"]).click()

    def text_assert(self):
        element = self.driver.find_element(By.XPATH, Register_Page_locators["assert_mssg"]).text
        if element == "Your Account Has Been Created!":
            print("Account created successfully!")
            
            assert True
        else:
            print("Account not created successfully!")
            assert False
    
    def click_continueButton(self):
        self.driver.find_element(By.XPATH, Register_Page_locators["click_continue"]).click()
    
    def click_login(self):
        self.driver.find_element(By.XPATH, Register_Page_locators["click_login"]).click()
        time.sleep(5)
    



    
