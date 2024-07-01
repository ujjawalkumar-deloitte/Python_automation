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
        print(total_cart_items)

    
    def click_checkout(self):
        self.driver.find_element(
            By.XPATH, shopping_cart["click_checkout"]).click()
        alert_message = self.driver.find_element(
            By.XPATH, shopping_cart["alert_message"]).text
        print(alert_message)


        if alert_message == alert_message:
            print(alert_message)
            assert True
        else:
            print("Alert message is not matching")
            assert False
