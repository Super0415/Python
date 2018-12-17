#!/usr/bin/env python
# encoding: utf-8
# file: lesson07.py
# author: Fengzc
# time: 2018/12/3 20:34

a = 5
if a < 3:
    print("a < 3")
else:
    print("a >= 3")

"""
if 条件：
    条件满足，需要做的事
else：
    条件不满足，需要做的事
"""
# 三目运算：if...else...简写
print("a < 3") if a < 3 else print("a <= 3")

# 条件满足，需要做的事情 if 条件 else 条件不满足，需要做的事情

# if...elif...else...
a = 4
if a < 3:
    print("a < 3")
elif 5 > a >= 3:
    print("5 > a >= 3")
else:
    print("a >= 5")

# 注意：python 里面是以缩进来实现代码块的（包含关系）
if a > 3:
    print(r" ****  1有缩进  ****")
    print(r" ****  2有缩进  ****")
print("无缩进")

# 拓展
# a = input("请输入你的名字：")
# print(a)

"""
a = int(input("请输入你的身高："))
print(a)
if a > 180:
    print("真高啊！")
elif 169 < a < 179:
    print("还行，找女朋友刚刚好！")
else:
    print("太矮，怎么找女票？？？")
"""


"""
# 打印一到十的所有数字
i = 1
while i < 11:
    print(i)
    i += 1
"""

# 循环取值
li = [1, 3, 5, 7, 9]
print("列表长度为：", len(li), " --- li[0] = ", li[0])
i = 0
# while i < len(li):
#     print("li[", i, "] = ", li[i])
#     i += 1
j = 0
while j < 5:        # 此处 5 改为 10 报警 “超出范围”
    if li[j] < 8:
        print("li[", j, "] = ", li[j], "----小于8")
    else:
        print("li[", j, "] = ", li[j], "----大于8")
    j += 1

# 循环 + 三目运算
lis = [1, 2, 3, 4, 5, 6, 7, ]
k = 0
while k < len(lis):
    print("@@@ 第", k, "个数据：", end="")
    print(lis[k], "大于4") if lis[k] > 4 else print(lis[k], "不大于4")
    k += 1

lis = [1, 2, 3, 4, 5, 6, 7, ]
# break：跳出整个循环
k = 0
print("==== START ====")
while k < len(lis):
    if lis[k] == 5:
        print("---遇5跳出循环---")
        break
    print("@@@ 第", k, "个数据：", end="")
    print(lis[k], "大于4") if lis[k] > 4 else print(lis[k], "不大于4")
    k += 1
print("====  END  ====")

# continue 跳出当前循环，进行下一次循环
k = 0
print("==== START ====")
while k < len(lis):
    if lis[k] == 5:
        print("---遇5跳过此次循环---")
        k += 1
        continue
    print("@@@ 第", k, "个数据：", end="")
    print(lis[k], "大于4") if lis[k] > 4 else print(lis[k], "不大于4")
    k += 1
print("====  END  ====")


# for - rang
m = 0
print("==== START ====")
for m in range(1, 5, 3):
    print(m, end="\t")
print("")
print("====  END  ====")
print("==== START ====")
for m in range(1, 5):
    print(m, end="\t")
print("====  END  ====")
print("==== START ====")
for m in range(1, 21):
    if m % 5 == 0:
        print("")
        # break
        continue
    print(m, end="\t")
print("====  END  ====")

print("==== START ====")
for m in range(1, 21, 4):
    if m % 5 == 0:
        print("")
        # break
        continue
    print(m, end="\t")
print("====  END  ====")





