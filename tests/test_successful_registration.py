from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import GenerateDatesForLogin
from locators import Locators
from data import Data


class TestFirstRegistration:
    def test_first_registration(self, driver):
        driver.find_element(*Locators.button_signin_by_account).click()
        driver.find_element(*Locators.button_registration).click()
        driver.find_element(*Locators.name_field).send_keys(Data.NAME)
        driver.find_element(*Locators.email_field).send_keys(GenerateDatesForLogin.generate_new_email())
        driver.find_element(*Locators.password_field).send_keys(GenerateDatesForLogin.generate_new_password())
        driver.find_element(*Locators.button_reg_in_window_reg).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.button_sign_in))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_password_length_less_than_six(self,driver):
        driver.find_element(*Locators.button_signin_by_account).click()
        driver.find_element(*Locators.button_registration).click()
        driver.find_element(*Locators.name_field).send_keys(Data.NAME)
        driver.find_element(*Locators.email_field).send_keys(GenerateDatesForLogin.generate_new_email())
        driver.find_element(*Locators.password_field).send_keys(GenerateDatesForLogin.generate_password_length_less_six())
        driver.find_element(*Locators.button_reg_in_window_reg).click()

        assert driver.find_element(*Locators.incorrect_password_element)
