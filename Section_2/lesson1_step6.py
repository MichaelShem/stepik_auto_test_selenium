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
site = "http://suninjuly.github.io/math.html"
driver = webdriver.Chrome()
try:
    driver.get(site)
    people_radio = driver.find_element(By.ID, "peopleRule")
    # проверяем присутствие атрибута в элементе, в данном случае то, что радио кнопка выбрана по умолчанию
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = driver.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

finally:
    time.sleep(3)
    driver.quit()
