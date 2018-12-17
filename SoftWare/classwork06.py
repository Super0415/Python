#!/usr/bin/env python
# encoding: utf-8
# file: classwork06.py
# author: Fengzc
# time: 2018/12/11 12:28

print("题目：对输入的数据进行排序，通过参数来决定正向排序还是反向排序")
def fun(*a, b):
    if b == 0:
        c = sorted(a)
        print(c)
    elif b == 1:
        d = sorted(a, reverse=True)
        print(d)
    else:
        print(b)
        print("shuruceshi")

Limt = 0
while Limt != 100:
    print("输入数据排序方式(0-正序；1-反序；100-退出)：", end="\t")
    InStr = input()
    if 0 < len(InStr) < 2 and InStr.isdigit():
        D = int(InStr)
        Limt = D
        if Limt == 100:
            print("成功退出！")
            break
        elif Limt > 2:
            print("无此排序方法！请重新输入...")
        else:
            print("输入数据(空格为间隔)：", end="\t")
            S = input()
            L1 = S.split(" ")
            fun(*L1, b=D)
    else:
        print("输入格式不正确，请重新输入...")

