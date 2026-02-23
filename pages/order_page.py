from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Класс домашней страницы
class HomePageScooter:
    # локатор для элемента "Самокат на пару дней"
    header_user = [By.CLASS_NAME, 'Home_Header__iJKdX']

    def __init__(self, driver):
        self.driver = driver

    # метод ожидания загрузки страницы
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.header_user))
    
    # метод для получения текста элемента
    def text_in_home_page(self):
        return self.driver.find_element(*self.header_user).text
