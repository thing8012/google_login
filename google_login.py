from selenium import webdriver
import os
import time

chrome_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
web = webdriver.Chrome(chrome_path)
url = "https://www.google.com"
web.get(url)
web.find_element_by_xpath('//*[@id="gb_70"]').click()
time.sleep(.5)
account = "your account"
password = "your password"

web.find_element_by_xpath('//*[@id="identifierId"]').send_keys(account)
time.sleep(.5)
web.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(.5)
web.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
time.sleep(1)
web.find_element_by_xpath('//*[@id="passwordNext"]').click()
