from selenium.webdriver.common.by import By
from pageObjects.Register_Page import RegisterPage
from utilities.readProperties import ReadConfig
from testData.locators import Register_Page_locators



class Test_Login:

    baseURL = ReadConfig.getApplicationURL()
    firstName = ReadConfig.getfirstName()
    lastName = ReadConfig.getlastName()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()
    telephone = ReadConfig.gettelephone()
    confirmPassword = ReadConfig.getConfirmPassword()


    def test_RegisterPage(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = RegisterPage(self.driver)
        self.lp.click_MyAccount()
        self.lp.click_Register_tab()
        self.lp.enter_Firstname(self.firstName)
        self.lp.enter_Lastname(self.lastName)
        self.lp.enter_password(self.password)
        self.lp.enter_telephone(self.telephone)
        self.lp.enter_Email(self.email)
        self.lp.enterConfirmPassoword(self.confirmPassword)
        self.lp.click_checkbox()
        self.lp.click_continue()
        alert_messsage = self.driver.find_element(By.XPATH, Register_Page_locators["alert_mssg"]).text
        print(alert_messsage)
        if alert_messsage  == "Warning: E-Mail Address is already registered!":
            self.lp.click_login()
            assert True
        else:
            self.lp.text_assert()
            self.lp.click_continueButton()
            assert False
        
        act_title = self.driver.title
        if act_title == "Account Login":
            assert True
        else:
            assert False

   
    