#!/usr/bin/env python
# encoding: utf-8
"""
@author: Fengzc
@software: pycharm
@file: lesson03.py
@time: 2018/11/29 20:38
"""

# 集合：无序、
# 变量初始化
a = {1, 2, "a", 5}
print("集合a的类型：", type(a))

c = {}  # 空字典
print("集合c的类型：", type(c))


# 增
# add()
# updata()
S = {1, 2, "a", 5}
print("打印集合S：", S)
S.add("World")
print("打印增加了“World”的集合：", S)

S.update("hello")
print("使用updata“hello”：", S)    # 无序更新合集
S.update("hello")
print("使用updata“hello”：", S)    # 不重复更新，每次刷新，均不一样


# 删
# remove pop discard
# remove ：有该指定元素删除，无该指定元素报错，指定删除传入的元素
# pop：随机删除
# discard：有该指定元素删除，无继续运行，指定删除传入的元素
S.remove(5)
print("remove删除'5'集合元素：", S)
# S.remove(10)
# print("remove删除'10'集合元素：", S) # 删除内容没有，程序无法进行

S.pop()
print("pop()删除随机元素：", S)
"""
S.pop()
print("pop()删除随机元素：", S)
S.pop()
print("pop()删除随机元素：", S)
S.pop()
print("pop()删除随机元素：", S)
S.pop()
print("pop()删除随机元素：", S)
S.pop()
print("pop()删除随机元素：", S)
"""
S.discard("world")
print("discard()删除无指定：", S)
S.discard("World")
print("discard()删除有指定：", S)


S1 = {1, 2, 3, 4}
S2 = {5, 6}
S3 = {3, 4, 5, 6}
print("以此三个例子", S1, S2, S3)
# 查
# isdisjoint():判断两个集合是否有交集
print("判断S1中是否存在S2部分：", S1.isdisjoint(S2))  # 没有交集返回Ture ，有交集返回False
# issubset():

# 交集：
print("交集S1 & S2：", S1 & S2)
print("交集S1 & S3：", S1 & S3)

# 并集：
print("并集S1|S2：", S1 | S2)
print("并集S1|S2：", S1 | S3)

# 差集：
print("差集S1-S2：", S1 - S2)  # 主体为前一位
print("差集S1-S3：", S1 - S3)
print("差集S2-S3：", S2 - S1)

# 去重
S = {1, 2, 2, 4, 4, 5}
print("S     :", S)
print(type(S))
print("set(S):", set(S))

L = [1, 2, 3, 3, 4, 4]  # list 列表
print("L     :", L)
print(type(L))
print("set(L):", set(L))

T = (1, 1, 2, 2, 3, 3)  # tuple 元组
print("T     :", T)
print(type(T))
print("set(T):", set(T))

# 二、基本数据list tuple dict set 特点比较
# 1.列表list: 有序，可以修改，可以重复，[] 空列表
# 2.元组tuple: 有序，不可以修改，可以重复，() 空元组
# 3.字典dict: 无序，可以修改，键不能重复，值可以重复，{} 空字典
# 4.集合set: 无序，重写，不允许重复，set() 空集合

# 三、数据类型的补充
# 1.int
n = 12
print("内存地址：", id(n))    # 1444376384
n1 = 122
n2 = int(n1)
n3 = 122
print("内存地址：", id(n1))
print("内存地址：", id(n2))
print("内存地址：", id(n3))

# 2.str
# 特殊字符：\n 换行     \t Tab
print("as")
print("\n")
print("df")
# 转义： \   r
print("as\tdf")
print("as\\tdf")
print(r"as\tdf")

print("+ 连接两个字符串", "a" + "b")
print("重复出现", "a"*5)


name = "Fengzc"
T = ("we", 12, "ed", 34, 45)
L = [12, 23, 34]
# list：字符串、元组---》列表
L0 = list(name)
print("字符串转换为列表：", L0)
L0 = list(T)
print("元组转换为列表：", L0)

# tuple:字符串、列表---》元组
T = tuple(name)
print("字符串转换为元组：", T)
T = tuple(L)
print("列表转换为元组：", T)

T = (12, 23, [34, 45, {"K1": "V1"}])
print(T[2][2]["K1"])

# dict

# enunerate: 自动生成一列，默认从0开始自增1
L = [11, 22, 33, 44]
print(L[0])
D = dict(enumerate(L))
print(D)


print("算术运算符： + - * / % * //")
a = 10
b = 20
print("a = :", a)
print("b = :", b)
print("取和：a + b = :", a + b)
print("取差：a - b = :", a - b)
print("取积：a * b = :", a * b)
print("取除：a / b = :", a / b)
print("取余：a % b = :", a % b)
print("取整：a // b = :", a // b)
print("取幂：a ** b = :", a ** b)

print("逻辑运算符： and or not , 与或非")
c = -10
print("a = ", a, "\tb = ", b, "\tc = ", c,)
print("a and b:", a and b)  # 20
print("a or  b:", a or b)   # 10
print("not a:", not a)    # False

print("a and c:", a and c)  # False
print("c and a:", c and a)  # False
print("a or  c:", a or c)   # 10
print("not a:", not a)    # False
print("not b:", not b)    # False
print("not c:", not c)    # True








