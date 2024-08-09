from locators import Locators


class TestMovementInConstructor:
    def test_move_to_sauce(self, driver):
        button_sauce = driver.find_element(*Locators.button_sauce)
        button_sauce.click()

        assert "tab_tab_type_current__2BEPc" in button_sauce.get_attribute("class").split(" ")

    def test_move_to_loaf(self, driver):
        driver.find_element(*Locators.button_sauce).click()
        button_loaf = driver.find_element(*Locators.button_loaf)
        button_loaf.click()

        assert "tab_tab_type_current__2BEPc" in button_loaf.get_attribute("class").split(" ")

    def test_move_to_topping(self, driver):
        button_topping = driver.find_element(*Locators.button_topping)
        button_topping.click()

        assert "tab_tab_type_current__2BEPc" in button_topping.get_attribute("class").split(" ")
