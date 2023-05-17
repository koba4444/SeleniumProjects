import time
import random
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from vk_auth_data import tel, password
from selenium.webdriver.common.keys import Keys

useragent = UserAgent()
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"


#options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent=user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
#options.add_argument("--proxy-server=45.145.57.238:11664")
options.add_argument('executable_path=/home/kok4444/PycharmProjects/SeleniumProjects/chromedriver/chromedriver')


driver = webdriver.Chrome(options=options)


try:
    driver.get("https://google.com/")
    time.sleep(2)
    email_input = driver.find_element(By.ID, "index_email")
    email_input.clear()
    email_input.send_keys(tel)
    time.sleep(2)
    email_input.send_keys(Keys.ENTER)
    #login_button = driver.find_elements(By.CLASS_NAME, "VkIdForm__signInButton")
    #login_button[0].click()
    time.sleep(2)
    password_input = driver.find_element(By.NAME, "password")
    time.sleep(2)
    password_input.clear()
    password_input.send_keys(password)

    time.sleep(2)
    password_input.send_keys(Keys.ENTER)
    #login_button1 = driver.find_element(By.CLASS_NAME,      "vkuiButton--sz-l")
    #login_button1.click()
    time.sleep(2)
    news_link = driver.find_element(By.ID, "l_msg").click()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()