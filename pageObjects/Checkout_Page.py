from testData.locators import log_file_path, checkout
from utilities.logger import LoggerUtils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



class Checkout_Page:

    def __init__(self, driver):
        self.driver = driver
        self.log = LoggerUtils(log_file_path)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    
    def click_checkout(self,firstName,lastName,Address,City,PostCode):
        try:
            self.log.log_info("clicking checkout button...")
            time.sleep(5)
            self.driver.find_element(By.XPATH, checkout["click_cart_total"]).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, checkout["click_checkout"]).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, checkout["continue_button1"]).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, checkout["continue_button2"]).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, checkout["continue_button3"]).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, checkout["click_tickbox"]).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, checkout["continue_button4"]).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, checkout["confirm_order"]).click()
            time.sleep(10)
            # self.driver.find_element(By.XPATH, checkout["firstName"]).send_keys(firstName)
            # self.driver.find_element(By.XPATH, checkout["lastName"]).send_keys(lastName)
            # self.driver.find_element(By.XPATH, checkout["Address1"]).send_keys(Address)
            # self.driver.find_element(By.XPATH, checkout["City"]).send_keys(City)
            # self.driver.find_element(By.XPATH, checkout["Postcode"]).send_keys(PostCode)
            # self.driver.find_element(By.XPATH, checkout["country_dropdown"]).click()
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, checkout["select_country"]).click()
            # self.driver.find_element(By.XPATH, checkout["state_dropdown"]).click()
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, checkout["select_state"]).click()
            # time.sleep(30)
            # self.driver.find_element(By.XPATH, checkout["continue_button"]).click()
            # time.sleep(5)

            exp_text = self.driver.find_element(By.XPATH, checkout["order_confirmed_message"]).text
            if exp_text == "Your order has been placed!":
                assert True
            else:
                print(exp_text)
                assert False
        except Exception as e:
            self.log.log_error(f"An error occurred: {str(e)}")

    # def confirm_order(self):
    #     self.driver.find_element(By.XPATH, checkout["click_cart_total"]).click()
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH, checkout["click_checkout"]).click()
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH, checkout["continue_button1"]).click()
    #     self.driver.find_element(By.XPATH, checkout["continue_button2"]).click()
    #     self.driver.find_element(By.XPATH, checkout["continue_button3"]).click()
    #     self.driver.find_element(By.XPATH, checkout["click_tickbox"]).click()
    #     self.driver.find_element(By.XPATH, checkout["confirm_order"]).click()
    #     time.sleep(10)

    #     exp_text = self.driver.find_element(By.XPATH, checkout["order_confirmed_message"]).text
    #     if exp_text == "Your order has been placed!":
    #         assert True
    #     else:
    #         print(exp_text)
    #         assert False

