#!/usr/bin/env python
# encoding: utf-8
# file: classwork09.py
# author: Fengzc
# time: 2018/12/22 17:03

print("定义正方形类。 实现类实例的可调用，调用时打印边长； 同时，直接打印类实例时能够打印出实例的面积")
class RectClass:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

print("（定义矩形父类，通过继承形成正方形子类）")
class SquareClass(RectClass):
    def __init__(self, length):
        RectClass.__init__(self, length, length)

    def Length(self):
        print("正方形边长为：{}".format(self.length))

while 1:
    print("请输入正方形的边长（空格间隔,其他格式-退出）：", end="")
    str = input()
    L = list(str.split())
    if L[0].isdigit():
        A = SquareClass(int(L[0]))
        A.Length()
        print("正方形面积为：{}".format(A.area()))
    else:
        exit()
