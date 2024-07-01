from selenium.webdriver.common.by import By
from testData.locators import shopping_cart


class Cart_Page:

    def __init__(self, driver):
        self.driver = driver

    def click_shopping_cart(self):
        self.driver.find_element(
            By.XPATH, shopping_cart["click_shopping_cart"]).click()
        total_cart_items = self.driver.find_element(
            By.XPATH, shopping_cart["total_cart_items"]).text
        print("total items in cart:", total_cart_items)

    
    def click_checkout(self):
        # alert_message = self.driver.find_element(
        #     By.XPATH, shopping_cart["alert_message"]).text
        # print(alert_message)


        # if alert_message == alert_message:
        #     print(alert_message)
        #     assert True
        # else:
        #     print("Alert message is not matching")
        #     assert False
        
        added_item_table = self.driver.find_element(By.XPATH, shopping_cart["total_items_added_in_cart"]).text
        alert_added_item = self.driver.find_element(By.XPATH, shopping_cart["added_item_with_star"]).text
        print("item added in cart:", added_item_table)
        print("items in cart with star:", alert_added_item)

        if alert_added_item in added_item_table:
            click_remove = self.driver.find_element(By.XPATH, shopping_cart["click_remove_button"])
            click_remove.click()
        else:
            self.driver.find_element(By.XPATH, shopping_cart["click_checkout"]).click()
