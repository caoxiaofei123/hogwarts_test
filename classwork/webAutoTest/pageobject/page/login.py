# -*- coding :UTF-8
# @Time     :2021/1/4 23:22
# @autor    :cxf
# @File     :login.py
from selenium.webdriver.common.by import By

from classwork.webAutoTest.pageobject.page.Register import Register
from classwork.webAutoTest.pageobject.page.base_page import BasePage


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR, "xxx").click()
        return Register(self._driver)