import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium import webdriver
from pages.main_page import MainPage

class TestQuestionsAboutImportant:
    
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def test_question_1_cost(self):
        # Сколько это стоит? И как оплатить?
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой." 
        actual_text = self.main_page.get_answer_text(0)  # Первый вопрос (индекс 0)

        assert expected_text in actual_text, (
            f"Ожидалось, что ответ будет содержать '{expected_text}', "
            f"но получил: '{actual_text}'"
        )

    def test_question_2_quauntity(self):
        # Хочу сразу несколько самокатов! Так можно?
        expected_text = ""
        actual_text = self.main_page.get_answer_text(1)  # Второй вопрос (индекс 1)

        assert expected_text in actual_text, (
            f"Ожидалось, что ответ будет содержать '{expected_text}', "
            f"но получил: '{actual_text}'"
        )

    def test_question_3_time(self):
        # Как рассчитывается время аренды?
        expected_text = ""
        actual_text = self.main_page.get_answer_text(2)  # Третий вопрос (индекс 2)

        assert expected_text in actual_text, (
            f"Ожидалось, что ответ будет содержать '{expected_text}', "
            f"но получил: '{actual_text}'"
        )

    def test_question_4_order_today(self):
        # Можно ли заказать самокат прямо на сегодня?
        expected_text = ""
        actual_text = self.main_page.get_answer_text(3)  # Четвёртый вопрос (индекс 3)

        assert expected_text in actual_text, (
            f"Ожидалось, что ответ будет содержать '{expected_text}', "
            f"но получил: '{actual_text}'"
        )

    def test_question_5_change_time(self):
        # Можно ли продлить заказ или вернуть самокат раньше?
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        actual_text = self.main_page.get_answer_text(4)  # Пятый вопрос (индекс 4)

        assert expected_text in actual_text, (
            f"Ожидалось, что ответ будет содержать '{expected_text}', "
            f"но получил: '{actual_text}'"
        )

    def test_question_6_charger(self):
        # Вы привозите зарядку вместе с самокатом?
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        actual_text = self.main_page.get_answer_text(5)  # Шестой вопрос (индекс 5)

        assert expected_text in actual_text, (
            f"Ожидалось, что ответ будет содержать '{expected_text}', "
            f"но получил: '{actual_text}'"
        )

    def test_question_7_cancel(self):
        # Можно ли отменить заказ?
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        actual_text = self.main_page.get_answer_text(6)  # Седьмой вопрос (индекс 6)

        assert expected_text in actual_text, (
            f"Ожидалось, что ответ будет содержать '{expected_text}', "
            f"но получил: '{actual_text}'"
        )

    def test_question_8_out_Moscow(self):
        # Я жизу за МКАДом, привезёте?
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        actual_text = self.main_page.get_answer_text(7)  # Восьмой вопрос (индекс 7)

        assert expected_text in actual_text, (
            f"Ожидалось, что ответ будет содержать '{expected_text}', "
            f"но получил: '{actual_text}'"
        )
    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()
