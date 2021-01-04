# -*- coding :UTF-8
# @Time     :2021/1/4 23:25
# @autor    :cxf
# @File     :test_register.py
from classwork.webAutoTest.pageobject.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert "xxx" == self.main.goto_register().register()


