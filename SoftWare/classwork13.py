#!/usr/bin/env python
# encoding: utf-8
# file: classwork13.py
# author: Fengzc
# time: 2018/12/17 22:40

print("1.写一个递归版本的斐波那契数列计算函数")
def Fun1(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    return Fun1(num-1) + Fun1(num-2)

print("请输入需要查看的数列数量：", end="\t")
Num = int(input())
Num = Num + 1
for i in range(1, Num):
    print(Fun1(i), end=" ")

print("\n请输入需要查看的数列序号：", end="\t")
Num = int(input())
print(Fun1(Num))


print("\n2.使用生成器来实现斐波那契数列计算函数")
def Fun2(m):
    global data3
    n = 2
    data1 = 1
    data2 = 1
    if m == 1 or m == 2:
        data3 = 1
    else:
        while n < m:
            data3 = data2 + data1
            data1 = data2
            data2 = data3
            n += 1
    yield data3

print("请输入需要查看的数列数量：", end="\t")
Num = int(input())
Num = Num + 1
for i in range(1, Num):
    print(next(Fun2(i)), end=" ")

print("\n请输入需要查看的数列序号：", end="\t")
Num = int(input())
f = Fun2(Num)
print(next(f))


