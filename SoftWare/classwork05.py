#!/usr/bin/env python
# encoding: utf-8
# file: classwork05.py
# author: Fengzc
# time: 2018/12/09 20:49

print("打印9*9乘法口诀表")
A = 9
B = 9
i = 0
j = 0
while j < B:
    j += 1
    i = 0
    while i < j:
        i += 1
        print(i, "*", j, "=", i*j, end="\t")
    print()


