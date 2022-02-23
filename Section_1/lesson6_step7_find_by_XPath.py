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

link = "http://suninjuly.github.io/find_xpath_form"
driver = webdriver.Chrome()
try:
    driver.get(link)
    input1 = driver.find_element(By.XPATH, "//input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.XPATH, '//input[@class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.XPATH, '//input[@id="country"]')
    input4.send_keys("Russia")
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)#Делаем задержку, что бы скопировать ответ
    driver.quit()