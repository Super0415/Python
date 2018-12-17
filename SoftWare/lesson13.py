#!/usr/bin/env python
# encoding: utf-8
# file: lesson13.py
# author: Fengzc
# time: 2018/12/10 21:03

# 多继承
class Owner:
    def eat(self):
        print("happy")


Own = Owner()
Own.eat()

# class Cat(Owner):
#     del Kun(self):

class Test:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        res = self.num + other.num
        return res

a = Test(22)
b = Test(11)
c = Test(44)
d = a + b
print(d)
print(b + c)


