from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Создание опций для режима инкогнито чтобы не выходить из аккаунта, если авторизация в браузере уже была
chrome_options = webdriver.ChromeOptions()
driver.get("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")
favorite_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Добавить в избранное')]")
favorite_button.click()
driver.quit()