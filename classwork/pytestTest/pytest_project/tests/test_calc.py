# -*- coding :UTF-8
# @Time     :2020/11/29 22:38
# @autor    :cxf
# @File     :test_calc.py
import pytest

from classwork.pytestTest.pytest_project.core.calc import celc


class TestCalc():
    # setup_class 方法每个类仅执行一次，适用于初始化公共参数/方法
    def setup_class(self):
        self.calc = celc()

    # setup每个用例前执行一次
    def setup(self):
        pass

    @pytest.mark.parametrize('a,b,c', [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ])
    def test_div(self, a, b, c):
        # 异常处理 ，多种异常时可直接用Exception
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a, b) == c

    @pytest.mark.parametrize('a,b,c', [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 流程测试，多个接口相互传参时的测试场景
    def test_process(self):
        self.calc.mul(1, 2)
        self.calc.div(2, 3)
