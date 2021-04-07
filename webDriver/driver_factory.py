# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 15:59
# @Author  : LK
# @File    : driver_factory.py
import os
from selenium import  webdriver
from util.logger import Logger
class DriverFactory:
    """
        # singleton
        单例模式，保证全局只有有一个driver
    """
    _instance= None
    _driver =None
    Chrome_driver_path =os.path.join(os.path.dirname(__file__),"drivers"+os.sep+"chromedriver.exe")
    logger =Logger()

    def  __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance=super().__new__(cls)
        return cls._instance

    @classmethod
    def get_driver(cls,browers="chrome"):
        if  cls._driver is None:
            cls._driver =cls.create_driver(browers)
            cls.logger.info("创建"+browers+"浏览器")
        return  cls._driver

    @classmethod
    def create_driver(cls,browers):
        driver =None
        if browers.lower() =="chrome":
            driver = webdriver.Chrome(executable_path=cls.Chrome_driver_path)
        else:
            cls.logger.warn("暂时不支持其它浏览器")
        return driver

if __name__ == '__main__':
    print(DriverFactory.Chrome_driver_path)
    driver = DriverFactory.get_driver()
    driver.get("http://www.baidu.com")