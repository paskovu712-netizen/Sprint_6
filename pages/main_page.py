from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Открытие главной страницы")
    def open(self):
        self.driver.get(self.base_url)

    # Локаторы для раздела class = 'accordion'
    ACCORDION_SECTION = (By.CLASS_NAME, "accordion")
    QUESTION_ITEMS = (By.CSS_SELECTOR, ".accordion__item")
    QUESTION_TITLE = (By.CLASS_NAME, "accordion__button")
    ANSWER_CONTENT = (By.CLASS_NAME, "accordion__panel")

    @allure.step("Поиск секции аккордеона на странице")
    def get_accordion_section(self):
        return self.wait.until(EC.presence_of_element_located(self.ACCORDION_SECTION))

    @allure.step("Получение списка всех вопросов в секции аккордеона")
    def get_all_questions(self):
        accordion = self.get_accordion_section()
        return accordion.find_elements(*self.QUESTION_ITEMS)

    @allure.step("Клик по вопросу №{question_index} в секции 'Вопросы о важном'")
    def click_question(self, question_index):
        questions = self.get_all_questions()
        if 0 <= question_index < len(questions):
            question = questions[question_index]
            self.driver.execute_script("document.body.style.zoom='50%'")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
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
