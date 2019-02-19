#!/usr/bin/env python
# encoding: utf-8
# file: WorkCount.py
# author: Fengzc
# time: 2019/1/4 9:1

def SF_OUM_TO_ADC():
    num = 0
    print("+++ 根据电阻值推算AD值 ++++")
    try:
        num = float(input("请输入电阻值:"))
    except:
        SF_OUM_TO_ADC()
    Snum = ((num * 4095) / (num + 300))
    print("推算AD值为: %f" % Snum)
    if num == 9999:
        return FunSys()
    else:
        SF_OUM_TO_ADC()

def SF_5V_TO_ADC():
    num = 0.0
    print("+++ 根据电压推算AD值（5V比较） ++++")
    try:
        num = float(input("请输入电压值:"))
    except:
        SF_5V_TO_ADC()
    Snum = ((num * 4095)* (2.0/3.0) / 3.3)
    print("推算AD值为: %f" % Snum)
    if num == 9999:
        return FunSys()
    else:
        SF_5V_TO_ADC()

def SF_TMP_TO_16U():
    num = 0.0
    print("+++ 根正负温度计算转换值 ++++")
    try:
        num = float(input("请输入温度:"))
    except:
        SF_TMP_TO_16U()
    Snum = ((num + 3276.8) * 10.0)
    print("推算温度转化值为: %f" % Snum)
    if num == 9999:
        return FunSys()
    else:
        SF_TMP_TO_16U()

def FunSys():
    function = 0
    print("请选择功能项：\n"
          "（0-根据电阻值推算AD值）\n"
          "（1-根正负温度计算转换值）\n"
          "（2-根据电压推算AD值（5V比较）)")
    try:
        function = int(input("功能项："))
    except:
        FunSys()

    if function == 0:
        SF_OUM_TO_ADC()
    elif function == 1:
        SF_TMP_TO_16U()
    elif function == 2:
        SF_5V_TO_ADC()
    elif function == 3:
        print("暂时未开发！！！")
    elif function == 4:
        print("暂时未开发！！！")
    elif function == 5:
        print("暂时未开发！！！")


FunSys()

