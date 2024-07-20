from selenium.webdriver.common.by import By
from testData.locators import shopping_cart
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Cart_Page:

    def __init__(self, driver):
        self.driver = driver
        

    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_shopping_cart(self):
        self.driver.find_element(
            By.XPATH, shopping_cart["click_shopping_cart"]).click()
        total_cart_items = self.driver.find_element(
            By.XPATH, shopping_cart["total_cart_items"]).text
        print("total items in cart:", total_cart_items)

    
    def add_items_in_cart(self):
               
        added_item_table = self.driver.find_element(By.XPATH, shopping_cart["total_items_added_in_cart"]).text
        alert_added_item = self.driver.find_element(By.XPATH, shopping_cart["added_item_with_star"]).text
        print("item added in cart:", added_item_table)
        print("items in cart with star:", alert_added_item)

        if alert_added_item in added_item_table:
            click_remove = self.driver.find_element(By.XPATH, shopping_cart["click_remove_button"])
            click_remove.click()
            
        else:
            act_title = self.driver.title
            if act_title == "Shopping Cart":
                assert True
            else:
                assert False

    
            
