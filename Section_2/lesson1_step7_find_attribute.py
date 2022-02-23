'''
By.ID – поиск по уникальному атрибуту id элемента;
By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
By.XPATH – поиск элементов с помощью языка запросов XPath;
By.NAME – поиск по атрибуту name элемента;
By.TAG_NAME – поиск по названию тега;
By.CLASS_NAME – поиск по атрибуту class элемента;
By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.'''
#Более предпочтительно пользоваться универсальным методом find_element() и полей класса y из библиотеки selenium
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
#Что бы браузер сам закрывался при ошибках, будеи использовать исключения

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
site = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()
try:
    driver.get(site)
    key = driver.find_element(By.ID, "treasure")
    key_check = key.get_attribute("valuex")
    answer = calc(key_check)
    # Ввод ответа
    send_answer = driver.find_element(By.ID, "answer")
    send_answer.send_keys(answer)

    # Установка отметок
    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = driver.find_element(By.ID, "robotsRule")
    radio.click()

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(3)
    driver.quit()
