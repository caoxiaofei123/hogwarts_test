# -*- coding :UTF-8
# @Time     :2021/1/4 22:52
# @autor    :cxf
# @File     :main.py
from selenium.webdriver.common.by import By

from classwork.webAutoTest.pageobject.page.Register import Register
from classwork.webAutoTest.pageobject.page.base_page import BasePage

#继承基础类
class Main(BasePage):
    # 重写基础类中的URL值
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, "XXX").click()
        return Register(self.driver)

