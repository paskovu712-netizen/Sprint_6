import pytest
import sys
import os
import allure

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium import webdriver
from pages.order_page import OrderPage
from data_pak import *

class TestOrderPage:

    @allure.feature('Оформление заказа самоката')
    @allure.story('Проверка процесса заказа с разными наборами данных')
    @pytest.mark.parametrize("test_data, order_button_method", [
        (TEST_DATA_SET_1, "click_order_button_top"),
        (TEST_DATA_SET_2, "click_order_button_bottom")
    ])
    @allure.title("Тест заказа самоката: {test_data[name]} {test_data[surname]}, кнопка: {order_button_method}")
    def test_order_scooter(self, driver, test_data, order_button_method):
        page = OrderPage(driver)
        page.open_main_page()

        with allure.step("1. Нажать кнопку «Заказать»"):
            methods = {
                "click_order_button_top": page.click_order_button_top,
                "click_order_button_bottom": page.click_order_button_bottom
            }
            methods[order_button_method]()

        with allure.step("2. Заполнить формы заказа"):
            page.fill_order_form_for_whom(
                test_data["name"],
                test_data["surname"],
                test_data["address"],
                test_data["station"],
                test_data["phone"]
            )

            page.fill_order_form_rent(
                test_data["data"],
                test_data["duration"],
            )

            page.answer_order_question()

        with allure.step("3. Проверить сообщение об успешном создании заказа"):
            assert page.is_success_message_displayed(), "Сообщение об успешном заказе не появилось"

    def test_scooter_logo_click(self, driver):
        with allure.step("4. Проверить переход на главную страницу при клике на логотип Самоката"):
            page = OrderPage(driver)
            page.open_main_page()
            page.click_scooter_logo()
            assert "qa-scooter.praktikum-services.ru" in page.get_current_url(), "Не перешли на главную страницу Самоката"

    def test_yandex_logo_click(self, driver):
        with allure.step("5. Проверить открытие Дзена при клике на логотип Яндекса"):
            page = OrderPage(driver)
            page.open_main_page()
            page.click_yandex_logo()
            page.switch_to_new_window()
            assert "dzen.ru" in page.get_current_url(), "Не открылся Дзен в новом окне"
