# -*- coding: utf-8 -*-
# @Time    : 2020-10-22 17:29
# @Author  : cxf
# @File    : random_demo.py

"""
作业题目：
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
---------------
实现方案：
1. 定义初始值字段 my_hp、my_power、enemy_hp、enemy_power，设置成随机值
2. 定义fight方法
    1） 设置计算公式：my_hp -= enemy_hp、enemy_hp -= my_hp
    2)  循环：双方血量都为0，平局；对方血量<=0，我方赢了；我方血量<=0,我方输了
    3)  优化：两方随机进行攻击动作
    4） 打印结果
3. 调用fight方法
"""
import random

# 定义fight方法
def fight(my_hp,enemy_hp,my_power,enemy_power) :
    # 打印攻击力数值
    print(f"我的攻击力是{my_power},我的血量是{my_hp}")
    print(f"敌人的攻击力是{enemy_power},敌人的血量是{enemy_hp}")

    # 定义比赛回合数
    roundNum = 1;
    # 循环，判断是否终结比赛
    while True:
        # 若随机数=0则我方出击，否则对方出击，回合数+1
        if random.randint(0,1) == 0:
            enemy_hp = enemy_hp - my_power
            print(f"当前回合：{roundNum},我方出击，我方攻击力是{my_power},敌方剩余血量是{my_hp}")
            roundNum = roundNum + 1
        else:
            my_hp = my_hp - enemy_power
            print(f"当前回合：{roundNum},敌方出击，敌方攻击力是{enemy_power},我方剩余血量是{enemy_hp}")
            roundNum = roundNum + 1

        # 判断谁的剩余血量<=0
        if my_hp <= 0:
            # 打印我方、敌方的剩余血量
            print(f"我方输了：我方剩余血量是{my_hp},敌人的剩余血量是{enemy_hp}")
            break
        elif enemy_hp <= 0:
            # 打印我方、敌方的剩余血量
            print(f"我方赢了：我方剩余血量是{my_hp},敌人的剩余血量是{enemy_hp}")
            break


if __name__ == "__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]

    # 定义初始值字段 my_hp、my_power、enemy_hp、enemy_power
    my_hp = random.choice(hp)
    enemy_hp = random.choice(hp)
    my_power = random.randint(190, 200)
    enemy_power = random.randint(190, 200)
    fight(my_hp, enemy_hp, my_power, enemy_power)