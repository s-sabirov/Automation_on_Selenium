from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)


try:
    input1 = browser.find_element(By.XPATH, "//input[contains(@name, 'firstname')]")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.XPATH, "//input[contains(@name, 'lastname')]")
    input2.send_keys("Ivanov")

    input3 = browser.find_element(By.XPATH, "//input[contains(@name, 'email')]")
    input3.send_keys("fipim70319@bookspre.com")

    # загрузка файла

    current_dir = os.path.abspath(os.path.dirname(''))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Hello_world.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

