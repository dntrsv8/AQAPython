import time

import pytest
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from helpers import forced_click

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


# Checking that correct page is opened (url)
def test_open_women_section(driver_chrome):
    driver_chrome.get("https://www.lamoda.by/")
    woman_xpath = '//*[@id="vue-root"]/div/header/div[2]/div[2]/nav/a[1]'
    element = driver_chrome.find_element(By.XPATH, woman_xpath)
    forced_click(driver_chrome, element)
    time.sleep(2)
    assert driver_chrome.current_url == 'https://www.lamoda.by/women-home/?sitelink=topmenuW'


# Checking that login pop-up is displayed after button click
def test_navigate_to_login(driver_chrome):
    driver_chrome.get("https://www.lamoda.by/")
    login_button_xpath = '//*[@id="vue-root"]/div/header/div[2]/div[1]/button'
    element = driver_chrome.find_element(By.XPATH, login_button_xpath)
    time.sleep(2)
    forced_click(driver_chrome, element)
    time.sleep(2)
    login_popup_check = driver_chrome.find_element(By.XPATH, '//*[@id="modals"]/div/div')


# Checking that search by item number opens item's page
def test_search_by_item_number(driver_chrome):
    driver_chrome.get("https://www.lamoda.by/")
    time.sleep(2)
    search_bar_xpath = '//*[@id="vue-root"]/div/header/div[3]/div/div/div/div/input'
    input_element = driver_chrome.find_element(By.XPATH, search_bar_xpath)
    search_button_xpath = '//*[@id="vue-root"]/div/header/div[3]/div/div/div/div/button/div'
    search_button = driver_chrome.find_element(By.XPATH, search_button_xpath)
    item_number = "rtlack740303"
    input_element.send_keys(item_number)
    forced_click(driver_chrome, search_button)
    time.sleep(2)
    assert "rtlack740303" in driver_chrome.current_url


# Checking that sign in button is disabled
def test_login_disabled_button(driver_chrome):
    driver_chrome.get("https://www.lamoda.by/")
    login_button_xpath = '//*[@id="vue-root"]/div/header/div[2]/div[1]/button'
    element = driver_chrome.find_element(By.XPATH, login_button_xpath)
    time.sleep(2)
    forced_click(driver_chrome, element)
    time.sleep(2)
    login_popup_check = driver_chrome.find_element(By.XPATH, '//*[@id="modals"]/div/div')
    current_position = pyautogui.position()
    invalid_email = 'dziyana.tarasava@gmail.com'
    pyautogui.typewrite(invalid_email)
    time.sleep(2)
    pyautogui.press('tab')
    invalid_pass = 'pass'
    pyautogui.typewrite(invalid_pass)
    pyautogui.press('tab')
    time.sleep(2)
    login_button= '//*[@id="modals"]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div[1]/form/div[5]/button'
    login_button_check = driver_chrome.find_element(By.XPATH,login_button)
    time.sleep(2)
    assert not login_button_check.is_enabled()

# Checking that validation message appears for wrong email format
def test_login_email_validation(driver_chrome):
    driver_chrome.get("https://www.lamoda.by/")
    login_button_xpath = '//*[@id="vue-root"]/div/header/div[2]/div[1]/button'
    element = driver_chrome.find_element(By.XPATH, login_button_xpath)
    time.sleep(2)
    forced_click(driver_chrome, element)
    time.sleep(2)
    login_popup_check = driver_chrome.find_element(By.XPATH, '//*[@id="modals"]/div/div')
    current_position = pyautogui.position()
    invalid_email='dziyana.tarasava'
    pyautogui.typewrite(invalid_email)
    time.sleep(2)
    pyautogui.press('tab')
    validation_path = '//*[@id="modals"]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div[1]/form/div[2]/div/div/div[2]/div[1]'
    validation_check = driver_chrome.find_element(By.XPATH, validation_path)
    time.sleep(2)
    assert validation_check.text == 'Пожалуйста, проверьте, правильно ли указан адрес'