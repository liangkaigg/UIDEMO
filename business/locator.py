# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 18:02
# @Author  : LK
# @File    : locator.py
from selenium.webdriver.common.by import By

login_locator ={
    "username" :(By.XPATH,"//input[@type='text']"),
    "password":(By.XPATH,"//input[@type='password']"),
    "login_button":(By.XPATH,"//button[@type='button']")
}

index_locator ={
    "index_herf" :(By.XPATH,"//a[@href='#/damp/index'][text()='数据资产']"),
    "searchlist_herf":(By.XPATH,"//span[@class='damp-input-group-addon']/button")
}

searchlist_locator={
    "tab_serach":(By.XPATH,"//div[@class='index_search_input__hysZn']//input"),
    "clear_serach":(By.XPATH,"//div[@class='index_list_header__3Scjx']/div/a"),
    "serach_button":(By.XPATH,"//div[@id='search_input']//button"),
    "table_detail":(By.XPATH,"//div[@class='damp-table-body']//td/a")
}

registerData_locator={
    "ds_manage":(By.XPATH,"//div[@class='damp-menu-submenu-title']//span[text()='数据源管理']"),
    "register_ds":(By.XPATH,"//a[@href='#/damp/thirdpage/registerData']"),
    "check_ds":(By.XPATH,"//div[@class='damp-table-body']//tr[1]/td/div/a[1]")
}


workBench_locator={
    "index_href":(By.XPATH,"//ul/li/a[text()='工作台']")
}