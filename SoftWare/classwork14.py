#!/usr/bin/env python
# encoding: utf-8
# file: classwork14.py
# author: Fengzc
# time: 2019/12/26 21:15

# print("1.已知小明所在的城市打车10元起步（3公里），3公里以后到20公里，每公里3元。 20公里以后每公里需另加0.6元的远途费，设计一个程序，输入公里数，自动计算出车费。 ", "\n"
#       "**********考查知识点：if-elif-else**********")
# def SumFare(kilometre):
#     if kilometre <= 3:
#         return 10
#     elif kilometre <= 20:
#         return (10 + 3*(kilometre-3))
#     else:
#         return 61 + 0.6 * (kilometre-20)
#
# sign = 1
# while sign == 1:
#     print("请输入行驶公里数(0-退出)：", end="")
#     try:
#         kilometre = int(input())
#         print("车费：{0}".format(SumFare(kilometre)))
#         if kilometre == 0:
#             sign = 0
#     except:
#         print("输入格式不正确，请重新输入！！！")
#         print(type(sign))


# print("2.设计一个小程序，让用户输入一个整数X，判断0 —— X 这个数之间有多少个数是5的倍数？ 并把所有5的倍数用保存到一个列表里面，打印出来。", "\n",
#       "**********考查知识点：列表，运算符，条件判断，循环。输入输出**********")
# def decorate(Func):
#     def Fun0(*args, **kwargs):
#         try:
#             num = Func(*args, **kwargs)
#             return num
#         except:
#             print("格式输入错误！")
#             return False
#     return Fun0
#
# def Save_n_Multiple(m, n):
#     L = []
#     for i in range(1, m):
#         if i%n == 0:
#             L.append(i)
#     return L
#
# @decorate
# def Fun1():
#     print("请输入一个整数X：", end="")
#     num = int(input())
#     return num
#
# X = Fun1()
# if X is not False:
#     L = Save_n_Multiple(X, 5)
#     print("0 —— {0} 这个数之间有 {1} 个数是5的倍数,打印如下：".format(X,len(L)),"",  L)


# print("3.设计一个程序，通过输入文件名，会自动创建文件，创建后提示需要写入的内容， 可以在里面写入文件内容，然后自动保存退出。", "\n",
#       "**********考查知识点：文件操作**********")
#
# print("请输入文件名：", end="")
# FileName = input()
# try:
#     f = open(FileName, "a", encoding="utf-8")
#     print("文件打开成功，请输入写入内容：")
# except:
#     print("文件打开失败，请重新操作！")
# content = input()
# f.write(content)
# f.write("\n")
# f.close()


# print("4.面向对象：定义一个Person类，这个类有名字，年纪，职业，并且有至少三个方法。 这个类的实例之间，可以通过 + 进行互动。 并且实例可以直接被调用，调用的时候会去使用类的其中一个方法。", "\n",
#       "**********考查知识点：类的定义与使用，魔法方法**********")
# class Person:
#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
#
#     def getname(self):
#         return self.name
#
#     def getage(self):
#         return self.age
#
#     def getposotion(self):
#         return self.position
#
#     def __add__(self, other):
#         return (self.age + self.age)
#
#     def __call__(self, *args, **kwargs):
#         return self.getname()
#
# xiaoming = Person("xiaoming", 23, "职业经理")
# xiaowang = Person("xiaowang", 22, "职业经理")
# print(xiaoming.getage())
# print(xiaoming.age)
# print(xiaoming + xiaowang)
# print(xiaowang())


# print("5.设计一个拥有注册和登录功能的小程序，要求：注册完成后提示注册的账号和密码， 登录成功后，提示欢迎登录，账号或者密码不正确时，返回相应提示。","\n",
#       "**********考查知识点：函数的定义，参数和变量的使用。**********")
#
# def saveinfo(name, password):
#     with open("UserInfo.txt", "a", encoding="utf-8") as filename:
#         filename.write(name)
#         filename.write(" ")
#         filename.write(password)
#         filename.write("\n")
#
# def checkname(name):
#     truefalse = False
#     with open("UserInfo.txt", "r", encoding="utf-8") as file:
#         line = file.readline()
#         while line:
#             if line.split(" ")[0] == name:
#                 truefalse = True
#             line = file.readline()
#     return truefalse
#
# def checkpassword(password):
#     truefalse = False
#     with open("UserInfo.txt", "r", encoding="utf-8") as file:
#         line = file.readline()
#         password_file = line.split(" ")[1].split("\n")[0]
#         if password_file == password:
#             print("密码匹配成功！")
#             truefalse = True
#         line = file.readline()
#     return truefalse
#
# print("#####################################################\n"
#       "####                                             ####\n"
#       "####               欢迎进入小程序                ####\n"
#       "#####################################################")
# name = ""
# password = ""
# function = 0
# sign = 1
# while sign:
#     print("请输入用户名：", end="")
#     name = input()
#     print("请输入密码：", end="")
#     password = input()
#     sign_fu = 1
#     while sign_fu:
#         print("请输入功能项（0-登陆；1-注册）：", end="")
#         fun_num = 0
#         try:
#             function = int(input())
#             if function == 0:
#                 print("denglu")
#             elif function == 1:
#                 print("zhuce")
#             else:
#                 print("无此功能！")
#             sign = 0
#             sign_fu = 0
#         except:
#             print("输入格式不正确！")
#             fun_num += 1
#             if fun_num == 4:
#                 sign_fu = 0
# print("用户:", name)
# print("密码:", password)
# print("功能:", function)
#
# truefalse = False
# if function == 0:    # 登陆
#     truefalse = checkname(name)
#     if truefalse is True:
#         truefalse = checkpassword(password)
#         print(truefalse)
#         if truefalse is True:
#             print("登陆成功")
#         else:
#             print("密码输入错误")
#     else:
#         print("无此用户")
# elif function == 1:
#     truefalse = checkname(name)
#     if truefalse is False:
#         saveinfo(name, password)
#     else:
#         print("用户名重复，注册失败！")
#

print("5.设计一个拥有注册和登录功能的小程序，要求：注册完成后提示注册的账号和密码， 登录成功后，提示欢迎登录，账号或者密码不正确时，返回相应提示。","\n",
      "**********考查知识点：函数的定义，参数和变量的使用。**********")

class User_system():
    def __init__(self):
        self.name = None
        self.password = None
        self.option = None

    def HeadContent(self):
        print("#####################################################\n"
              "####                                             ####\n"
              "####               欢迎进入小程序                ####\n"
              "#####################################################")

    def sys_option(self):
        option = input("请输入服务项(0-注册；1-登陆；其他-待开发)：")
        try:
            if int(option) == 0:
                self.option = option
            elif int(option) == 1:
                self.option = option
            else:
                print("待开发，请重新选择...")
                self.sys_option()
        except:
            print("待开发，请重新选择...")
            self.sys_option()

    def login(self):
        name = input("请输入登陆用户名：")
        self.name = name
        if self.checkname(self.name) is True:
            print("存在此用户名！")
            password = input("请输入登陆密码：")
            self.password = password
            if self.checkpassword(self.password) is True:
                print("登陆成功！")
            else:
                print("密码错误！")
                self.login()
        else:
            print("不存在此用户！")
            self.login()

    def register(self):
        name = input("请输入注册用户名：")
        self.name = name
        if self.checkname(self.name) is True:
            print("用户名重复！")
            self.register()
        else:
            password = input("请输入注册密码：")
            if self.saveinfo() is True:
                print("注册成功！！")
                      # "注册用户名为：{}，注册密码为：{}".format(self.name, self.password))
            else:
                print("保存失败！")

    def saveinfo(self):
        try:
            with open("UserInfo.txt", "a", encoding="utf-8") as filename:
                info = [self.name,self.password]
                filename.writelines(info)

                filename.write(self.name)
                filename.flush()
                filename.write(" ")
                filename.flush()
                filename.write(self.password)
                filename.flush()
                filename.write("\n")
                filename.flush()
                return True
        except:
            return False

    def checkname(self, name):
        truefalse = False
        with open("UserInfo.txt", "r", encoding="utf-8") as file:
            line = file.readline()
            while line:
                if line.split(" ")[0] == name:
                    truefalse = True
                line = file.readline()
        return truefalse

    def checkpassword(self, password):
        truefalse = False
        with open("UserInfo.txt", "r", encoding="utf-8") as file:
            line = file.readline()
            password_file = line.split(" ")[1].split("\n")[0]
            if password_file == password:
                truefalse = True
            line = file.readline()
        return truefalse

    def system_state(self):
        self.HeadContent()
        self.sys_option()
        if int(self.option) == 0:
            self.register()
        elif int(self.option) == 1:
            self.login()
        else:
            print("无此功能项")


Sys = User_system()
Sys.system_state()



