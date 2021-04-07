# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 14:37
# @Author  : LK
# @File    : run.py
import unittest,os
from util.common import  get_report_path
from util.HTMLTestRunner_cn import HtmlTestRunner


def run():
    test_path =os.path.dirname(__file__)+"/cases"
    report_path =get_report_path()
    suite =unittest.defaultTestLoader.discover(test_path)
    with open(report_path,"wb") as f:
        runner = HtmlTestRunner(
            stream=f,
            title="UI report",
            description="自动化测试报告",
            retry=1
        )
        runner.run(suite)
if __name__ == '__main__':
    run()