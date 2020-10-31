#!/usr/bin/python3
# -*- coding: utf-8 -*-
# autor cxf
# time  2020.10.31

"""
作业：
1.定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
    1.1 see_people方法，需要传入一个name参数，
    如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，
    如果传入“丁春秋”，打印“叛徒！我杀了你”
    1.2fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
    需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

2.定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
from classtest.homework2.TongLao import TongLao


class XuZhu(TongLao):

    # 定义构造方法
    def __init__(self,xzHp,xzPower):
        self.xzHp = xzHp
        self.xzPower = xzPower
        super().__init__(200,400)
    # 定义本身方法
    def read(self):
        print("罪过罪过")



if __name__ == "__main__":
    # 实例化对象
    xuzhu = XuZhu(200,500)
    # 调用父类方法
    xuzhu.seePeople("丁春秋")
    xuzhu.fightZms(1000,100)
    # 调用本身方法
    xuzhu.read()