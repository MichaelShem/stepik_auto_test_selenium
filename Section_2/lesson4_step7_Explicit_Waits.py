from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)#Это неявное ожидание

browser.get("http://suninjuly.github.io/wait2.html")

#в данном тесте кнопка становится активной только через 1 секунду, что бы драйвер не кликнул на нее, пока она неактивна, пропишем явное ожидание, применяя методы WebDriverWait и expected_conditions
button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'verify')))
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text