#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2018/12/6

# filter():过滤
# li = [3, 20, 4, 6, 5, 9]
#
#
# def f1(x):
#     return x > 5
#
#
# print(list(filter(f1, li)))  # [20, 6, 9]

# 匿名函数
# lambda函数
# 不含参
# def f1():
#     return 123
f1 = lambda: 123
print(f1())

# 含参
# def f2(a, b):
#     return a + b
f2 = lambda a, b: a + b

print(f2(11, 22))

# 函数名 = lambda 参数： 表达式

li = [3, 20, 4, 6, 5, 9]
f1 = lambda x: x > 5
print(list(filter(f1, li)))    # [20, 6, 9]

#


# def f1(a, b):
#     result = a + b
#     return result
# 匿名函数想要自执行，函数名（）
f1 = lambda a, b: a + b

num = f1(11, 22)
print(num)

# 把lambda函数当做参数传入，这样可以实现不同方法


def f2(a, b, func):
    result = func(a, b)
    return result


# num = f2(11, 22, lambda x, y: x + y)
num = f2(11, 22, lambda x, y: x - y)
print(num)

# 实现函数的输入
# func = input("请输入一个匿名函数：")
# func = eval(func)
# num = f2(11, 22, func)
# print(num)
# 实现输入函数的循环执行
# while True:
#     flag = input("你还要继续吗？输入yes继续，否则终止：")
#     if flag == "yes":
#         func = input("请输入一个匿名函数：")
#         func = eval(func)
#         num = f2(11, 22, func)
#         print(num)
#     else:
#         print("结束运行")
#         break

# 函数作用域：变量的作用范围
# num = 100   # 全局变量----全局作用域
#
#
# def f():
#     num = 200   # 局部变量，只在函数内生效，函数外无法拿到---局部作用域
#     print(num)
#
#
# f()
# print(num)
# 1.用的是函数内部定义的变量
# 2.注释函数内部变量后，使用的是函数外定义的变量

# global：在函数内部定义全局变量
# num = 100   # 全局变量----全局作用域


# def f():
#     # num = 200   # 局部变量，只在函数内生效，函数外无法拿到---局部作用域
#     global num
#     num = 200
#     print(num)
#
#
# f()
# print(num)
#
# num = 100
# num = 200
# print(num)

# nonlocal


# def f1():
#     num = 66
#
#
#     def f2():
#         nonlocal num
#         num += 1
#         return num
#     return f2()
#
#
# num = f1()
# print(num)


# 总结：
"""
a.函数内部定义的变量是局部变量，其作用域为局部作用域，函数外无法调用
b.函数外定义的变量是全局变量，其作用域为全局作用域，如果你想要在函数内修改全局变量，需要加 “global 变量名”
"""

# 闭包
# 函数嵌套


# def f1():
#     print("f1外层函数")
#
#     def f2():
#         print("f2内层函数")
#     return f2
#
#
# a = f1()
# a()

# f1函数内又定义了一个f2函数，我们调用f1函数，f1函数内部又调用了f2函数，这就叫函数的嵌套

# 函数名即变量
# f1 = lambda x, y: x + y

#


def f1():
    print('f1外层函数')


a = f1
a()
b = a
b()
# 函数名===》变量明
# 函数名（）===》函数执行


def f1():
    print("f1外层函数")

    def f2():
        return 5
    return f2


a = f1()    # a===>f2
print("a执行结果：", a())

# 闭包：函数嵌套时，外层函数返回内层函数的函数名，这种情况就叫闭包

# 带参数情况


def f1(num1):
    print(num1)

    def f2(num2):
        res = num1 + num2
        print(res)

    return f2


a = f1(66)
a(88)

# 我们应该知道
'''
1.函数内的变量函数外部访问不了
2.闭包是概念，不是某种函数类型，就是一种特殊的函数调用
3.闭包可以得到外层函数的局部变量，是函数内部和外部沟通的桥梁
'''

# 装饰器了解：
# 装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数


def outer(func):
    def inner():
        print("在原有功能前增加新功能")
        r = func()
        print("在原有功能后增加新功能")
        return r
    return inner()


# 表示：1.执行outer函数，并将下方的函数名作为参数赋值给outer函数；2.将outer函数的返回值重新赋值给下方的函数
@outer
def f1():
    print("原功能模块")


@outer
def f2():
    print("f2")


# 。。。。
@outer
def fn():
    print("fn")

# 不带参数的单层装饰器。

# tu = ('feifei', 18, 160)
# di = {'name': 'sophia', 'age': 20, 'height': 165}
#
#
# def f():
#     pass


# tu = ('sophia', 20, 165)
# di = {'name': 'feifei', 'age': 18, 'height': 160}

