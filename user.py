from random import random, choice
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime


class User:
    """Your discord account"""
    def __init__(self, url):
        # Url of the website you want to automatically access
        self.url = url

        # Driver of the browser you use
        self.driver = webdriver.Chrome("./chromedriver.exe")
        self.driver.get(self.url)


    def login(self):
        """Login to discord"""
        #self.driver.find_element_by_name('email').send_keys(self.email)
        #self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_name('password').send_keys(Keys.ENTER)

    def goto(self, url):
        self.browse = self.driver.get(url)

    def select_text(self, text):
        self.log("Click "+text)
        ele = self.driver.find_element_by_xpath('//button[@type="button" and contains(., "'+text+'")]')
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        ele.click()

    def select_dropdown(self, text):
        self.log("Select")
        ele = self.driver.find_element_by_xpath('//span[contains(., "'+text+'")]')
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        ele.click()
        
    def select_dropdown_random_option(self):
        self.log("Select random option")
        self.driver.find_element_by_xpath('//div[@role="option"]').click()

    def choose(self):
        """Choose where to send messages"""
        self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[2]/div[2]').click()
        self.driver.find_element_by_xpath('//*[@id="channels"]/div/div[4]').click()

    def send_message(self, msg):
        """Send messages to text channel"""
        msg_xpath = '//div[@role="textbox"]'
        enter_xpath = '//div[@role="textbox"]'
        self.driver.find_element_by_xpath(msg_xpath).send_keys(msg)
        self.driver.find_element_by_xpath(enter_xpath).send_keys(Keys.ENTER)
        self.log(msg)

    def log(self, msg):
        """Msg log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')
