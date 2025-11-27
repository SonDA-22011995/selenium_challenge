import os
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER_NAME = "sonda@gmail.com"
PASSWORD = "son22011995"
CLASS = ["yoga","spin","hiit"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# go to the gym page
url = "https://appbrewery.github.io/gym/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

WebDriverWait(driver, 10)

# move to login page
login_bt = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="login-button"]'))
)
login_bt.click()


# fill email, password input and login
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="email-input"]'))
)
email_input.clear()
email_input.send_keys(USER_NAME)
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="password-input"]'))
)
password_input.clear()
password_input.send_keys(PASSWORD)
login_bt = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="submit-button"]'))
)
login_bt.click()

# # Book the upcoming Tuesday class
content = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,"__next"))
)

today = datetime.now()

def get_next_tuesday(date: datetime) ->datetime:
    # day_index = date.weekday()
    # match day_index:
    #     # monday
    #     case 0:
    #         tuesday = date + timedelta(days=1)
    #     # tuesday
    #     case 1:
    #         tuesday = date + timedelta(days=7)
    #     # wednesday
    #     case 2:
    #         tuesday = date + timedelta(days=6)
    #     # thursday
    #     case 3:
    #         tuesday = date + timedelta(days=5)
    #     # friday
    #     case 4:
    #         tuesday = date + timedelta(days=4)
    #     # saturday
    #     case 5:
    #         tuesday = date + timedelta(days=3)
    #     # sunday
    #     case 6:
    #         tuesday = date + timedelta(days=2)
    # return tuesday
    days = (1 - date.weekday()) % 7
    if days == 0:
        days = 7
    return date + timedelta(days=days)

tuesday = get_next_tuesday(today)
id = f'{tuesday.strftime("%Y-%m-%d")}-1800'

for class_type in CLASS:
    card_id_temp = f'class-card-{class_type}-{id}'
    card = None
    try:
        card = content.find_element(By.ID, card_id_temp)

        available_id = f'class-availability-{class_type}-{id}'
        available = card.find_element(By.ID, available_id)
        available_num = available.text.replace("Available:","")
        available_num = available_num.replace("spots", "")
        available_num = available_num.strip()
        available_num = available_num.split(" / ")

        if int(available_num[1]) > int(available_num[0]):
            button_id = f"book-button-{class_type}-{id}"
            button = card.find_element(By.ID, button_id)
            if button.is_enabled():
                button.click()
                print(f"Booked: {class_type} Class on {id}")
            else:
                print(f"You already booked {class_type} Class on {id}")
            break
    except Exception as e:
        print(f'id="{card_id_temp}" is not found')




