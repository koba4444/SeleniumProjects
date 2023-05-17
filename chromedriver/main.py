import time
import random
from fake_useragent import UserAgent
#from selenium import webdriver
from seleniumwire import webdriver
from proxy_auth_data import login, password

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"

user_agent_list = [
    "hello",
    "ioweit9908",
    "2222",
    "33333",
    "55555"
]

useragent = UserAgent()
#options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
#options.add_argument("--proxy-server=45.145.57.238:11664")
proxy_options = {
    "proxy":{
        "https": f"http://{login}:{password}@45.145.57.238:11664"
    }
}


#driver = webdriver.Chrome(executable_path='/home/kok4444/PycharmProjects/SeleniumProjects/chromedriver/chromedriver',
#                         options=options)
driver = webdriver.Chrome(executable_path='/home/kok4444/PycharmProjects/SeleniumProjects/chromedriver/chromedriver',
                          seleniumwire_options=proxy_options)

try:
    driver.get("http://www.wallet.gamestop.com")
    time.sleep(2)
    driver.get_screenshot_as_file("1.png")
    driver.save_screenshot("2.png")

    driver.get('https://www.meduza.io')
    driver.get_screenshot_as_file("3.png")
    driver.save_screenshot("4.png")

    time.sleep(20002)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()