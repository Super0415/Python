#!/usr/bin/env python
# encoding: utf-8
# file: classwork11.py
# author: Fengzc
# time: 2018/12/22 19:42
from datetime import datetime
print("测试 type 和 isinstance 两个函数，哪个速度更加的快")
def run_time(func):
    def interval_time(*args, **kwargs):
        start_time = datetime.now()
        print('程序开始时间：%s' % start_time)
        func(*args, **kwargs)
        end_time = datetime.now()
        print('程序结束时间：%s' % end_time)
        Period_time = end_time - start_time
        print('程序总共执行时间为：%s' % Period_time)
        return Period_time
    return interval_time

@run_time
def fun1():
    print(type(1))

@run_time
def fun2():
    print(isinstance(1, int))

@run_time
def fun3(n):
    for i in range(n):
        type(1)

@run_time
def fun4(n):
    for i in range(n):
        isinstance(1, int)

def fun5(n):
    Sum = n
    Sum0 = 0
    Sum1 = 0
    Sum2 = 0
    while Sum > 0:
        T1 = fun1()
        T2 = fun2()
        print("++++++++++++++++++++++++++")
        print(type(T1))
        print("isinstance()耗时{0}，type()耗时{1}".format(T1, T2))
        if T1 > T2:
            print("isinstance()更快")
            Sum0 += 1
        elif T1 == T2:
            print("isinstance()和type()一样快")
            Sum1 += 1
        else:
            print("type()更快")
            Sum2 += 1
        Sum -= 1

    print("循环{1}次，其中{2}次isinstance()更快，{3}次isinstance()和type()一样快，{4}次type()更快，".format(0, num, Sum0, Sum1, Sum2))

print("请输入测试 type 和 isinstance 两个函数的次数：", end="")
num = int(input())
fun5(num)
print("++++++++++++++++++++++")
T3 = fun3(100000)  # type
T4 = fun4(100000)  # isinstance
if T3 > T4:
    print("isinstance()更快")
elif T3 == T4:
    print("isinstance()和type()一样快")
else:
    print("type()更快")
