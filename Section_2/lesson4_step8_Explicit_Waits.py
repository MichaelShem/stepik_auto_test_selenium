import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)#Это неявное ожидание будет искать элемент в течение 5 секунд(в данной задаче не нужнн)

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #в данном тесте нужно дождаться, когда цена будет 100, пропишем явное ожидание, применяя методы WebDriverWait и expected_conditions
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    #теперь кликаем
    button = browser.find_element(By.ID, 'book').click()

    #решаем задачку
    x = browser.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    answer = calc(x)

    # Вставляем овтет
    send_answer = browser.find_element(By.ID, "answer")
    send_answer.send_keys(answer)

    # Кликаем на отправку
    finish = browser.find_element(By.ID, 'solve').click()


finally:
    time.sleep(5)
    browser.quit()