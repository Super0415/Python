#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2018/12/5

# 知识点回顾
# 列表排序
# sorted:内置函数,将列表进行排序
# reversed:内置函数,将列表反向
# L = [1, 5, 2, 6, 3, 4]
# print(sorted(L))
# print(list(reversed(L)))
# print(sorted(L, reverse=True))

# sort():没有返回值，修改自身
# 类名.方法名（）
# L.sort()
# print(L)
# L.sort(reverse=True)
# print(L)

# 定义个函数，可以对输入的数据进行排序，通过参数来决定是正向排序还是反向排序
# 1.定义一个函数：def func（）：
# 2.参数：x，y
# 3.函数体：排序

# s=1或者不传入s的值时，表示正向
# s=2表示反向


# def func(*args, s=1):
#     li = list(args)
#     if s == 1:
#         # a = sorted(args)    # 正向排序
#         li.sort()
#         print(li)
#
#     elif s == 2:
#         b = sorted(args, reverse=True)  # 反向排序
#         print(b)
#     else:
#         print("输入错误！！！！")


# L1 = [1, 5, 2, 6, 3, 4]
# L2 = ["a", "f", "b", "e", "g"]
# func([1, 5, 2, 6, 3, 4])
# func(*L1, s=2)
# func(*L2, s=1)

# s = input("请输入你的名字：")
# print(s)

# print("{}-{}-{}".format("我", "是", "花田错"))
# a = 10
# b = 5
# if a < 5 and b < 8:
#     print("ok")
# 参数：形参（必须参数：必须传入值的参数）、实参（位置参数）、默认参数、关键字参数、动态参数（*args、**kwargs）


# def f(x, y, z, *args, **kwargs):
#     print(args)
#     print(kwargs)


# f(1, 2, 3, 4, z=5, a=6)
# L = [1, 2]
# L.append(5)
# print(L)
# #
# range(5)    # -->[0,1,2,3,4]
# #
# range(1, 5)  # -->[1,2,3,4]
# #
# range(1, 5, 2)  # -->[1,3]

#
# u = "123456"
# p = "789456"
# u_i = input("请输入用户名：")
# p_i = input("请输入密码：")
# if u == u_i and p == p_i:
#     print("登录成功")


def func(x):
    print(x)
    return x


a = func(5)
print(a)



