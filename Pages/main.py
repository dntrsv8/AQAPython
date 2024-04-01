from selenium.webdriver.common.by import By
from Pages.basepage import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage, MainLocators):

    # Opening main page
    def open_main(self):
        self.driver_chrome.get("https://www.lamoda.by/")
        button_xpath = "//*[contains(text(),'Отклонить')]"
        self.wait_for_element(button_xpath)
        button = self.driver_chrome.find_element(By.XPATH, button_xpath)
        button.click()

    # Opening Women section through tab
    def open_women_section(self):
        women_element = self.driver_chrome.find_element(By.XPATH, self.woman_tab_xpath)
        women_element.click()

    def chat_open_button(self):
        chat_button = self.driver_chrome.find_element(By.XPATH, self.chat_popup_button_xpath)
        return chat_button

    def chat_open_header(self):
        chat_popup = self.driver_chrome.find_element(By.XPATH, self.chat_popup_header_xpath)
        return chat_popup

    def chat_popup(self):
        popup = self.driver_chrome.find_element(By.XPATH, self.chat_popup_container)
        return popup
    def login_button(self):
        login_button = self.driver_chrome.find_element(By.XPATH, self.login_button_xpath)
        return login_button

    def login_popup(self):
        login_popup = self.driver_chrome.find_element(By.XPATH, self.login_button_popup)
        return login_popup

    def login_email(self):
        login_email = self.driver_chrome.find_element(By.XPATH, self.email_popup)
        return login_email

    def login_popup_button(self):
        login_popup_button = self.driver_chrome.find_element(By.XPATH, self.login_button_popup)
        return login_popup_button

    def login_popup_email_validation(self):
        email_validation = self.driver_chrome.find_element(By.XPATH, self.validation_path_popup)
        return email_validation

    def search_bar(self):
        search_field = self.driver_chrome.find_element(By.XPATH, self.search_bar_xpath)
        return search_field

    def search_button(self):
        search_button = self.driver_chrome.find_element(By.XPATH, self.search_button_xpath)
        return search_button

    def footer_localization(self):
        localization_popup = self.driver_chrome.find_element(By.XPATH, self.localization_footer)
        return localization_popup

    def kz_site(self):
        local = self.driver_chrome.find_element(By.XPATH, self.kz_local)
        return local

    def ru_site(self):
        local = self.driver_chrome.find_element(By.XPATH, self.ru_local)
        return local

    def by_site(self):
        local = self.driver_chrome.find_element(By.XPATH, self.by_local)
        return local

    def subscription_footer_email(self):
        email = self.driver_chrome.find_element(By.XPATH, self.subscription_email)
        return email

    def subscription_submit_button(self):
        button = self.driver_chrome.find_element(By.XPATH, self.subscription_button)
        return button

    def subscription_validation_email(self):
        validation = self.driver_chrome.find_element(By.XPATH, self.email_validation)
        return validation

    def acceptance_link_click(self):
        link = self.driver_chrome.find_element(By.XPATH, self.acceptance_link)
        link.click()
    def footer_vk(self):
        vk_link = self.driver_chrome.find_element(By.XPATH, self.vk_xpath)
        return vk_link

    def footer_twitter(self):
        twitter_link = self.driver_chrome.find_element(By.XPATH, self.twitter_xpath)
        return twitter_link

    def footer_ok(self):
        ok_link = self.driver_chrome.find_element(By.XPATH, self.ok_xpath)
        return ok_link
