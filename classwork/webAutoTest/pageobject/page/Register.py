# -*- coding :UTF-8
# @Time     :2021/1/4 23:06
# @autor    :cxf
# @File     :Register.py
from selenium.webdriver.common.by import By

from classwork.webAutoTest.pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "xxx").send_keys("hello")
        self.find(By.Id, "yyy").send_keys("world")