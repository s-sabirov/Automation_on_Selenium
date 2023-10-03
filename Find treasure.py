from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def  calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считывание  x
    picture = browser.find_element(By.ID, 'treasure')
    x = picture.get_attribute('valuex')

    # выделение поля ввода
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    # кликаем на чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # кликаем на радиобатон
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print(x)
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
