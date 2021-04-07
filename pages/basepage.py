# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:43
# @Author  : LK
# @File    : basepage.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from util.common import *
from util.logger import Logger

class Basepage:
    """
    page基类,编写常用action
    """
    logger =Logger()
    def __init__(self,driver):
        self.driver =driver

    def find_element_and_wait(self,locator):
        """
         :param locator: 元组形式(By.ID,"id")
         :return: 返回element
         """
        element=None
        try:
            element=WebDriverWait(self.driver,30).until(lambda driver:self.driver.find_element(*locator))
        except TimeoutException as e:
            self.logger.erro(f"定位元素{locator}超时")
            self.get_screenShot()
        return element

    def find_elements_and_wait(self, locator):
        elements=None
        try:
            elements=WebDriverWait(self.driver,30).until(lambda driver:self.driver.find_elements(*locator))
        except TimeoutException as e:
            self.logger.erro(f"定位元素{locator}超时")
            self.get_screenShot()
        return elements

    def open_home(self, url):
        self.logger.info(f"打开{url}")
        self.driver.get(url)


    def click_element(self,locator):
        self.logger.info(f"点击{locator}元素")
        self.find_element_and_wait(locator).click()

    def send_text(self,locator,text):
        self.logger.info(f"在{locator}元素上输入{text}")
        element= self.find_element_and_wait(locator)
        element.clear()
        element.send_keys(text)

    def execute_js_click(self,locator):
        self.logger.info(f"使用JS点击{locator}")
        element=self.find_element_and_wait(locator)
        self.driver.execute_script("arguments[0].click();",element)

    def scroll_to_bottom(self,speed=1,index=100):
        js="return action=document.body.scrollHeight"
        height=0
        new_height=self.driver.execute_script(js)
        print(new_height)
        while height<new_height:
            for i in range(height,new_height, index):
                self.driver.execute_script('window.scrollTo(0,%d)' % i)
                time.sleep(speed)
            height = new_height
            time.sleep(2)
            new_height = self.driver.execute_script(js)
        self.driver.execute_script('window.scrollTo(0,0)')

    def is_exit(self,locator):
        flag=True
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException as e:
            flag=False
        return flag

    def delete_cookies(self):
        self.logger.info("清除cookies")
        self.driver.delete_all_cookies()

    def get_screenShot(self):
        self.logger.info("开始截图")
        save_screen_shot(self.driver)

    def switch_frame(self,locator):
        iframe=self.find_element_and_wait(locator)
        self.logger.info(f"进入{locator}")
        self.driver.switch_to.frame(iframe)

    def switch_windown(self):
        self.logger.info("切换页签")
        self.driver.switch_to.window(self.driver.window_handles[0])

    def switch_to_default(self):
        self.logger.info("退出iframe")
        self.driver.switch_to.default_content()

    def quit(self):
        self.logger.info("关闭浏览器")
        self.driver.quit()