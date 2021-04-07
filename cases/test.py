# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 17:17
# @Author  : LK
# @File    : test.py
from cases.base_Testcase import BaseTestcase
from parameterized import parameterized
import time

class TestLogin(BaseTestcase):
    # def setUp(self) -> None:
    #     self.basepage.open_home("http://168.61.114.19:8888/login/")
    #     self.handle = Login(self.driver)
    # def tearDown(self) -> None:
    #     self.basepage.delete_cookies()

    @parameterized.expand([("K1081222","ht123456")])
    def test_a_login_correct(self,username,password):
        self.handle.login(username,password)
        time.sleep(2)
        title =self.driver.title
        self.assertEqual(title,"数据中台",self.driver)

    def test_b_index(self):
        self.handle.go_index()
        self.handle.go_searchlist()

    def test_c_serchtable(self,tab='damp_data_asset'):
        self.handle.search_tab(tab)

    def test_d_detail(self):
        self.handle.check_tabdetail()

    def test_e_datasouce(self):
        self.handle.go_dsRegiter()
        self.handle.check_dsdetail()

    def test_f_workBench(self):
        self.handle.go_workBench()