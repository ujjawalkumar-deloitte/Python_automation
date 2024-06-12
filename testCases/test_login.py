import pytest
import os
from pageObjects.loginpage import LoginPage
from utilities.readProperties import ReadConfig


class Test_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_login()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_loginbutton()

    