'''
By.ID – поиск по уникальному атрибуту id элемента;
By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
By.XPATH – поиск элементов с помощью языка запросов XPath;
By.NAME – поиск по атрибуту name элемента;
By.TAG_NAME – поиск по названию тега;
By.CLASS_NAME – поиск по атрибуту class элемента;
By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.'''

# Более предпочтительно пользоваться универсальным методом find_element() и полей класса y из библиотеки selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
# Что бы браузер сам закрывался при ошибках, будеи использовать исключения

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()
try:
    driver.get(link)
    #Найдет значение х и его математическую функция
    x = driver.find_element(By.ID, "input_value").text
    answer = calc(x)
    #С помощью JavaScript проскролим вниз
    driver.execute_script("window.scrollBy(0, 100);")

    #Введем ответ
    send_answer = driver.find_element(By.ID, "answer")
    send_answer.send_keys(answer)

    #ставим галочки
    checkbox = driver.find_element(By.ID, 'robotCheckbox').click()
    radio = driver.find_element(By.ID, 'robotsRule').click()

    # кликаем
    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(3)
    driver.quit()

