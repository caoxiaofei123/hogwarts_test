"""
第一个pytest文件,
1.安装 pip install pytest
2.规则：类型时test_XX.py  方法：test_xx()
3.运行pytest 即可运行
详细的运行日志 pytest -v

"""

# 普通方法，而非测试用例
import pytest


# 部分用例需要调用其他方法时，使用fixture定义
@pytest.fixture()
def login():
    print("login")
    return "haha"


class test_demo:

    def inc(x):
        return x + 1

    # test开头，可识别成测试用例
    # parametrize 定义用例入参
    @pytest.mark.parametrize('a,b', [
        (1, 2),
        (2, 3)])
    def test_answer(a, b):
        print(a)
        print(login)
        assert a == b


# pytest -k test_xx   即执行测试用例
# -v 打印执行详情
if __name__ == '__main__':
    pytest.main(['test_demo1.py'])
