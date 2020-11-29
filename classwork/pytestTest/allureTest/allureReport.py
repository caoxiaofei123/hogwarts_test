"""
allur是一个轻量级的测试报告，可插入图片、视频等
1. 安装插件
pip install allure-pytest

2.运行脚本
pytest allureReport.py --alluredir=./allureTest/1

3.生成报告
allure serve ./allureTest/1
"""

import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')