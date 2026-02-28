from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие главной страницы Яндекс Самоката")
    def open(self):
        # Открывает главную страницу Яндекс Самоката
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    # Локаторы элементов
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//button[text()='Заказать']")
    ORDER_BUTTON_MIDDLE = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(2)")
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
        button = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_TOP))
        button.click()

    @allure.step("Нажатие кнопки «Заказать» внизу страницы")
    def click_order_button_bottom(self):
        # Нажимает кнопку «Заказать» внизу страницы
        self.driver.execute_script("document.body.style.zoom='50%'")
        button = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_BOTTOM))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()

    @allure.step("Заполнение формы «Для кого» (имя: {name}, фамилия: {surname})")
    def fill_order_form_for_whom(self, name, surname, address, station, phone):
        # Заполняет первую форму заказа для кого
        name_field = self.wait.until(EC.visibility_of_element_located(self.NAME_FIELD))
        name_field.send_keys(name)

        surname_field = self.driver.find_element(*self.SURNAME_FIELD)
        surname_field.send_keys(surname)

        address_field = self.driver.find_element(*self.ADDRESS_FIELD)
        address_field.send_keys(address)

        station_field = self.driver.find_element(*self.STATION_FIELD)
        station_field.send_keys(station)
        option = self.wait.until(EC.element_to_be_clickable(self.STATION_ITEM))
        option.click()

        phone_field = self.driver.find_element(*self.PHONE_FIELD)
        phone_field.send_keys(phone)
        # Нажимает кнопку Далее
        next_button = self.driver.find_element(*self.NEXT_BUTTON)
        next_button.click()

    @allure.step("Заполнение формы «Аренда» (дата: {data}, длительность: {duration})")
    def fill_order_form_rent(self, data, duration):
        # Заполняет вторую форму заказа Аренда
        data_field = self.driver.find_element(*self.DATA_FIELD)
        data_field.send_keys(data)

        duration_list = self.wait.until(EC.element_to_be_clickable(self.DURATION_DROPDOWN))
        duration_list.click()

        duration_option = self.driver.find_element(*self.DURATION_OPTION)
        duration_option.click()
        # Нажимает кнопку Заказать
        order_button = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_MIDDLE))
        import time
        time.sleep(2)
        order_button.click()

    @allure.step("Подтверждение заказа (нажатие кнопки «Да»)")
    def answer_order_question(self):
        # Нажимает кнопку Да в окне подтверждения заказа
        yes = self.wait.until(EC.element_to_be_clickable(self.YES_BUTTON))
        yes.click()

    @allure.step("Проверка отображения сообщения об успешном заказе")
    def is_success_message_displayed(self):
        # Проверяет отображение сообщения об успешном заказе
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
            return True
        except:
            return False

    @allure.step("Клик на логотип Самоката")
    def click_scooter_logo(self):
        # Кликает на логотип Самоката
        logo = self.wait.until(EC.element_to_be_clickable(self.LOGO_SCOOTER))
        self.driver.execute_script("arguments[0].click();", logo)

    @allure.step("Клик на логотип Яндекса")
    def click_yandex_logo(self):
        # Кликает на логотип Яндекса
        logo = self.wait.until(EC.element_to_be_clickable(self.LOGO_YANDEX))
        logo.click()

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
