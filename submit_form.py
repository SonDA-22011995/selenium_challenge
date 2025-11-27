from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.clear()
first_name.send_keys("sonda")

last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
last_name.clear()
last_name.send_keys("sonda")

email = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email.clear()
email.send_keys("sonda@gmail.com")

sign_up = driver.find_element(By.XPATH, '/html/body/form/button')
sign_up.click()


assert "Success" in driver.page_source