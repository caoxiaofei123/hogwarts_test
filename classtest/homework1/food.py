#!/usr/bin/python3
#autor cxf
#time  2020.10.31

"""
练习类：食物
1.属性：名字、味道
2.动作：吃
3.对象：火锅、冰淇凌、、、
"""

class food:

    # 构造方法定义
    def __init__(self,name,taste):
        self.name = name
        self.taste = taste

    # 定义通用方法，输出个别字段值
    def eat(self):
        print(f"现在正在吃{self.name},味道{self.taste}")


if __name__ == "__main__":
    # 创建实例对象，传入对象值
    chafingDish = food("火锅","辣辣的")
    chafingDish.eat()
    icecream = food("冰淇凌","凉凉、甜甜的")
    icecream.eat();








