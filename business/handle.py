# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 9:35
# @Author  : LK
# @File    : handle.py
from pages.page import *
from util.logger import Logger
import time

class Handle:
    logger =Logger()
    def __init__(self,driver):
        """
        初始化page对象
        :param driver:
        """
        self.driver=driver
        self.loginpage = LoginPage(self.driver)
        self.indexpage = IndexPage(self.driver)
        self.searchlist= SearchList(self.driver)
        self.dsRegister =RegisterData(self.driver)
        self.workBench = workBench(self.driver)

    def  login(self,uname,pword):
        """
        中台登录
        :param uname:
        :param pword:
        :return:
        """
        self.logger.info("-----正在开始登陆数据中台-----")
        self.loginpage.send_uname(uname)
        self.loginpage.send_pword(pword)
        self.loginpage.click_button()
        self.logger.info("")
    def  go_index(self):
        """
        跳转中台首页
        :return:
        """
        self.logger.info("----正在前往数据资产首页-----")
        self.indexpage.click_index_herf()

    def  go_searchlist(self):
        """
        进入数据资产二级页面
        :return:
        """
        self.logger.info("---进入数据资产二级页面-----")
        self.indexpage.click_searchlist_herf()

    def  search_tab(self,table):
        """
        高搜功能搜索表
        :param table:
        :return:
        """
        self.logger.info("---搜索数据表---")
        self.searchlist.send_tableName(table)
        self.searchlist.click_serach()
        time.sleep(5)

    def  check_tabdetail(self):
        """
        查看表详情
        :return:
        """
        self.logger.info("---查看表详情---")
        self.searchlist.click_detail()
        time.sleep(10)

    def go_dsRegiter(self):
        self.searchlist.switch_windown()
        self.logger.info("---前往数据源登记页面---")
        self.dsRegister.click_dsManage()
        self.dsRegister.click_registerDs()

    def check_dsdetail(self):
        self.dsRegister.ds_detail()
        time.sleep(10)

    def go_workBench(self):
        self.workBench.click_workBench()
        time.sleep(10)