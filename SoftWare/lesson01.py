# 一.
temp = "my name is zhangchao"
print(temp)
print(temp.upper())

# 二、数字类型
# print type of value
print(type(temp))

# 1.整数类型
a1 = 10   # 十进制
print(a1, '的类型为：', type(a1))

b1 = 0b1111   # 二进制
print(b1, '的类型为：', type(b1))

c1 = 0o10   # 八进制
print(c1, '的数据类型为：', type(c1))

d1 = 0x10   # 16进制
print(d1, '的数据类型为：', type(d1))

# 2.浮点数
a2 = 3.0
print(a2, '的数据类型为：', type(a2))

import decimal   # 放在程序之前
e2 = "3.1234567890123456789012345678901234567890"
e2 = decimal.Decimal(e2)
print("无设置精度位数：", e2)
decimal.getcontext().prec = 10   # 精度位数
print("有设置精度位数：", e2)

# 3.复数

# 4.三种数据类型间的转换
a = "1"
b = 2
c = 3.14
print(a, type(a))
print(b, type(b))
# print(c.type(c))

d = int(a)
print(d, type(d))

# 转换为复数 complex
h = complex(b, c)
print(h)

a = 4 / 9
print(a)

# 三、布尔值：bool
# 简单举例
a = 1
b = 0
print(a)
print(bool(a))   # True
print(bool(b))   # False

print("bool 值为false值有哪些")
c = None
d = False
e = 0
f = 0.0
g = 0+0j
h = "None"
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))
print(bool(h))

temp = "super,Hello"
print("注意 capitalize ,首字母以及其余字母大小写：", temp)
print("注意 capitalize ,首字母以及其余字母大小写：", temp.capitalize())

# 字符串常用功能
# 索引
S = "Hello,Super"
print(S)
print(S[0], S[1], S[2], S[3], S[4], S[5], S[6], S[7], S[8])
print(S[-1], S[-2], S[-3], S[-4], S[-5], S[-6], S[-7], S[-8])

print("切片：")
print(S[0:6])
print(S[6:0:-1])
S = "hello"
print(S[::-1])  # olleh

# 移除

# 分割 split()
# S.split()
S = "   Hello,Super"
print(S.split(","))
print(S.split())








