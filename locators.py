from selenium.webdriver.common.by import By


class Locators:
    button_signin_by_account = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]") # Кнопка "Войти в аккаунт"
    button_sign_in = (By.XPATH, ".//button[contains(text(),'Войти')]") # Кнопка "Войти" на странице логина
    button_sign_in_registration = (By.LINK_TEXT, "Войти") # Кнопка "Войти" в окне регистрации
    button_sign_in_lost_password = (By.LINK_TEXT, "Восстановить пароль") # Кнопка "Восстановить пароль" в окне на странице логина
    button_registration = (By.LINK_TEXT, 'Зарегистрироваться') # Кнопка "Зарегистрироваться" в окне логина
    button_sign_in_password_window = (By.LINK_TEXT, "Войти") # Кнопка "Войти" на странице восстановления пароля
    button_sauce = (By.XPATH, ".//span[(@class = 'text text_type_main-default') and (text() = 'Соусы')]/parent::*") # Кнопка "Соусы"
    button_loaf = (By.XPATH, ".//span[(@class = 'text text_type_main-default') and (text() = 'Булки')]/parent::*") # Кнопка "Булки"
    button_topping = (By.XPATH, ".//span[(@class = 'text text_type_main-default') and (text() = 'Начинки')]/parent::*") # Кнопка "Начинки"
    button_reg_in_window_reg = (By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]") # Кнопка "Зарегистрироваться" в окне регистрации
    button_order = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]") # Кнопка "Оформить заказ"
    button_my_account = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный Кабинет"
    button_profile = (By.LINK_TEXT, 'Профиль') # Кнопка "Профиль" в личном кабинете
    button_constructor = (By.XPATH, ".//p[contains(text(),'Конструктор')]") # Кнопка "Конструктор"
    button_exit = (By.XPATH, ".//button[contains(text(),'Выход')]") # Кнопка "Выход" в личном кабинете
    button_logo = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']/a") # Логотип Stellar Burgers
    email_field = (By.XPATH, ".//label[text() = 'Email']/following-sibling::*") # Поле "Email"
    name_field = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::*")  # Поле "Имя"
    password_field = (By.XPATH, ".//input[@name = 'Пароль']") # Поле "Пароль"
    incorrect_password_element = (By.XPATH, ".//p[text()='Некорректный пароль']") # Элемент с ошибкой про некорректный пароль
