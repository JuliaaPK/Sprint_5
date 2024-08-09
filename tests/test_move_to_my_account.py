from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestMoveFromPages:
    def test_move_to_page_my_account(self, signin_my_account_driver):
        assert signin_my_account_driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_move_to_constructor_from_my_account(self, signin_my_account_driver):
        signin_my_account_driver.find_element(*Locators.button_constructor).click()

        WebDriverWait(signin_my_account_driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.button_my_account))

        assert signin_my_account_driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_move_to_logo_from_my_account(self, signin_my_account_driver):
        signin_my_account_driver.find_element(*Locators.button_logo).click()

        WebDriverWait(signin_my_account_driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.button_my_account))

        assert signin_my_account_driver.current_url == "https://stellarburgers.nomoreparties.site/"
