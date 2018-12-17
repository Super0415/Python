#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2018/11/27

# 字符串里字符是不支持通过索引修改
S = "hello,TZ"
print(S[2:3])
print(S[-5:-6:-1])
print(S[::-2])
print(S[-1])
# S[0] = "e"
# print(S[0])

# 一、列表:list
# 变量初始化，
L = []  # 空列表
L1 = ["a", "b", "cd"]   # 字符串列表项
L2 = [1, "a", "cd"]     # 数字列表项
L3 = [1, "a", "bd", ["c", "d"]]     # 列表列表项

print("L的类型是：", type(L))
print("L1的类型是：", type(L1))
print("L2的类型是：", type(L2))
print("L3的类型是：", type(L3))

# 列表常用方法：增删改查、循环、包含、长度
# 长度
L = ["a", "b", "c"]
print(len(L))

# 增
# append():追加
# extend(iter):批量追加
L.append("d")
print(L)    # ['a', 'b', 'c', 'd']

L2 = [1, 2, 3]
L.extend(L2)
print(L)    # ['a', 'b', 'c', 'd', 1, 2, 3]

# 查+改（索引）
print(L[2])
L[2] = "w"
print(L[2])

# 删
# pop()：删除最后一个元素，并且该元素可赋值
# remove():移除左边起第一个指定元素
# del()：删除指定索引元素
print(L)    # ['a', 'b', 'w', 'd', 1, 2, 3]
a = L.pop()
print(L)    # ['a', 'b', 'w', 'd', 1, 2]
print(a)    # 3

L.append("w")   # ['a', 'b', 'w', 'd', 1, 2, 'w']
print(L)
L.remove("w")
print(L)    # ['a', 'b', 'd', 1, 2, 'w']

del(L[3])
print(L)    # ['a', 'b', 'd', 2, 'w']

# 循环
L = ["a", "b", "c"]

for i in L:     # 循环遍历，第一次循环打印的L[0]，第二次循环打印L[1],第三次循环打印L[2]
    print(i)

# 包含（in）：判断列表里是否有这个元素
L = ["a", "b", "c"]
a = "a"
b = "w"

print(a in L)   # True
print(b in L)   # False

# 二、元祖tuple：有序，不可变的
# 变量初始化
T = ()  # 空元祖
T1 = ("a", "b", "cd")   # 字符串
T2 = (1, "a", "bc")     # 数字
T3 = (1, "bc", ["a", "b"])  # 列表
T4 = (1, "bc", ["a", "b"], ("a", "b"))  # 元祖

# 注意：单元素元祖时("hello",)
f = ("hello")
g = ("hello",)
print("f的类型是：", type(f))    # f的类型是： <class 'str'>
print("g的类型是：", type(g))    # g的类型是： <class 'tuple'>

# 常用功能
# 长度
T = ("a", "b", "c")
print(len(T))   # 3
# 索引(查）
print(T[1])
# 切片
print(T[:2])
print(T[:-1])
print(T[-3:-1])

# 循环
for j in T:
    print(j)

# 包含
a = "a"
b = "d"
print(a in T)
print(b in T)

# 三、字典dict：由键值对构成的无序集合（key——value）
# 键（key）数据类型一般为数字或者字符串，必须是唯一不重复的
# 值（value）可以是任意数据类型

# 字典{}
# 变量初始化
a = {}
b = {
    1: 2,   # key:数字；value:数字
    "k2": "v2",  # key:字符串；value：字符串
    "k3": [1, 2, 3],  # key:字符串；value：列表
    "k4": (1, 2, 3),    # key:字符串；value：元祖
    "k5": {             # key:字符串；value：字典
        "name": "fei",
        "age": 18
    },
    ("k6",): "v6"       # key:元祖
}
print("a的数据类型是：", type(a))  # a的数据类型是： <class 'dict'>
print("b的数据类型是：", type(b))

# 字典常用功能：增删改查、长度
# 长度
D = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3"
}
print(len(D))

# 键、值、键值对
print(D.keys())     # dict_keys(['k1', 'k2', 'k3'])
print(D.values())   # dict_values(['v1', 'v2', 'v3'])
print(D.items())    # dict_items([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])

# 查:
# 第一种:通过key值去获取value值
print(D["k2"])  # v2
# print(D["k4"])  # 报错

# 第二种方法：get
print(D.get("k3"))  # v3
print(D.get("k4"))  # None
print(D.get("k4", "false"))  # false

# 第三种方法：setdefault()
print(D.setdefault("k3"))  # v3
print(D.setdefault("k4"))  # None
print(D)    # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': None}
print(D.setdefault("k5", "v5"))  # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': None, 'k5': 'v5'}
print(D)

# 增+改
# 第一种，同上setdefault（），有则获取，无则增
# 第二种，通过索引，有则改，无则增
D["k4"] = 'v4'
print(D)    # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5'}
D["k6"] = "v6"
print(D)    # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5', 'k6': 'v6'}

# 删
# pop（）:获取并在字典中移除指定key值项
# popitem():获取并在字典中移除最后一项
# clear（）：
a = D.pop("k2")
print(D)    # {'k1': 'v1', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5', 'k6': 'v6'}
print(a)    # v2

b = D.popitem()
print(D)    # {'k1': 'v1', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5'}
print(b)    # ('k6', 'v6')

D.clear()
print(D)    # {}

# 循环
D = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3"
}

# D.items():键值对
for k, v in D.items():
    print(k, ":", v)

# D.keys():键 dict_keys(['k1', 'k2', 'k3'])
for k in D.keys():
    print(k)

# D.values():值
for v in D.values():
    print(v)

L = ["a", "b", "c"]
for i in L:
    print(i)






