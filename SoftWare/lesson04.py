#!/usr/bin/env python
# encoding: utf-8
# file: lesson04.py
# author: Fengzc
# time: 2018/12/7 10:34

print("1.输出带符号的浮点数，并保留两位小数")
N = 11.1111111
print("%+-.2f" % N)
print("%+-.2f" % -N)

print("\n2.将上面的问题使用两种格式化方法输出")
print("2.1传统方法，使用“%”")
print("%+-.2f" % N)
print("%+-.2f" % -N)
print("2.2使用format")
print("{:+.2f}".format(N))
print("{:+.2f}".format(-N))



