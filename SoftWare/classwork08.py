#!/usr/bin/env python
# encoding: utf-8
# file: classwork08.py
# author: Fengzc
# time: 2018/12/22 16:40

print("定义个矩形类，有长和宽两个实例属性， 还有一个计算面积的方法")
class RectClass:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
while 1:
    print("请输入矩形的长、宽（空格间隔,其他格式-退出）：")
    str = input()
    L = list(str.split())
    print(type(L[0]))
    if L[0].isdigit() == True and L[1].isdigit() == True:
        A = RectClass(int(L[0]), int(L[1]))
        print(A.area())
    else:
        exit()

