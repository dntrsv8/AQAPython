def forced_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

