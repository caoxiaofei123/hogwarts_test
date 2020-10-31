#!/usr/bin/python3
#autor cxf
#time  2020.10.31

"""
练习类：花朵
1.属性：名字、颜色
2.动作：开花
3.对象：茉莉花、玫瑰花、、、
"""

class flower:
    # 构造方法定义
    def __init__(self,name,color):
        self.name = name
        self.color = color

    # 定义通用方法，输出个别字段值
    def blossom(self):
        print(f"花园里有{self.name},颜色是{self.color}")


if __name__ == "__main__":
    # 创建实例对象，传入对象值
    roe = flower("玫瑰","红的")
    lily = flower("百合","粉色的")
    roe.blossom()
    lily.blossom()








