#!/usr/bin/env python
# encoding: utf-8
# file: classwork07.py
# author: Fengzc
# time: 2018/12/13 18:28

print("定义一个函数，能够输入字典和元组。 函数返回一个字典和元组，字典的value值和元组的值交换")
tu = ('feifei', 18, 160)
di = {'name': 'sophia', 'age': 20, 'height': 165}
def fun(a, b):
    T1 = tuple(b.values())
    T2 = tuple(zip(b.keys(), a))
    return T1 + T2

T = fun(tu, di)
print(T)

