#!/usr/bin/python3
#autor cxf
#time  2020.10.31

"""
练习类：笔：
1.属性：分类、样式、颜色、价格、厂家等
2.动作：写
3.对象：铅笔、圆珠笔、钢笔等
"""

class pen:
    # 定义类属性
    typeSort = "圆珠笔"
    style = "sample"
    color = "black"
    price = 1.5

    # 构造方法定义
    def __init__(self,typeSort,style,color,price):
        self.typeSort = typeSort
        self.color = color
        self.style = style
        self.price = price

    # 定义通用方法，输出个别字段值
    def write(self):
        print(f"现在正在写，使用的是{self.typeSort},字的颜色是{self.color}")


if __name__ == "__main__":
    # 创建实例对象，传入对象值
    pencil = pen("铅笔","sample","red",1.5)
    # 掉用方法
    pencil.write()








