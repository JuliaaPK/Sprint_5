from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestExitFromAccount:
    def test_exit_from_my_account(self, signin_my_account_driver):
        signin_my_account_driver.find_element(*Locators.button_exit).click()

        WebDriverWait(signin_my_account_driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.button_sign_in))

        assert signin_my_account_driver.current_url == "https://stellarburgers.nomoreparties.site/login"
