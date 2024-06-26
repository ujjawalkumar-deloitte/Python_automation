from selenium.webdriver.common.by import By
from testData.locators import Add_To_Cart_list, nav_headers1
from selenium.webdriver import ActionChains
import time


class Nav_Bar:
    def __init__(self, driver):
        self.driver = driver

    # def nav_headers(self):

    #     for name in Nav_bar_list:
    #         header = self.driver.find_element(By.XPATH, name["header1"])
    #         print(header)
    #         if header. is_displayed() and header. is_enabled():
    #             print(f"Header {name} is visible and clickable. Clicking...")
    #             header.click()
    #         else:
    #             print("Header not visible")

    def nav_headers1(self):
        time.sleep(5)
        element_to_hover_over = self.driver.find_element(By.XPATH, nav_headers1["header1"])
        element_to_hover_over.click()
        element_to_hover_over.text
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.driver.find_element(By.XPATH, nav_headers1["click_show_all_desktops"]).click()

        
        
    def add_to_cart(self):
        time.sleep(5)
        for click_addtocart in Add_To_Cart_list:
            click_add_to_cart = self.driver.find_element(By.XPATH, click_addtocart["click_add_to_cart"])
            click_add_to_cart.click()
            time.sleep(5)
