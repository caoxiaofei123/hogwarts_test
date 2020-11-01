#!/usr/bin/python3
#autor cxf
#time  2020.10.31

"""
练习类：车
1.属性：品牌、速度、颜色
2.动作：加速
3.对象：汽车、货车、、、
"""

class car:
    # 构造方法定义
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    # 定义通用方法，输出个别字段值
    def accelerate(self):
        print(f"有个{self.color}的{self.brand}车，已经加速到{self.speed}")


if __name__ == "__main__":
    # 创建实例对象，传入对象值
    kdlk = car("凯迪拉克","黑的",110)
    hq = car("红旗","红的",120)
    kdlk.accelerate()
    hq.accelerate()