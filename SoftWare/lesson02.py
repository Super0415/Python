# 一、列表list：有序、可变的
L = [0, 2, 3, 6, 32]
print(L)
print(L[0])
print(L[2])
print(L[1])
print(L[3])
print(L[4])

L1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(L1)
L1[1] = 'm'
print(L1)
print(L1[0])

# 删
print("pop(): 删除最后一个元素，并且该元素可赋值")
a = L1.pop()
print(a)
print(L1)
print("remove()")


# 循环
L = ['a', 'b', 'c', 'd']
a = 'a'
b = 'g'
print("循环显示")
for i in L:
    print(i)
print("判断某值是否在此数组中：")
print(a, a in L)
print(b, b in L)

# 二、元祖tuple：有序、不可变的
# 变量初始化
T = ()  # 空元祖

# 三、字典dict：由键值对构成的无序集合（key - value）
# 键（key）数据类型

# 字典 {}
# 变量初始化
a = {}
b = {
    1: 2,                    # 数字
    "K2": "V2",             #
    "K3": [1, 2, 3, 4],     #
    "K4": (1, 2, 3, 4),     #
    "K5": {                 #
        "name": "feng",
        "age": 18,

    },
    ("K6",): "V6"

}
print("a的数据类型为：", type(a))
print("b的数据类型为：", type(b))


# 长度
D = {
    "K1": "V1",
    "K2": "V2",
    "K3": "V3",
    "K4": "V4",
    "K5": "V5",
}
print(len(D))

# 键 - 值 - 键值对
print(D.keys())
print(D.values())
print(D.items())

# 查
# 第一种：通过 key 值去获取 value 的值
print(D.keys())

# 第二种：get
print(D.get("K3"))
print(D.get("K3", "false"))
print(D.get("K5"))
print(D.get("K6"))
print(D.get("K6", "false"))
print(D)

# 第三种：setdefault
print(D.setdefault("K3"))
print(D.setdefault("K6"))
print(D.setdefault("K6", "V6"))





