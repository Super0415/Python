a = 1
b = 1.2
c = 1+2j
d = "My Name"
e = bool(1)
print(a, "的数据类型为：", type(a))
print(b, "的数据类型为：", type(b))
print(c, "的数据类型为：", type(c))
print(d, "的数据类型为：", type(d))
print(e, "的数据类型为：", type(e))
print("定义讲过的每种数字类型并实现相互之间的转换")
print("***********  1.1.转换数据类型-整型")
print(b, "转换为整型：", int(b))
# print(c, "转换为整型：", int(c))    # 复数不支持转换整型
# print(d, "转换为整型：", int(d))    # 字符串不支持转换整型
print(e, "转换为整型：", int(e))
print("***********  1.2.转换数据类型-浮点型")
print(a, "转换为浮点型：", float(a))
# print(c, "转换为浮点型：", float(c)) # 复数不支持转换浮点型
# print(d, "转换为浮点型：", float(d)) # 字符串不支持转换浮点型
print(e, "转换为浮点型：", float(e))
print("***********  1.3.转换数据类型-复数型")
print(a, " 转换为复数", complex(a))
print(b, " 转换为复数", complex(b))
# print(d, " 转换为复数", complex(d))    # 字符串不支持转换浮点型
print(e, " 转换为复数", complex(e))
print(a, "和", b, "组合转换为复数", c)
print("***********  1.4.转换数据类型-布尔型")
print(a, "转换为布尔型：", bool(a))
print(b, "转换为布尔型：", bool(b))
print(c, "转换为布尔型：", bool(c))
print(d, "转换为布尔型：", bool(d))
print("2.自定义一个字符串（eg：a = “hello,world!”），用切片的方式进行逆序")
Test = "hello,world!"
print(Test)
print(Test[0:12:2])
print(Test[:])
# print(Test[0:12:-1])  # -1 此处不仅输出反序，前两位输入也相反
print(Test[-1:-13:-1])
print(Test[::-1])
print("3.有一个时间形式(eg: 20180929),要求从这个格式中得到年、月、日")
Time = "20180929"
print("时间形式为：", Time)
print("年：", Time[0:4])
print("月：", Time[4:6])
print("日：", Time[6:8])


