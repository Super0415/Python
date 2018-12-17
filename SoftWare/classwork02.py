#!/usr/bin/env python
# encoding: utf-8
# file: classwork02.py
# author: Fengzc
# time: 2018/12/3 22:51

print("1.用多种方法往列表中插入值")
L = [12, 23, 34, 45, "asd", 56]
print("列表为：L = [12, 23, 34, 45, 'asd', 56]，x新增加")
print("1.1：append()增加1个元素")
L.append("new1")
print("L = ", L)
print("1.2：append()增加2个元素")
L1 = ["new2", "new3"]
L.extend(L1)
print("L = ", L)
print("1.3：insert()在X位置插入Y值")
L.insert(6, "new4")
print("L = ", L)

print("\n2.列表[‘hello’,‘python’,‘!’] 拼接并输出'hello python !'（两种）")
L2 = ['hello', 'python', '!']
L3 = []
print("2.1：利用字符串拼接")
S = L2[0] + ' ' + L2[1] + ' '+L2[2]
print(S)
print("2.2：利用join()将列表转换为字符串再拼接")
S1 = ''.join(L2)
S1 = S1[:5] + ' ' + S1[5:11] + ' ' + S1[11:]
print(S1)
print("2.3：转换为字符串拼接")
S1 = str(L2[0]) + ' ' + str(L2[1]) + ' ' + str(L2[2])
print(S1)

print("\n3.查找列表、元祖、字典中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。")
li = ["abc", " Adc", "A ox", "Ton", "rain "]
tu = ("abc", " ABc", "AoC", "Ton", "rain")
dic = {'k1': "abc", 'k2': ' Akc', "k3": "Aoc", "k4": "Ton", "k5": "rain"}
print(li)
print(tu)
print(dic)
print("3.1移除每个元素空格，并满足要求")
i = 0
Ln = []
D = {}
while i < len(li):
    D[i] = list(li[i])
    i += 1
i = 0
while i < len(li):
    j = 0
    Ln = D[i]
    while j < len(Ln):
        if Ln[j] == " ":
            del(Ln[j])
            continue
        j += 1
    i += 1
i = 0
while i < len(li):
    S3 = "".join(D[i])
    if (S3.startswith('a') or S3.startswith('A')) and (S3.endswith('c')):
        print("满足要求的元素为：", i, "-", S3, )
    D[i] = S3
    i += 1
print(D)

print("3.2移除每个元素空格，并满足要求")
i = 0
Ln = []
D = {}
while i < len(tu):
    D[i] = list(tu[i])
    i += 1
i = 0
while i < len(tu):
    j = 0
    Ln = D[i]
    while j < len(Ln):
        if Ln[j] == " ":
            del(Ln[j])
            continue
        j += 1
    i += 1
i = 0
while i < len(tu):
    S3 = "".join(D[i])
    if (S3.startswith('a') or S3.startswith('A')) and (S3.endswith('c')):
        print("满足要求的元素为：", i, "-", S3,)
    D[i] = S3
    i += 1
print(D)

print("3.3移除每个元素空格，并满足要求")
i = 0
Ln = []
D = {}
for k in dic.keys():
    D[i] = list(dic[k])
    i += 1
i = 0
for k in dic.keys():
    j = 0
    Ln = D[i]
    while j < len(Ln):
        if Ln[j] == " ":
            del(Ln[j])
            continue
        j += 1
    i += 1
i = 0
for k in dic.keys():
    S3 = "".join(D[i])
    if (S3.startswith('a') or S3.startswith('A')) and (S3.endswith('c')):
        print("满足要求的元素为：", i, "-", S3,)
    D[i] = S3
    i += 1
print(D)








