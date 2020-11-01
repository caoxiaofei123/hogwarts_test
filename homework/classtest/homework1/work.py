#!/usr/bin/python3
#autor: cxf
#time:  2020.10.31

"""
练习类：工作
1.属性：所属公司、工号、职位、薪资
2.动作：上班、下班
3.对象：打工人

优化*：私有属性设置
"""

class work:

    # 定义私有变量
    def __init__(self):
        self.company = "中国银行"
        self.workNumber = "0001"
        self.position = "leader"
        self.salary = 20
        print("初始化")

    # 定义set、get方法
    def setCompany(self,company):
        self.company = company

    def getCompany(self):
        return self.company

    def setWorkNumber(self, workNumber):
        self.workNumber = workNumber

    def getWorkNumber(self):
        return self.workNumber

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    # 定义通用方法
    def goWork(self):
        print(f"打工人去上班了，今天要发工资了，有{self.getSalary()}票票")

    def offWork(self):
        print(f"打工人下班了，今天发工资了，带着{self.getSalary()}票票回家了")


if __name__ == "__main__":
    # 实例化对象，打工人
    worker = work()
    # 调用通用方法
    worker.goWork()
    # 通过set方法设置字段值
    worker.setSalary(25)
    worker.offWork()
