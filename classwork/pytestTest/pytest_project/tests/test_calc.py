# -*- coding :UTF-8
# @Time     :2020/11/29 22:38
# @autor    :cxf
# @File     :test_calc.py
import pytest

from classwork.pytestTest.pytest_project.core.Calc import Celc


class TestCalc():
    # setup_class 方法每个类仅执行一次，适用于初始化公共参数/方法
    def setup_class(self):
        self.calc = Celc()

    # setup每个用例前执行一次
    def setup(self):
        pass

    @pytest.mark.parametrize('a, b, c', [
        [2, 1, 2],
        [1, 2, 0.5],
        [0.2, 2, 0.1],
        [-2, -1, -2],
        [2, 0, 0],
        [0, 2, 0],
        [2, '', 0],
        [2, "String", 0],
        [2, 'a', 0],
        [2, None, 0]
    ])
    def test_div(self, a, b, c):
        try:
            assert self.calc.div(a, b) == c
        except ZeroDivisionError as e:
            print(e)

    @pytest.mark.parametrize('a, b, c', [
        [2, 3, 6],
        [-2, 3, -6],
        [-3, -2, 6],
        [2, 0, 0],
        [0, 2, 0],
        [2, '', 0],
        [2, "String", 0],
        [0.2, 0.3, 0.06],
        [-3, -2, 6],
        [2, None, 0]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c
#
# # 流程测试，多个接口相互传参时的测试场景
# def test_process(self):
#     self.calc.mul(1, 2)
#     self.calc.div(2, 3)
