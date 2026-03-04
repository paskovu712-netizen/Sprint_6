from asyncio.windows_events import NULL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открытие страницы")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Найти все элементы")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Кликнуть по элементу через скрипт")
    def click_script(self, locator):
        object = self.find(locator)
        self.driver.execute_script("arguments[0].click();", object)        

    @allure.step("Ввести текст")
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find(locator).text
    
    @allure.step("Проверить видимость элемента")
    def get_visibility(self, locator):
        return self.find(locator).is_displayed()
    
    @allure.step("Сфокусироваться на элементе")
    def focus_script(self,locator):
        self.driver.execute_script("document.body.style.zoom='50%'")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", locator)

    @allure.step("Масштаб 50%")
    def zoom50_script(self):
        self.driver.execute_script("document.body.style.zoom='50%'")

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        # Возвращает текущий URL
        return self.driver.current_url

    @allure.step("Переключение на новое окно браузера")
    def switch_to_new_window(self):
        # Переключается на новое окно браузера
        self.driver.switch_to.window(self.driver.window_handles[-1])
        import time
        time.sleep(2)
