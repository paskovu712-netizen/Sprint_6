from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.base_page import BasePage
from curl import BASE_URL

class MainPage(BasePage):
    
    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.open(BASE_URL)

    # Локаторы для раздела class = 'accordion'
    ACCORDION_SECTION = (By.CLASS_NAME, "accordion")
    QUESTION_ITEMS = (By.CSS_SELECTOR, ".accordion__item")
    QUESTION_TITLE = (By.CLASS_NAME, "accordion__button")
    ANSWER_CONTENT = (By.CLASS_NAME, "accordion__panel")

    @allure.step("Поиск секции аккордеона на странице")
    def get_accordion_section(self):
        accordion_section = self.find(self.ACCORDION_SECTION)
        return accordion_section

    @allure.step("Получение списка всех вопросов в секции аккордеона")
    def get_all_questions(self):
        accordion = self.get_accordion_section()
        question_items = self.find_all(self.QUESTION_ITEMS)
        return question_items

    @allure.step("Клик по вопросу №{question_index} в секции 'Вопросы о важном'")
    def click_question(self, question_index):
        questions = self.get_all_questions()
        if 0 <= question_index < len(questions):
            question = questions[question_index]
            self.focus_script(question)
            self.wait.until(EC.element_to_be_clickable(question))
            question.find_element(*self.QUESTION_TITLE).click()

    @allure.step("Получение текста ответа на вопрос №{question_index}")
    def get_answer_text(self, question_index):
        questions = self.get_all_questions()
        if 0 <= question_index < len(questions):
            self.click_question(question_index)
            answer_element = questions[question_index].find_element(*self.ANSWER_CONTENT)
            self.wait.until(EC.visibility_of(answer_element))
            
            return answer_element.text.strip()

        return ""
