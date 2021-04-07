# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 16:27
# @Author  : LK
# @File    : base_Testcase.py
from util.overwrite_TestCase import NewTestCase
from webDriver.driver_factory import DriverFactory
from util.logger import Logger
from pages.basepage import Basepage
from business.handle import Handle
import  time
class BaseTestcase(NewTestCase):
    driver =None
    logger =Logger()

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info("----开始执行测试----")
        cls.driver =DriverFactory.get_driver()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.basepage =Basepage(cls.driver)
        cls.basepage.open_home("http://168.61.114.19:8888/login/")
        cls.handle = Handle(cls.driver)
    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(10)
        cls.driver.quit()
        cls.logger.info("----结束测试-----")

