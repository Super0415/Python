#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2018/11/27


# 数字类型：整数、浮点数、复数
# 初始数字类型
a = 5
b = 5.66
c = "6"
# d = 1 + 2j
print("a:", a)
print("a的类型为：", type(a))    # a的类型为： <class 'int'>
print("b:", b)
print("b的类型为：", type(b))    # b的类型为： <class 'float'>
print("c:", c)
print("c的类型为：", type(c))    # c的类型为： <class 'str'>
# print(d.real) # 实数
# print(d.imag) # 虚数

# 转换为整数
d = int(b)
e = int(c)
print("d:", d)
print("d的类型为：", type(d))    # d的类型为： <class 'int'>
print("e:", e)
print("e的类型为：", type(e))    # e的类型为： <class 'int'>

# 转换为浮点数
f = float(a)
g = float(c)
print("f:", f)
print("f的类型为：", type(f))    # f的类型为： <class 'float'>
print("g:", g)
print("g的类型为：", type(g))    # g的类型为： <class 'float'>

# 转换为复数
h = complex(a, b)
i = complex(b, a)
j = complex(c)
print("h:", h)  # h: (5+5.66j)
print("h的类型为：", type(h))    # h的类型为： <class 'complex'>
print("i:", i)  # i: (5.66+5j)
print("i的类型为：", type(i))    # i的类型为： <class 'complex'>
print("j:", j)  # j: (6+0j)
print("j的类型为：", type(j))    # j的类型为： <class 'complex'>


# 逆序
s = "hello,world!"
print(s[::-1])


# 切片得到年月日
s1 = "20181127"
year = s1[:4]
month = s1[4:6]
day = s1[6:]
print("年：", year)
print("月：", month)
print("日：", day)

S = "abcaodawf"
print(S.count("a"))
print(S.count("a", 3, 8))

