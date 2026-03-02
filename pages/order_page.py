from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.base_page import BasePage
from curl import BASE_URL

class OrderPage(BasePage):

    @allure.step("Открытие главной страницы Яндекс Самоката")
    def open_main_page(self):
        self.open(BASE_URL)

    # Локаторы элементов
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//button[text()='Заказать']")
    ORDER_BUTTON_MIDDLE = (By.XPATH, ".//button[text()='Заказать'and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    STATION_ITEM = (By.XPATH, ".//li[contains(text(), station)]")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DATA_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DURATION_DROPDOWN = (By.CSS_SELECTOR, ".Dropdown-control")
    DURATION_OPTION = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(1)")
    YES_BUTTON = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")

    @allure.step("Нажатие кнопки «Заказать» вверху страницы")
    def click_order_button_top(self):
        # Нажимает кнопку «Заказать» вверху страницы
        self.driver.execute_script("document.body.style.zoom='50%'")
        self.click(self.ORDER_BUTTON_TOP)

    @allure.step("Нажатие кнопки «Заказать» внизу страницы")
    def click_order_button_bottom(self):
        # Нажимает кнопку «Заказать» внизу страницы
        self.driver.execute_script("document.body.style.zoom='50%'")
        self.click(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Заполнение формы «Для кого» (имя: {name}, фамилия: {surname})")
    def fill_order_form_for_whom(self, name, surname, address, station, phone):
        # Заполняет первую форму заказа для кого
        self.type(self.NAME_FIELD, name)
        self.type(self.SURNAME_FIELD, surname)
        self.type(self.ADDRESS_FIELD, address)

        station_field = self.driver.find_element(*self.STATION_FIELD)
        station_field.send_keys(station)
        option = self.wait.until(EC.element_to_be_clickable(self.STATION_ITEM))
        option.click()

        self.type(self.PHONE_FIELD, phone)
        # Нажимает кнопку Далее
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнение формы «Аренда» (дата: {data}, длительность: {duration})")
    def fill_order_form_rent(self, data, duration):
        # Заполняет вторую форму заказа Аренда
        self.type(self.DATA_FIELD, data)
        self.click(self.DURATION_DROPDOWN)
        self.click(self.DURATION_OPTION)
        
        # Нажимает кнопку Заказать
        self.click(self.ORDER_BUTTON_MIDDLE)

    @allure.step("Подтверждение заказа (нажатие кнопки «Да»)")
    def answer_order_question(self):
        self.click(self.YES_BUTTON)

    @allure.step("Проверка отображения сообщения об успешном заказе")
    def is_success_message_displayed(self):
        # Проверяет отображение сообщения об успешном заказе
        try:
            self.get_visibility(self.SUCCESS_MESSAGE)
            return True
        except:
            return False

    @allure.step("Клик на логотип Самоката")
    def click_scooter_logo(self):
        # Кликает на логотип Самоката
        self.click_script(self.LOGO_SCOOTER)

    @allure.step("Клик на логотип Яндекса")
    def click_yandex_logo(self):
        # Кликает на логотип Яндекса
        self.click(self.LOGO_YANDEX)

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
