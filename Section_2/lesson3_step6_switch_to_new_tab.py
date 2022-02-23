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

link = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
try:
    #открываем ссылку
    driver.get(link)

    #Нажимаем на кнопку
    click = driver.find_element(By.CLASS_NAME, 'trollface').click()

    #У нас открылась новая вкладка, нужно переключиться на нее
    new_window = driver.window_handles[1] #создали переменную, в которой указали имя новой вкладки с помощью метода window_handles
    switch = driver.switch_to.window(new_window)

    #ищем число и запускаем вынкцию по вычислению ответа
    x = driver.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    answer = calc(x)

    #Вставляем овтет
    send_answer = driver.find_element(By.ID, "answer")
    send_answer.send_keys(answer)

    #Кликаем на отправку
    button = driver.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(3)
    driver.quit()

