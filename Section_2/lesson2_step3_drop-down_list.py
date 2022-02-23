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
from selenium.webdriver.support.ui import Select #библиотека для выборки значений из выпадающих списков
#Что бы браузер сам закрывался при ошибках, будеи использовать исключения


site = "http://suninjuly.github.io/selects1.html"
driver = webdriver.Chrome()
try:
    driver.get(site)
    #нашли значение двух чисел и их сумму
    num1 = driver.find_element(By.ID, "num1").text
    num2 = driver.find_element(By.ID, "num2").text
    print(num1, num2)
    answer = int(num1) + int(num2)
    print(answer)
    #с помощью метода Select выберем ответ из выпадающего списка
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(answer))


    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    driver.quit()
