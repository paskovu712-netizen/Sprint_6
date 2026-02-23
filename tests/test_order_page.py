import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page  import OrderPageScooter

# класс с автотестом
class TestHomePage:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        #cls.driver = webdriver.Chrome()

    def test_check_test_in_order_page(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

        # создай объект класса домашней страницы
        order_page = OrderPageScooter(self.driver)

        # дождись загрузки домашней страницы
        order_page.wait_for_load_order_page()

        # получи текст элемента в заголовке
        text_order_page = order_page.text_in_order_page()

        # сделай проверку, что полученное значение совпадает c email
        assert 'Для кого самокат' in text_order_page

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()
