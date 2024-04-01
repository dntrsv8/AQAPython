import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture
def lamoda_track(driver_chrome):
    driver_chrome.get("https://www.lamoda.by/track/")
    WebDriverWait(driver_chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='_header_1q75s_7']")))
    return driver_chrome

@pytest.fixture
def lamoda_main(driver_chrome):
    driver_chrome.get("https://www.lamoda.by/")
    WebDriverWait(driver_chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='_title_16eml_8']")))
    return driver_chrome
