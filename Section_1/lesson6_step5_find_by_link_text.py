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

site = "http://suninjuly.github.io/find_link_text"
driver = webdriver.Chrome()
x = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(x)
try:
    driver.get(site)
    link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(30)
    driver.quit()
