from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects1.html" #переход по ссылке на сайт
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.ID, "num1") # чтение текста на странице
    x1 = x1_element.text

    x2_element = browser.find_element(By.ID, "num2") #чтение текста на странице
    x2 = x2_element.text





    sum =str(int(x1) + int(x2))


    select = Select(browser.find_element(By.TAG_NAME, "select"))# выделение нужного элмента в списке
    select.select_by_visible_text(sum)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")# клик по кнопке submit
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
