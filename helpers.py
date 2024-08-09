import random


class GenerateDatesForLogin:

    @staticmethod
    def generate_new_email():
        return f'testnameperevezentceva{random.randint(100, 900)}@yandex.ru'

    @staticmethod
    def generate_new_password():
        return f'{random.randint(100000, 999999)}'

    @staticmethod
    def generate_password_length_less_six():
        return f'{random.randint(100, 999)}'
