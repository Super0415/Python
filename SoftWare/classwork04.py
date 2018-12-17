#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2018/11/29


# 集合：无序、不允许重复.set
# 变量初始化
a = {1, 2, "a", 5}
print(type(a))  # <class 'set'>
b = set()
print(type(b))  # <class 'set'> 空集合
c = {}  # 空字典
print(type(c))

# 常用功能：增删查，去重，交集，并集，差集
# 增
# add()
# update():把要传入的元素拆分传入集合
S = {1, 2, "a", 5}
S.add("卢卢卢")
print(S)    # {1, 2, 5, 'a', '卢卢卢'}

S.update("hello")
print(S)

# 删除：remove,pop,discard
# remove:有则删，无报错，指定删除你传入的元素
# pop():随机删除
# discard():有则删，无不做任何操作，指定删除你传入的元素
print(S)    # {1, 2, 5, 'o', 'h', '卢卢卢', 'e', 'l', 'a'}
S.remove(5)
print(S)
# S.remove("fei")
# print(S)

S.pop()
print("1", S)

S.discard("e")
print(S)
S.discard("fei")
print(S)

print("2")

# 交集：你有我也有，我们两共有的部分
S1 = {1, 2, 3, 4}
S2 = {3, 4}
print(S1 & S2)  # {3, 4}

# 并集：
print(S1 | S2)  # {1, 2, 3, 4}

# 差集：- 所有属于前一个集合，不属于后一个集合的项组成的新集合
S1 = {1, 2, 3, 4}
S2 = {3, 4, 8, 9, 10}
print(S1-S2)    # {1, 2}
print(S2-S1)    # {8, 9, 10}

# 去重
s = {1, 2, 2, 3, 4, 5}
print(s)
L = [1, 2, 2, 3, 4, 5]
T = (1, 2, 2, 3, 4, 5)
S1 = set(L)
print(list(S1))
S2 = set(T)
print(tuple(S2))
print(T)

# 查：isdisjoint()/issubset()/issuperset()
# isdisjoint():判断s1、s2集合是否无交集，有False；无True
S1 = {1, 2, 3, 4}
S2 = {3, 4}
print(S1 & S2)
print(S1.isdisjoint(S2))    # False

# issubset()：是子集吗？
print(S1.issubset(S2))  # False
print(S2.issubset(S1))  # True

# issuperset()：是父集吗？
print(S1.issuperset(S2))    # True
print(S2.issuperset(S1))    # False

# 二、基本数据list、tuple、dict、set特点比较
# 1.列表list：有序，可以修改，可以重复，[]空列表
# 2.元组tuple：有序，不可以修改，可以重复,()空元祖
# 3.字典dict：无序，可以修改，键不能重复，值可以重复,{}空字典
# 4.集合set：无序，不允许重复，重写,set()空集合

# 三、数据类型的补充
# 1.int:-5~~257
n = 12
print(id(n))
n1 = 122
n2 = int(122)
n3 = 122
print(id(n1))
print(id(n2))
print(id(n3))

# 2.str
# 特殊字符：\n:换行；\t:tab；" "
# 转义
# print("a")
# print("\n")
# print("b")
print("ru\\nds")
print("a" + "b")
print("a"*5)

# list：字符串、元祖--->列表
# 转换
name = "飞飞"
L = list(name)
print(L)    # ['飞', '飞']

T = (11, 22, 33)
L1 = list(T)
print(L1)

# tuple:字符串、列表--->元组
T = tuple(name)
print(T)

L = [11, 22, 33]
T1 = tuple(L)
print(T1)

T2 = (11, 22, ["fei", {"k1": "v1"}])
print(T2[2][1]["k1"])

# dict:
D = {"k1": "v1"}
D1 = dict(k1=123, k2=456)
print(D1)   # {'k1': 123, 'k2': 456}

L = [11, 22, 33]
print(L[0])
D2 = dict(enumerate(L))
print(D2)   # {0: 11, 1: 22, 2: 33}

# enumerate:自动生成一列，默认从0开始自增1

# 集合
L = [11, 22, 33]
T = (11, 22, 33)
St = "112233"

S1 = set(L)
print(S1)   # {33, 11, 22}

S2 = set(T)
print(S2)

S3 = set(St)
print(S3)   # {'2', '1', '3'}

# 算术运算符：+，-，*，/，%，**，//
a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)    # 取余，返回的除法的余数
print(a // b)   # 取整除，返回的商的整数部分
print(a ** b)   # 幂，10的20次方，100000000000000000000

# 比较运算符：==，!=，>，<，>=，<=
print(a == b)   # a等于b吗？
print(a != b)   # a不等于b吗？
print(a > b)    # a大于b吗？
print(a < b)    # a小于b吗？
print(a >= b)   # a大于等于b吗？
print(a <= b)   # a小于等于b吗？

# 赋值运算符：=，+=，-=，*=，/=，%=， **=，//=
c = a + b
print(c)
c += a  # ===>c = c + a
print(c)
c -= a  # ===>c = c - a
c *= a  # ===>c = c * a
c /= a  # ===>c = c / a
c %= a  # ===>c = c % a
c //= a  # ===>c = c // a
c **= a  # ===>c = c ** a
# 逻辑运算符：and，or，not,与或非
print(a and b)  # 如果a为false，返回a值，a为true，返回b的值
print(a or b)   # 如果a为true，返回a的值，a为false，返回b的值
print(not a)    # False

# 成员运算符：in，not in
L = [1, 2, 3, 4]
a = 2
b = 5
print(a in L)   # True
print(b in L)   # False

print(a not in L)   # False
print(b not in L)   # True

a = 5
print(a)
a = 10
print(a)



