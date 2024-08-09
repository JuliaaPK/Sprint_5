from locators import Locators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSuccessfulSignIn:
    def test_sign_in_by_button_sign_in(self, driver):
        driver.find_element(*Locators.button_signin_by_account).click()
        driver.find_element(*Locators.email_field).send_keys(Data.EMAIL_INPUT_DATA)
        driver.find_element(*Locators.password_field).send_keys(Data.PASSWORD_INPUT_DATA)
        driver.find_element(*Locators.button_sign_in).click()

        WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located(Locators.button_order))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_sign_in_by_button_my_account(self, driver):
        driver.find_element(*Locators.button_my_account).click()
        driver.find_element(*Locators.email_field).send_keys(Data.EMAIL_INPUT_DATA)
        driver.find_element(*Locators.password_field).send_keys(Data.PASSWORD_INPUT_DATA)
        driver.find_element(*Locators.button_sign_in).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.button_order))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_sign_in_by_button_in_registration_form(self, driver):
        driver.find_element(*Locators.button_signin_by_account).click()
        driver.find_element(*Locators.button_registration).click()
        driver.find_element(*Locators.button_sign_in_registration).click()
        driver.find_element(*Locators.email_field).send_keys(Data.EMAIL_INPUT_DATA)
        driver.find_element(*Locators.password_field).send_keys(Data.PASSWORD_INPUT_DATA)
        driver.find_element(*Locators.button_sign_in).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.button_order))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_sign_in_by_button_lost_password(self, driver):
        driver.find_element(*Locators.button_signin_by_account).click()
        driver.find_element(*Locators.button_sign_in_lost_password).click()
        driver.find_element(*Locators.button_sign_in_password_window).click()
        driver.find_element(*Locators.email_field).send_keys(Data.EMAIL_INPUT_DATA)
        driver.find_element(*Locators.password_field).send_keys(Data.PASSWORD_INPUT_DATA)
        driver.find_element(*Locators.button_sign_in).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.button_order))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
