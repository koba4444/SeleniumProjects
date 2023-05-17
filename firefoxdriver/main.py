
#Вылетает ошибка
#selenium.common.exceptions.WebDriverException: Message: Process unexpectedly closed with status 127


import time
from selenium import webdriver
url = "https://www.instagram.com/"

driver = webdriver.Firefox(executable_path='/home/kok4444/PycharmProjects/SeleniumProjects/firefoxdriver/geckodriver')

try:
    driver.get('https://www.vk.ru/')
    driver.get_screenshot_as_file("1.png")
    driver.save_screenshot("2.png")
    time.sleep(1)
    driver.get('https://www.gosuslugi.ru/')
    driver.get_screenshot_as_file("3.png")
    driver.save_screenshot("4.png")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()