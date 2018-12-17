#!/usr/bin/env python
# encoding: utf-8
# file: classwork02.py
# author: Fengzc
# time: 2018/11/29 22:55

# 第一题：
print("第一题：找出两个列表中相同的元素")
L1 = [1, 2, 3, "we", "you", 6]
L2 = [3, "you", 5, 6, 7, 8]
print("列表1：", L1)
print("列表2：", L2)
S = set(L1) & set(L2)
L = list(S)
print("列表1和列表2的重复部分：\n", L)

# 第二题：
print("\n第二题：新建一个字典，用3种方法往字典里面插入值； 用 4 种方法取出values，用2种方法取出key")
print("2.1新建字典：")
D = {}
L = [1, 2, 3]
print("空字典：", D)
print("有键值，无初值的字典：", D.fromkeys(L))
print("有键值，赋初值的字典：", D.fromkeys(L, 'V1'))
print("2.2用3种方法往字典里面插入值：")
D.setdefault(4, 'v4')
print("D字典： ", D)
D.update({5: "V5", "K6": "V6"})
print("D字典： ", D)
D["K6"] = "V6-1"
print("D字典： ", D)
D1 = D.copy()
print("D1字典：", D1)

print("2.3用4种方法取出字典的values：")
L = list(D.values())
print(L)
print(D.get(4))
print(D["K6"])
T = list(D.items())
print(T[1][0])
print("2.4用2种方法取出key：")
L = list(D.keys())
print(L)
T = list(D.items())
print(T[0][0])

# 第三题：
print("\n第三题：定义我们学过的每种数据类型， 并且注明，哪些是可变，哪些是不可变的")
print("1.列表list: 有序，可以修改，可以重复，[] 空列表")
print("2.元组tuple: 有序，不可以修改，可以重复，() 空元组")
print("3.字典dict: 无序，可以修改，键不能重复，值可以重复，{} 空字典")
print("4.集合set: 无序，重写，不允许重复，set() 空集合")





