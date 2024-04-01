from Pages.basepage import BasePage
from locators.tracking_locators import TrackingLocators
from selenium.webdriver.common.by import By


class Tracking(BasePage, TrackingLocators):

    def open_tracking(self):
        self.driver_chrome.get("https://www.lamoda.by/track/")
        button_xpath = "//*[contains(text(),'Отклонить')]"
        self.wait_for_element(button_xpath)
        button = self.driver_chrome.find_element(By.XPATH, button_xpath)
        button.click()


    def order_number_field(self):
        order_number = self.driver_chrome.find_element(By.XPATH, self.order_number_xpath)
        return order_number

    def validation_order_number(self):
        validation = self.driver_chrome.find_element(By.XPATH, self.order_validation_xpath)
        return validation

    def phone_number_field(self):
        phone_number = self.driver_chrome.find_element(By.XPATH, self.phone_number_xpath)
        return phone_number

    def validation_phone_number(self):
        validation = self.driver_chrome.find_element(By.XPATH, self.phone_validation_xpath)
        return validation

    def button_tracking_order(self):
        button = self.driver_chrome.find_element(By.XPATH, self.check_button_xpath)
        return button

    def my_orders_click(self):
        link = self.driver_chrome.find_element(By.XPATH, self.my_orders_xpath)
        link.click()