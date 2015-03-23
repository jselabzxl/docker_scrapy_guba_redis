# -*- coding: utf-8 -*-

import sys
import time
import datetime
from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException

# 分别对应45、46、47、48、60、126
USERS_PWD = [('by1408144', '822851'), ('sy1308114', '19920113'), ('sy1108209', '822851'), \
        ('zy1408214', '09081370'), ('zy1408216', '08116817'), ('sy1208103', '19891130')]

idx = int(sys.argv[1])
USER_NAME, USER_PWD = USERS_PWD[idx]

def test_network():
    client = webdriver.Chrome()
    verified_url = 'http://202.112.136.131/index.html'
    client.get(verified_url)

    uname_input_element = client.find_element_by_name("uname")
    password_input_element = client.find_element_by_name("pass")
    submit_input_element = client.find_element_by_xpath("/html/body/table/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[6]/td/input[1]")

    uname_input_element.send_keys(USER_NAME)
    password_input_element.send_keys(USER_PWD)
    submit_input_element.click()

    confirm = client.switch_to_alert() # 获取对话框对象
    confirm.accept() # 点击“确认”

    print datetime.datetime.now(), 'verify and test network success'
    client.quit()

if __name__ == '__main__':
    while 1:
        test_network()
        time.sleep(60)
