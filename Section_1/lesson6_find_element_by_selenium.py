"""
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/simple_form_find_task.html")
button = driver.find_element_by_id("submit_button")
print(button)
driver.quit()
"""
#Более предпочтительно пользоваться универсальным методом find_element() и полей класса y из библиотеки selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/simple_form_find_task.html")
button = driver.find_element(By.ID, "submit_button")
'''
By.ID – поиск по уникальному атрибуту id элемента;
By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
By.XPATH – поиск элементов с помощью языка запросов XPath;
By.NAME – поиск по атрибуту name элемента;
By.TAG_NAME – поиск по названию тега;
By.CLASS_NAME – поиск по атрибуту class элемента;
By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.'''
print(button)
driver.quit()