import pytest
import sys
import os
import allure

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium import webdriver
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

# Наборы тестовых данных
TEST_DATA_SET_1 = {
    "name": "Иван",
    "surname": "Петров",
    "address": "ул. Ленина, д. 15",
    "station": "Тверская",
    "phone": "+79991234567",
    "data": "01.04.2026",
    "duration": "сутки"
}

TEST_DATA_SET_2 = {
    "name": "Мария",
    "surname": "Сидорова",
    "address": "пр. Мира, д. 42",
    "station": "Курская",
    "phone": "+79167654321",
    "data": "01.04.2026",
    "duration": "сутки"
}

@allure.feature('Оформление заказа самоката')
@allure.story('Проверка процесса заказа с разными наборами данных')
@pytest.mark.parametrize("test_data, order_button_method", [
    (TEST_DATA_SET_1, "click_order_button_top"),
    (TEST_DATA_SET_2, "click_order_button_bottom")
])
@allure.title("Тест заказа самоката: {test_data[name]} {test_data[surname]}, кнопка: {order_button_method}")
def test_order_scooter(driver, test_data, order_button_method):
    page = OrderPage(driver)
    page.open()

    with allure.step("1. Нажать кнопку «Заказать»"):
        if order_button_method == "click_order_button_top":
            page.click_order_button_top()
        else:
            page.click_order_button_bottom()

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

    with allure.step("4. Проверить переход на главную страницу при клике на логотип Самоката"):
        page.click_scooter_logo()
        assert "qa-scooter.praktikum-services.ru" in page.get_current_url(), "Не перешли на главную страницу Самоката"

    with allure.step("5. Проверить открытие Дзена при клике на логотип Яндекса"):
        page.click_yandex_logo()
        page.switch_to_new_window()
        assert "dzen.ru" in page.get_current_url(), "Не открылся Дзен в новом окне"
