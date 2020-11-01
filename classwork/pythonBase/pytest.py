# -*- coding :UTF-8
# @Time     :2020/11/1 16:18
# @autor    :cxf
# @File     :pytest.py
"""
1.第三方库的安装
pip install pytest
pip install request
2.可以参考pypi方法库，进行查看具体的第三方库使用方法
https://pypi.org/search/?q=requests
"""

import requests

r = requests.get('http://www.baidu.com')
r.encoding = "utf-8"
print(r.text)
