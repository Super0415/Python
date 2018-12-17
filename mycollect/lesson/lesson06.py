#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2018/12/1

# 输出带符号的浮点数，并保留两位小数，并保留两位小数
# 将上面的问题使用两种格式化方法输出
# %:%d,%f,%s
print("%-+.2f" % -520.6666666)  # -520.67
print("%-+.2f" % 520.6666666)  # +520.67

# format
print("{:.2f}".format(520.6666666))
print("{:.2f}".format(-520.6666666))


# 赋值、浅拷贝、深拷贝
L = ["a", "b", "c", ["d", "e", ["f", "g"]]]

# 赋值
L1 = L
L[1] = "fei"
print(L)
print(L1)

L[3][1] = "fei"
print(L)
print(L1)

L[3][2][1] = "fei"
print(L)
print(L1)

# 浅拷贝
import copy
L = ["a", "b", "c", ["d", "e", ["f", "g"]]]
L2 = copy.copy(L)

L[1] = "fei"
print(L)
print(L2)

L[3][1] = "fei"
print(L)
print(L2)

L[3][2][1] = "fei"
print(L)
print(L2)

# 深拷贝
L = ["a", "b", "c", ["d", "e", ["f", "g"]]]
L3 = copy.deepcopy(L)

L[1] = "fei"
print(L)
print(L3)

L[3][1] = "fei"
print(L)
print(L3)

L[3][2][1] = "fei"
print(L)
print(L3)







