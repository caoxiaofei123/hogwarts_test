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
import random


class TongLao:

    # 定义构造方法
    def __init__(self, hp, power):
        self.hp = hp;
        self.power = power;

    # 定义get、set方法
    def setHp(self, hp):
        self.hp = hp

    def getHp(self):
        return self.hp

    def setPower(self, power):
        self.power = power

    def getPower(self):
        return self.power

    def seePeople(self,name):
        if name == "WYZ":
            print("师弟！！！！")
        if name == "李秋水":
            print("师弟是我的！")
        if name == "丁春秋":
            print("叛徒！我杀了你")

    def fightZms(self,enemy_power,enemy_hp):
        self.hp *= 10
        self.power /= 2

        # 随机进行PK
        if random.randint(0, 1) == 0:
            enemy_hp -= self.hp
        else:
            self.hp -= enemy_power

        # 判断谁的剩余血量<=0
        if self.hp < enemy_hp:
            # 打印我方、敌方的剩余血量
            print(f"我方输了：我方剩余血量是{self.hp},敌人的剩余血量是{enemy_hp}")
        elif self.hp > enemy_hp :
            # 打印我方、敌方的剩余血量
            print(f"我方赢了：我方剩余血量是{self.hp},敌人的剩余血量是{enemy_hp}")
        else:
            # 打印我方、敌方的剩余血量
            print(f"平手：我方剩余血量是{self.hp},敌人的剩余血量是{enemy_hp}")

if __name__ == "__main__":
    # 实例化对象
    tonglao = TongLao(1000,200)
    # 调用通用方法
    tonglao.seePeople("丁春秋")
    tonglao.fightZms(999,199)








