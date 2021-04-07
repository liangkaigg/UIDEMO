# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 18:01
# @Author  : LK
# @File    : page.py
from pages.basepage import Basepage
from business.locator import *
import time

class LoginPage(Basepage):
    """
    中台首页登陆
    """
    def send_uname(self,uname):
        self.send_text(login_locator.get("username"),uname)

    def send_pword(self,pword):
        self.send_text(login_locator.get("password"),pword)

    def click_button(self):
        self.click_element(login_locator.get("login_button"))


class  IndexPage(Basepage):
    """
    资产首页
    """
    def  click_index_herf(self):
        self.click_element(index_locator.get("index_herf"))

    def  click_searchlist_herf(self):
        self.click_element(index_locator.get("searchlist_herf"))


class SearchList(Basepage):
    """
    资产搜索
    """
    def send_tableName(self,tabname):
        self.click_element(searchlist_locator.get("clear_serach"))
        self.send_text(searchlist_locator.get("tab_serach"),tabname)

    def click_serach(self):
        self.click_element(searchlist_locator.get("serach_button"))

    def click_detail(self):
        self.click_element(searchlist_locator.get("table_detail"))

    def switch_serchlist(self):
        self.switch_windown()

class  RegisterData(Basepage):
    """数据源"""
    def click_dsManage(self):
        """点击数据源管理"""
        self.click_element(registerData_locator.get("ds_manage"))
        time.sleep(10)

    def  click_registerDs(self):
        """点击数据源登记"""
        self.click_element(registerData_locator.get("register_ds"))

    def  ds_detail(self):
        """查看数据源详情"""
        self.click_element(registerData_locator.get("check_ds"))
        self.scroll_to_bottom()

class  workBench(Basepage):
    def  click_workBench(self):
        """
        跳转工作台首页
        :return:
        """
        self.click_element(workBench_locator.get("index_href"))