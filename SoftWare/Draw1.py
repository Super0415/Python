#!/usr/bin/env python
# encoding: utf-8
# file: Work.py
# author: Fengzc
# time: 2019/1/15 9:53

# -*- coding: utf-8 -*-
"""
Lesson 17 : 利用递归算法，生成分形图形
"""
import turtle


# 引入函数，过程，将重复动作组合在一个函数中。
def sierpinski(turtle, length, level):
    if level == 0:
        triangle(turtle, length)
    else:
        # for i in range(3):重复三次画三角形，分别在三个顶点上画三角形
        curpos = t.position()  # 保留起始点坐标
        length *= 0.5
        sierpinski(turtle, length, level - 1)

        turtle.penup()
        turtle.forward(length)
        turtle.pendown()
        sierpinski(turtle, length, level - 1)

        turtle.penup()
        turtle.left(120)
        turtle.forward(length)
        turtle.right(120)
        turtle.pendown()
        sierpinski(turtle, length, level - 1)

        t.setposition(curpos[0], curpos[1])  # 回到起始点，方向也复原


def triangle(t, length):
    for i in range(3):
        t.forward(length)
        t.left(120)


scr = turtle.Screen()
t = turtle.Pen()  # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("turtle")  # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.

scr.bgcolor("black")  # (0.1,0.51,0.3)   # red,green,blue 取值在0和1之间。1代表255,
t.pensize(2)  # 改变线宽度
t.color("red")  # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)
t.speed(0)
t.penup()
t.setposition(-200, -100)
t.pendown()

sierpinski(t, 400, 4)
t.hideturtle()  # 隐藏乌龟图形
scr.exitonclick()