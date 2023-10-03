from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# скролл странице вниз на 100px
browser.execute_script("window.scrollBy(0, 100);")

button1 = browser.find_element(By.ID, "book")
# говорим Selenium проверять в течение 12 секунд, пока сумманедостигет 100 баксов
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button1.click()


# скролл странице вниз на 200px
browser.execute_script("window.scrollBy(0, 200);")

x_element = browser.find_element(By.ID, "input_value")  # чтение текста на странице
x = x_element.text

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(calc(x))

# Отправляем заполненную форму

button2 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve")))
button2.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()