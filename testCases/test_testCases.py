from selenium.webdriver.common.by import By
from pageObjects.Login_Page import LoginPage
from pageObjects.Logout_Page import Logout
from pageObjects.Register_Page import RegisterPage
from pageObjects.nav_bar import Nav_Bar
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
        self.rp = RegisterPage(self.driver)
        self.rp.click_MyAccount()
        self.rp.click_Register_tab()
        self.rp.enter_Firstname(self.firstName)
        self.rp.enter_Lastname(self.lastName)
        self.rp.enter_password(self.password)
        self.rp.enter_telephone(self.telephone)
        self.rp.enter_Email(self.email)
        self.rp.enterConfirmPassoword(self.confirmPassword)
        self.rp.click_checkbox()
        self.rp.click_continue()
        alert_messsage = self.driver.find_element(By.XPATH, Register_Page_locators["alert_mssg"]).text
        print(alert_messsage)
        if alert_messsage  == "Warning: E-Mail Address is already registered!":
            self.rp.click_login()
            assert True
        else:
            self.rp.text_assert()
            self.rp.click_continueButton()
            assert False
        
        act_title = self.driver.title
        if act_title == "Account Login":
            assert True
        else:
            assert False



    def test_loginPage(self, setup):
        self.driver = setup
        self.rp = RegisterPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.lp.enter_email(self.email)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        if act_title == "My Account":
            assert True
        else:
            assert False

    def test_nav_bar(self,setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.nav = Nav_Bar(self.driver)
        self.nav.nav_headers1()
        self.nav.add_to_cart()



    def test_logout(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lo = Logout(self.driver)
        self.lo.click_logout()
        act_title = self.driver.title
        if act_title == "Account Logout":
            assert True
        else:
            assert False

   
    