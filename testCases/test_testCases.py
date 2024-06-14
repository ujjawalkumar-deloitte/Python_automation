from selenium import webdriver
from pageObjects.Register_Page import RegisterPage
from utilities.readProperties import ReadConfig



class Test_Login:

    baseURL = ReadConfig.getApplicationURL()
    firstName = ReadConfig.getfirstName()
    lastName = ReadConfig.getlastName()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()
    telephone = ReadConfig.gettelephone()
    confirmPassword = ReadConfig.getConfirmPassword()


    def test_login(self,setup):
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
       
        act_title = self.driver.title
        if act_title == "Register Account":
            assert True
        else:
            assert False

   
    