# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 14:31
# @Author  : LK
# @File    : test.py

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.switch_to.window()