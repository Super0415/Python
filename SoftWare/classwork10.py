#!/usr/bin/env python
# encoding: utf-8
# file: classwork10.py
# author: Fengzc
# time: 2018/12/22 17:26
from datetime import datetime
import io
# def run_time(func):
#     def interval_time(*args, **kwargs):
#         start_time = datetime.now()
#         print('程序开始时间：%s' % start_time)
#         func(*args, **kwargs)
#         end_time = datetime.now()
#         print('程序结束时间：%s' % end_time)
#         Period_time = end_time - start_time
#         print('程序总共执行时间为：%s' % Period_time)
#         return Period_time
#     return interval_time
#
# @run_time
# def WriteFile(File):
#     fileElem = open(File, 'w+', encoding='utf-8')
#     fileElem.write("TEST")
#     fileElem.close()
#
# @run_time
# def ReadFile(File):
#     fileElem = open(File, 'r+', encoding='utf-8')
#     s = fileElem.read()
#     print(s)
#     fileElem.close()

# print("自定义上下文管理器， 判断 IO 操作 和 文件操作 那个速度更快")
# FileName = "classwork10.txt"
# T0 = WriteFile(FileName)
# T1 = ReadFile(FileName)
# print("文件操作：“写”耗时{0}，读耗时{1}".format(T0, T1))
#

# with open(FileName, "a", encoding="utf-8")as f:
#     f.write("wohenhaoa")
#     f.write("jintian今天")
#
# with open(FileName, "r", encoding="utf-8")as f1:
#     print(f1.read())

class RunTime:
    def __enter__(self):  # 进入时自动调用
        self.start_time = datetime.now()
        print("进入时间：", self.start_time)
        return self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.now()
        print("退出时间：", self.end_time)
        print("运行时间：", self.end_time - self.start_time)
        return self.end_time

print("自定义上下文管理器， 判断 IO 操作 和 文件操作 那个速度更快")
with RunTime() as Test1:
    fileElem = open("classwork10.txt", 'w', encoding='utf-8')
    fileElem.write("hello world")
    fileElem.close()

with RunTime() as Test2:
    sio = io.StringIO()  # 创建一个对象，进行保存读取
    sio.write("hello world")
    print(sio.getvalue())
    sio.close()
Period_Time1 = Test1.now()-Test1
Period_Time2 = Test2.now()-Test2
if Period_Time1 > Period_Time2:
    print("IO操作比文件操作快！")
elif Period_Time1 == Period_Time2:
    print("IO操作与文件操作一样快！")
else:
    print("文件操作比IO操作快！")


