# Проект автоматизации тестирования сервиса Stellar Burgers

1. Основа для написания автотестов — фреймворк pytest и инструмент для автоматизации действий веб-браузера Selenium.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v. 

## Описание файлов с тестами
### Проверка успешного входа test_successful_sign_in.py 
* test_sign_in_by_button_sign_in - проверка входа через кнопку "Войти в аккаунт"
* test_sign_in_by_button_my_account - проверка входа через кнопку "Личный кабинет"
* test_sign_in_by_button_in_registration_form - проверка входа через кнопку "Войти" в окне регистрации
* test_sign_in_by_button_lost_password - проверка входа через кнопку "Войти" в окне восстановления пароля

### Проверка успешной регистрации в файле test_successful_registration.py
* test_first_registration - проверка успешной регистрации 
* test_password_length_less_than_six -  проверка регистрации с паролем меньше 6 символов

### Проверка перехода в личный кабинет и из личного кабинета в файле test_move_to_my_account.py
* test_move_to_page_my_account - проверка перехода в личный кабинет
* test_move_to_constructor_from_my_account - проверка перехода по клику на конструктор из личного кабинет
* test_move_to_logo_from_my_account -  проверка перехода по клику на логотип из личного кабинет

### Проверка выхода из личного кабинета в файле test_exit_from_account.py
* test_exit_from_my_account -  выход из личного кабинета по кнопке "Выйти"

### Проверка раздела "Конструктор" в файле test_move_pages_in_constructor.py
* test_move_to_sauce - переход к разделу "Соусы"
* test_move_to_loaf - переход к разделу "Булки"
* test_move_to_topping - переход к разделу "Начинки"

## Описание вспомогательных файлов
* В файле locators.py - локаторы элементов
* В файле conftest.py - используемые фикстуры
* В файле data.py - данные для авторизации
* В файле helpers.py - функции, генерирующие логин и пароль