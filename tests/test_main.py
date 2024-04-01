import pyautogui
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.main import MainPage
from locators.main_locators import MainLocators

# Checking that correct page is opened for Woman section(url)
def test_open_women_section(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.open_women_section()
    main_page.wait_for_url('https://www.lamoda.by/women-home/?sitelink=topmenuW')
    assert driver_chrome.current_url == 'https://www.lamoda.by/women-home/?sitelink=topmenuW'


# Checking that login pop-up is displayed after button click
def test_navigate_to_login(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    button=main_page.login_button()
    main_page.forced_click(button)# Клик по кнопке входа
    main_page.wait_for_element(main_page.login_button_popup)  # Ожидание появления всплывающего окна
    popup_element = main_page.login_popup()
    assert popup_element is not None


# Checking that search by item number opens item's page
def test_search_by_item_number(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.wait_for_element(main_page.search_bar_xpath)
    input_element= main_page.search_bar()
    item_number = "rtlack740303"
    input_element.send_keys(item_number)
    search_button = main_page.search_button()
    main_page.forced_click(search_button)
    main_page.wait_url_contains(item_number)
    assert item_number in driver_chrome.current_url


@pytest.mark.parametrize("email", ['dziyana.tarasava@gmail.com', 'dziyana@', 'dziyana@gmail'])
def test_login_disabled_button(driver_chrome, email):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    button = main_page.login_button()
    main_page.forced_click(button)
    main_page.wait_for_element(main_page.login_button_popup)
    current_position = pyautogui.position()
    pyautogui.typewrite(email)
    login_button_check = main_page.login_popup_button()
    assert not login_button_check.is_enabled()


# Checking that validation message appears for wrong email format
@pytest.mark.parametrize("invalid_email", ['dziyana', 'dziyana@', 'dziyana@gmail'])
def test_login_email_validation(driver_chrome, invalid_email):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.wait_for_element(main_page.login_button_xpath)
    button = main_page.login_button()
    main_page.forced_click(button)
    main_page.wait_for_element(main_page.login_button_popup)
    main_page.enter_text_pyautogui_current(invalid_email)
    pyautogui.press('tab')
    validation_check = main_page.login_popup_email_validation()
    assert validation_check.text == 'Пожалуйста, проверьте, правильно ли указан адрес'


@pytest.mark.socialmedia
def test_vk_link(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.vk_xpath)
    element = main_page.footer_vk()
    element.click()
    main_page.switch_to_second_tab()
    assert driver_chrome.current_url == 'https://vk.com/lamodaby?from=footer'


@pytest.mark.socialmedia
def test_twitter_link(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.twitter_xpath)
    element = main_page.footer_twitter()
    element.click()
    main_page.switch_to_second_tab()
    assert driver_chrome.current_url == 'https://twitter.com/Lamoda_by?from=footer'


@pytest.mark.socialmedia
def test_ok_link(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.ok_xpath)
    element = main_page.footer_ok()
    element.click()
    main_page.switch_to_second_tab()
    assert driver_chrome.current_url == 'https://ok.ru/group/52479738445918?from=footer'

def test_site_localization_kz(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.by_local)
    country = main_page.by_site()
    main_page.hover_over_element(country)
    kz = main_page.kz_site()
    main_page.forced_click(kz)
    assert driver_chrome.current_url == 'https://www.lamoda.kz/'

def test_site_localization_ru(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.by_local)
    country = main_page.by_site()
    main_page.hover_over_element(country)
    ru = main_page.ru_site()
    main_page.forced_click(ru)
    assert driver_chrome.current_url == 'https://www.lamoda.ru/'

@pytest.mark.parametrize("emails",['dziyana','dziyana@','dziyana@test', 'dziyana@test.'])
def test_subscription_validation_email(driver_chrome, emails):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.subscription_email)
    field = main_page.subscription_footer_email()
    field.click()
    main_page.enter_text_pyautogui_current(emails)
    pyautogui.press('tab')
    main_page.wait_for_element(main_page.email_validation)
    validation = main_page.subscription_validation_email()
    assert validation.text == 'Пожалуйста, проверьте, правильно ли указан адрес'

def test_acceptance_link(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.acceptance_link)
    main_page.acceptance_link_click()
    main_page.switch_to_second_tab()
    assert driver_chrome.current_url == 'https://a.lmcdn.ru/files/cms/consent-to-mailing.pdf'

def test_chat_open_popup(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.wait_for_element(main_page.chat_popup_button_xpath)
    button = main_page.chat_open_button()
    main_page.hover_over_element(button)
    button.click()
    main_page.switch_to_iframe((By.XPATH,main_page.chat_iframe_xpath))
    main_page.wait_for_element(main_page.chat_popup_header_xpath)
    popup_element = main_page.chat_open_header()
    assert "Напишите нам, операторы в сети!" in popup_element.text