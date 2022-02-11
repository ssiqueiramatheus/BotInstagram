from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, passaword):
        self.username = username
        self.passaword = passaword
        self.driver = webdriver.Chrome(executable_path="C:\\dev\\tools\\drivers\\chromedriver.exe")

#//*[@id="react-root"]/section/main/article/div[2]/div/div/div[3]/span/button

#//*[@id="loginForm"]/div/div[1]/div/label/input

#//*[@id="loginForm"]/div/div[2]/div/label/input

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        usuario_button = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        usuario_button.clear()
        usuario_button.send_keys(self.username)

        senha_button = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        senha_button.clear()
        senha_button.send_keys(self.passaword)
        senha_button.send_keys(Keys.RETURN)
        time.sleep(5)


matheusBot = InstagramBot('eusoufoda', '123456')
matheusBot.login()