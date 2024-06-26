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


# Nav_bar_list = [
#     {"header1" : "//a[normalize-space()='Desktops']"},
#     {"header2" : "//a[normalize-space()='Laptops & Notebooks']"},
#     {"header3" : "//a[normalize-space()='Components']"},
#     {"header4" : "//a[normalize-space()='Software']"},
#     {"header5" : "//a[normalize-space()='Tablets']"},
#     {"header6" : "//a[normalize-space()='Phones & PDAs']"},
#     {"header7" : "//a[normalize-space()='Cameras']"},
#     {"header8" : "//a[normalize-space()='MP3 Players']"}
#     ]

nav_headers1 = {

    "header1" : "//a[normalize-space()='MP3 Players']",
    # "header2" : "//a[normalize-space()='Laptops & Notebooks']",
    # "header3" : "//a[normalize-space()='Components']",
    # "header4" : "//a[normalize-space()='Software']",
    # "header5" : "//a[normalize-space()='Tablets']",
    # "header6" : "//a[normalize-space()='Phones & PDA']",
    # "header7" : "//a[normalize-space()='Cameras']",
    # "header8" : "//a[normalize-space()='MP3 Players']"
    "click_show_all_desktops" : "//a[normalize-space()='Show AllMP3 Players']"

}

Add_To_Cart_list = [
    {"click_add_to_cart" : "//*[@id='content']/div[4]/div[1]/div/div[2]/div[2]/button[1]"},
    {"click_add_to_cart" : "//*[@id='content']/div[4]/div[2]/div/div[2]/div[2]/button[1]"},
    {"click_add_to_cart" : "//*[@id='content']/div[4]/div[3]/div/div[2]/div[2]/button[1]"}
]

Logout_Page = {
    "click_MyAccount" : "//a[@title='My Account']",
    "click_logout" : "//a[normalize-space()='Logout']"
}