from selenium import webdriver
import time

USERNAME = 'admin'
PASSWORD = 'admin'

driver = webdriver.Chrome(executable_path='C:\Python39\chromedriver.exe')
driver.get("http://127.0.0.1:8000/adminlogin")

user_input = driver.find_element_by_id('id_username')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('id_password')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('id_login')
time.sleep(300)
login_button.click()
