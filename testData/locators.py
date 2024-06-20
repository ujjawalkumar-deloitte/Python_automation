log_file_path = 'Logs/automation.log'




Register_Page_locators = {
    "click_MyAccount" : "//a[@title='My Account']",
    "click_register" : "//a[normalize-space()='Register']",
    "enter_firstname" : "input-firstname",
    "enter_lastname" : "input-lastname",
    "enter_email" : "input-email",
    "enter_telephone" : "input-telephone",
    "enter_password" : "//input[@id='input-password']",
    "enterConfirmPassword" : "//input[@id='input-confirm']",
    "click_checkbox" : "//input[@name='agree']",
    "click_continue_button" : "//input[@value='Continue']",
    "click_continue" : "//a[normalize-space()='Continue']",
    "assert_mssg" : "//h1[normalize-space()='Your Account Has Been Created!']",
    "alert_mssg" : "//div[@class='alert alert-danger alert-dismissible']",
    "click_login" : "//a[@class='list-group-item'][normalize-space()='Login']"
}

Login_Page = {

    "enter_email" : "input-email",
    "enter_password" : "input-password",
    "login_button" : "//input[@value='Login']"
}

Logout = {
    "logout_button" : "//a[@class='list-group-item'][normalize-space()='Logout']"
}