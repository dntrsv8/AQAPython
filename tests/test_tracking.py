import pytest
from Pages.tracking_order import Tracking


def test_tracking_order_title(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    assert "Проверить заказ по номеру" in tracking_page.title()


def test_my_order_link(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.my_orders_xpath)
    tracking_page.my_orders_click()
    tracking_page.wait_for_url("https://www.lamoda.by/sales/order/history/?from=track")
    assert driver_chrome.current_url == "https://www.lamoda.by/sales/order/history/?from=track"


def test_tracking_button_enabled(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.order_number_xpath)
    input_order = tracking_page.order_number_field()
    input_order.send_keys("BY123456-123456")
    input_phone = tracking_page.phone_number_field()
    input_phone.send_keys("375331234567")
    check_button = tracking_page.button_tracking_order()
    assert check_button.is_enabled()


def test_tracking_button_order_disabled(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.order_number_xpath)
    input_order = tracking_page.order_number_field()
    input_order.send_keys("BY123456-123456")
    check_button = tracking_page.button_tracking_order()
    assert not check_button.is_enabled()

def test_tracking_button_phone_disabled(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.order_number_xpath)
    input_phone = tracking_page.phone_number_field()
    input_phone.send_keys("375331234567")
    check_button = tracking_page.button_tracking_order()
    assert not check_button.is_enabled()


@pytest.mark.orderstatus
@pytest.mark.parametrize("order_number", ["BY123456-2", "12ABCJAJA"])
def test_track_order_number(driver_chrome, order_number):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.order_number_xpath)
    input_element = tracking_page.order_number_field()
    input_element.send_keys(order_number)
    tracking_page.wait_for_text_in_element(tracking_page.order_validation_xpath,
                                           "Пожалуйста, проверьте, правильно ли указан номер заказа.")
    assert tracking_page.validation_order_number().text == "Пожалуйста, проверьте, правильно ли указан номер заказа."


@pytest.mark.orderstatus
@pytest.mark.parametrize("phone_number", ["12312312", "ABCJAJA"])
def test_track_phone_number(driver_chrome, phone_number):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.phone_number_xpath)
    input_element = tracking_page.phone_number_field()
    input_element.send_keys(phone_number)
    tracking_page.wait_for_element(tracking_page.phone_validation_xpath)
    assert tracking_page.validation_phone_number().text == "Номер телефона должен состоять из 12 цифр."
