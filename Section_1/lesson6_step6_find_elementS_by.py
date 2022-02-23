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
from selenium.webdriver.common.by import By
#Что бы браузер сам закрывался при ошибках, будеи использовать исключения

site = "http://suninjuly.github.io/huge_form.html"
driver = webdriver.Chrome()
try:
    driver.get(site)
    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("some")
    button = driver.find_element(By.TAG_NAME, "button.btn")
    button.click()
finally:
    time.sleep(30)
    driver.quit()
