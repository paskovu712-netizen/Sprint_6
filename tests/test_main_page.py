import pytest
import sys
import os
import allure

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium import webdriver
from pages.main_page import MainPage

class TestQuestionsAboutImportant:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.fixture(autouse=True)
    def setup(self):
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    @allure.feature('Раздел "Вопросы о важном"')
    @allure.story('Проверка ответа на вопрос о стоимости и оплате')
    @allure.title('Тест 1: Проверка текста ответа на вопрос "Сколько это стоит? И как оплатить?"')
    def test_question_1_cost(self):
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        actual_text = self.main_page.get_answer_text(0)

        with allure.step('Проверка содержания ответа'):
            assert expected_text in actual_text, (
                f"Ожидалось, что ответ будет содержать '{expected_text}', "
                f"но получил: '{actual_text}'"
            )

    @allure.feature('Раздел "Вопросы о важном"')
    @allure.story('Проверка ответа на вопрос о нескольких самокатах')
    @allure.title('Тест 2: Проверка текста ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def test_question_2_quauntity(self):
        expected_text = ""
        actual_text = self.main_page.get_answer_text(1)

        with allure.step('Проверка содержания ответа'):
            assert expected_text in actual_text, (
                f"Ожидалось, что ответ будет содержать '{expected_text}', "
                f"но получил: '{actual_text}'"
            )

    @allure.feature('Раздел "Вопросы о важном"')
    @allure.story('Проверка ответа на вопрос о расчёте времени аренды')
    @allure.title('Тест 3: Проверка текста ответа на вопрос "Как рассчитывается время аренды?"')
    def test_question_3_time(self):
        expected_text = ""
        actual_text = self.main_page.get_answer_text(2)

        with allure.step('Проверка содержания ответа'):
            assert expected_text in actual_text, (
                f"Ожидалось, что ответ будет содержать '{expected_text}', "
                f"но получил: '{actual_text}'"
            )

    @allure.feature('Раздел "Вопросы о важном"')
    @allure.story('Проверка ответа на вопрос о заказе на сегодня')
    @allure.title('Тест 4: Проверка текста ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def test_question_4_order_today(self):
        expected_text = ""
        actual_text = self.main_page.get_answer_text(3)

        with allure.step('Проверка содержания ответа'):
            assert expected_text in actual_text, (
                f"Ожидалось, что ответ будет содержать '{expected_text}', "
                f"но получил: '{actual_text}'"
            )

    @allure.feature('Раздел "Вопросы о важном"')
    @allure.story('Проверка ответа на вопрос о продлении/возврате заказа')
    @allure.title('Тест 5: Проверка текста ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_question_5_change_time(self):
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        actual_text = self.main_page.get_answer_text(4)

        with allure.step('Проверка содержания ответа'):
            assert expected_text in actual_text, (
                f"Ожидалось, что ответ будет содержать '{expected_text}', "
                f"но получил: '{actual_text}'"
            )

    @allure.feature('Раздел "Вопросы о важном"')
    @allure.story('Проверка ответа на вопрос о зарядке')
    @allure.title('Тест 6: Проверка текста ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def test_question_6_charger(self):
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        actual_text = self.main_page.get_answer_text(5)

        with allure.step('Проверка содержания ответа'):
            assert expected_text in actual_text, (
                f"Ожидалось, что ответ будет содержать '{expected_text}', "
                f"но получил: '{actual_text}'"
            )

    @allure.feature('Раздел "Вопросы о важном"')
    @allure.story('Проверка ответа на вопрос об отмене заказа')
    @allure.title('Тест 7: Проверка текста ответа на вопрос "Можно ли отменить заказ?"')
    def test_question_7_cancel(self):
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        actual_text = self.main_page.get_answer_text(6)

        with allure.step('Проверка содержания ответа'):
            assert expected_text in actual_text, (
                f"Ожидалось, что ответ будет содержать '{expected_text}', "
                f"но получил: '{actual_text}'"
            )

    @allure.feature('Раздел "Вопросы о важном"')
    @allure.story('Проверка ответа на вопрос о доставке за МКАД')
    @allure.title('Тест 8: Проверка текста ответа на вопрос "Я живу за МКАДом, привезёте?"')
    def test_question_8_out_Moscow(self):
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        actual_text = self.main_page.get_answer_text(7)

        with allure.step('Проверка содержания ответа'):
            assert expected_text in actual_text, (
                f"Ожидалось, что ответ будет содержать '{expected_text}', "
                f"но получил: '{actual_text}'"
            )

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
