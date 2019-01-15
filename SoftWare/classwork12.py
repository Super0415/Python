#!/usr/bin/env python
# encoding: utf-8
# file: classwork.py
# author: Fengzc
# time: 2018/12/26 18:45

print("1.自己构造一个报错的场景， 并模仿课堂进行一个报错分析")
print("（报错的类型，报错的原因，报错的代码，和报错的行）")
print(qw)



print("2.结合异常处理，确保打开文件后的正常关闭")
print("（如果我用w模式正常的打开了文件，然后write时候如果报错呢？ 那么我怎么正常关闭文件？）")

f = open("classwork11.txt","w",encoding="utf-8")
try:
    f.write(w,"12345")
    f.close()
except:
    print("123")
    f.close()



