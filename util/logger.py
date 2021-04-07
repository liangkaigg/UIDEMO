# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 16:37
# @Author  : LK
# @File    : logger.py
import logging
from logging import handlers
import os
from util.common import get_date
#项目路径
pro_path =os.path.dirname(os.path.dirname(__file__))

class Logger:
    _instanse=None
    logger=None
    log_path =os.path.join((os.path.join(pro_path,"log")),(get_date()+".log"))

    def __new__(cls, *args, **kwargs):
        if not cls._instanse:
            cls._instanse =super().__new__(cls,*args,**kwargs)
        return cls._instanse

    def __init__(self):
        if  self.logger is None:
            self.logger =self.creat_logger()

    def creat_logger(self):
        formater = logging.Formatter(
            '[%(asctime)s] [%(levelname)s]: %(message)s'
        )
        logger =logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)
        fileHandle = handlers.TimedRotatingFileHandler(
            self.log_path,when="h",interval=24,backupCount=1,encoding="utf8")
        consoleHandle = logging.StreamHandler()
        fileHandle.setFormatter(formater)
        consoleHandle.setFormatter(formater)
        fileHandle.setLevel(logging.INFO)
        consoleHandle.setLevel(logging.DEBUG)
        logger.addHandler(fileHandle)
        logger.addHandler(consoleHandle)
        return logger


    def info(self,msg):
        self.logger.info(msg)

    def debug(self,msg):
        self.logger.debug(msg)

    def warn(self,msg):
        self.logger.warning(msg)

    def erro(self,msg):
        self.logger.error(msg)


if __name__ == '__main__':
    print(pro_path)
    log =Logger()
    log.warn("hahah")