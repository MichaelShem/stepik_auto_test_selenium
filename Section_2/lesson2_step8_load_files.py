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
import os #Модель позволяет работать с операционной системой(причем с любой)

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
try:
    #открываем ссылку
    driver.get(link)

    #Ищем и заполняем поля для ввода
    f_name = driver.find_element(By.CSS_SELECTOR, 'input:nth-child(2)').send_keys('Michael')
    l_name = driver.find_element(By.CSS_SELECTOR, 'input:nth-child(4)').send_keys('Shemyakin')
    email = driver.find_element(By.CSS_SELECTOR, 'input:nth-child(6)').send_keys('Minya2044@yandex.ru')

    #Теперь найдет кнопку загрузки файла и загрузим файл
    load_file = driver.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__)) #Получает путь к директории тукущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла

    load_file.send_keys(file_path) #с помощью этой команды передаем файл в кнопку для загрузки файла

    # кликаем
    button = driver.find_element_by_tag_name("button")
    button.click()


finally:
    time.sleep(3)
    driver.quit()

