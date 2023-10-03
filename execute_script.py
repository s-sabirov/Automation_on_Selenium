from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

def  calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    button = browser.find_element(By.TAG_NAME, "button")
    x_element = browser.find_element(By.ID, "input_value") # чтение текста на странице
    x = x_element.text
    print(x, calc(x))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    # скролл странице вниз на 100px
    browser.execute_script("window.scrollBy(0, 100);")
    # кликаем на чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # кликаем на радиобатон
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

