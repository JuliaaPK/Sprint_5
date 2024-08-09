import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.STELLAR_BURGER_URL)
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture
def signin_my_account_driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.STELLAR_BURGER_URL)
    chrome_driver.find_element(*Locators.button_signin_by_account).click()
    chrome_driver.find_element(*Locators.email_field).send_keys(Data.EMAIL_INPUT_DATA)
    chrome_driver.find_element(*Locators.password_field).send_keys(Data.PASSWORD_INPUT_DATA)
    chrome_driver.find_element(*Locators.button_sign_in).click()

    WebDriverWait(chrome_driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.button_order))

    chrome_driver.find_element(*Locators.button_my_account).click()

    WebDriverWait(chrome_driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.button_profile))

    yield chrome_driver
    chrome_driver.quit()
