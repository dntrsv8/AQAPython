import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import lamoda_track
from conftest import lamoda_main


@pytest.mark.orderstatus
@pytest.mark.parametrize("order_number", ["BY123456-2", "12ABCJAJA"])
def test_track_order_number(lamoda_track, order_number):
    order_number_xpath = "//*[@name='input-order-number']"
    input_element = WebDriverWait(lamoda_track, 10).until(
        EC.presence_of_element_located((By.XPATH, order_number_xpath)))
    input_element.send_keys(order_number)
    validation_xpath = "//*[@id='vue-root']//form//div[1]//div[contains(@class, 'input__validation-message')]"
    validation_check = WebDriverWait(lamoda_track, 10).until(
        EC.presence_of_element_located((By.XPATH, validation_xpath)))
    assert validation_check.text == "Пожалуйста, проверьте, правильно ли указан номер заказа."


@pytest.mark.orderstatus
@pytest.mark.parametrize("phone_number", ["12312312", "ABCJAJA"])
def test_track_phone_number(lamoda_track, phone_number):
    phone_number_xpath = "//*[@name='input-phone']"
    input_element = WebDriverWait(lamoda_track, 10).until(
        EC.presence_of_element_located((By.XPATH, phone_number_xpath)))
    input_element.send_keys(phone_number)
    validation_xpath = "//*[@id='vue-root']//form//div[2]//div[contains(@class, 'input__validation-message')]"
    validation_check = WebDriverWait(lamoda_track, 10).until(
        EC.presence_of_element_located((By.XPATH, validation_xpath)))
    assert validation_check.text == "Номер телефона должен состоять из 12 цифр."


@pytest.mark.socialmedia
def test_vk_link(lamoda_main):
    current_tab = lamoda_main.current_window_handle
    footer = lamoda_main.find_element(By.TAG_NAME, "body")
    footer.send_keys(Keys.END)
    vk_xpath = "//*[@class='icon icon_social icon_social-vk']"
    element = WebDriverWait(lamoda_main, 10).until(EC.presence_of_element_located((By.XPATH, vk_xpath)))
    element.click()
    WebDriverWait(lamoda_main, 10).until(EC.number_of_windows_to_be(2))
    all_handles = lamoda_main.window_handles
    new_tab_handle = [handle for handle in all_handles if handle != current_tab][0]
    lamoda_main.switch_to.window(new_tab_handle)
    assert lamoda_main.current_url == 'https://vk.com/lamodaby?from=footer'


@pytest.mark.socialmedia
def test_twitter_link(lamoda_main):
    current_tab = lamoda_main.current_window_handle
    footer = lamoda_main.find_element(By.TAG_NAME, "body")
    footer.send_keys(Keys.END)
    twitter_xpath = "//*[@class='icon icon_social icon_social-twitter']"
    element = WebDriverWait(lamoda_main, 10).until(EC.presence_of_element_located((By.XPATH, twitter_xpath)))
    element.click()
    WebDriverWait(lamoda_main, 10).until(EC.number_of_windows_to_be(2))
    all_handles = lamoda_main.window_handles
    new_tab_handle = [handle for handle in all_handles if handle != current_tab][0]
    lamoda_main.switch_to.window(new_tab_handle)
    assert lamoda_main.current_url == 'https://twitter.com/Lamoda_by?from=footer'


@pytest.mark.socialmedia
def test_ok_link(lamoda_main):
    current_tab = lamoda_main.current_window_handle
    footer = lamoda_main.find_element(By.TAG_NAME, "body")
    footer.send_keys(Keys.END)
    ok_xpath = "//*[@class='icon icon_social icon_social-ok']"
    element = WebDriverWait(lamoda_main, 10).until(EC.presence_of_element_located((By.XPATH, ok_xpath)))
    element.click()
    WebDriverWait(lamoda_main, 10).until(EC.number_of_windows_to_be(2))
    all_handles = lamoda_main.window_handles
    new_tab_handle = [handle for handle in all_handles if handle != current_tab][0]
    lamoda_main.switch_to.window(new_tab_handle)
    assert lamoda_main.current_url == 'https://ok.ru/group/52479738445918?from=footer'
