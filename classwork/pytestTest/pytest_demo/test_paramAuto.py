# -*- coding :UTF-8
# @Time     :2020/11/29 20:57
# @autor    :cxf
# @File     :test_paramAuto.py

import pytest
class TestParamAuto:

    @pytest.mark.parametrize("a,b",[(10,20),(11,20),(13,20)])
    def test_paramAuto(self ,a ,b):
        print(a + b)
