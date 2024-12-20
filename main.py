from time import sleep
from os import getenv
from dotenv import load_dotenv

from selenium import webdriver
# Импортируем классы для Chrome. Если у вас другой браузер - измените импорт.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()


# DJANGO_URL = getenv('LOGIN_URL')
DJANGO_URL = 'https://login.mos.ru/sps/login/methods/password?bo=%2Fsps%2Foauth%2Fae%3Fresponse_type%3Dcode%26access_type%3Doffline%26client_id%3Ddnevnik.mos.ru%26scope%3Dopenid%2Bprofile%2Bbirthday%2Bcontacts%2Bsnils%2Bblitz_user_rights%2Bblitz_change_password%26redirect_uri%3Dhttps%3A%2F%2Fschool.mos.ru%2Fv3%2Fauth%2Fsudir%2Fcallback'
USERNAME = getenv('USERNAME')
PASSWORD = getenv('PASSWORD')
PAUSE_DURATION_SECONDS = 1
PAUSE = 40

if __name__ == '__main__':
    # Запуск веб-драйвера.
    driver = webdriver.Safari()
    # Открытие страницы по заданному адресу.
    driver.get(DJANGO_URL)
    # Развёртывание окна на полный экран.
    driver.maximize_window()
    # Здесь и далее паузы, чтобы рассмотреть происходящее.
    sleep(PAUSE_DURATION_SECONDS)

    # Поиск в содержимом страницы поля для логина.
    # Возможные варианты для поиска:
    # ID, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, 
    # NAME, TAG_NAME, CLASS_NAME, CSS_SELECTOR
    username_input = driver.find_element(By.NAME, 'login')
    # Ввод логина при помощи имитации ввода с клавиатуры.
    username_input.send_keys(USERNAME)
    sleep(PAUSE_DURATION_SECONDS)

    # Поиска поля для пароля.
    password_input = driver.find_element(By.NAME, 'password')
    # Ввод пароля.
    password_input.send_keys(PASSWORD)
    sleep(PAUSE_DURATION_SECONDS)

    # Поиск кнопки "Войти".
    submit_button = driver.find_element(By.TAG_NAME, 'button')
    # Эмуляция щелчка мышью.
    submit_button.click()
    sleep(PAUSE)

    # Сохранение скриншота страницы с заданным именем.
    # driver.save_screenshot('screenshot.png')
    # sleep(PAUSE_DURATION_SECONDS)

    # # Поиск первого поста на странице по классу.
    # first_post = driver.find_element(By.CLASS_NAME, 'diary-emotion-cache-12iwo17-content')
    # # Вывод текста найденного элемента в терминал.
    # print(first_post.text)
    # # Закрытие веб-драйвера.
    driver.quit()