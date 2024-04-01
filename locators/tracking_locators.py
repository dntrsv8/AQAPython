class TrackingLocators:
    order_number_xpath = "//*[@name='input-order-number']"
    order_validation_xpath = "//div[@class='input__validation-message input__validation-message_default-theme']"
    phone_number_xpath = "//*[@name='input-phone']"
    phone_validation_xpath = "//*[@id='vue-root']//form//div[2]//div[contains(@class, 'input__validation-message')]"
    check_button_xpath = '//*[@class="x-button x-button_primaryFilledWeb7184 x-button_40 x-button_intrinsic-width"]'
    my_orders_xpath = "//*[@role='link' and text()='Мои заказы']"