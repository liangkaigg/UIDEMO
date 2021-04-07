# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 15:35
# @Author  : LK
# @File    : overwrite_TestCase.py
import  unittest
from  util.logger import Logger
from  util.common import *

class NewTestCase(unittest.TestCase):
    logger = Logger()
    def assertEqual_new(self,first,second,msg,driver):
        try:
            self.assertEqual(first,second,msg)
        except Exception as e:
            self.input_log_and_save_screenshot(str(e),driver)
            raise

    def assertIn_new(self,first,second,msg,driver):
        try:
            self.assertIn(first,second,msg)
        except Exception as e:
            self.input_log_and_save_screenshot(str(e),driver)
            raise

    def assertIs_new(self, first, second, msg, driver):
        try:
            self.assertIs(first, second, msg)
        except Exception as e:
            self.input_log_and_save_screenshot(str(e), driver)
            raise

    def assertisNone_new(self, exp, msg, driver):
        try:
            self.assertIsNone(exp, msg)
        except Exception as e:
            self.input_log_and_save_screenshot(str(e), driver)
            raise

    def input_log_and_save_screenshot(self, exc, driver):
        self.logger.erro("断言失败"+exc)
        save_screen_shot(driver)

