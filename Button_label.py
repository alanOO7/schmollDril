#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8
import os
from Tkinter import *
import tkMessageBox as tkm
from settings import *


share_user = 'b3driller'
share_password = 'B3dr1325'


# share_file_host='\\\\192.168.1.24'
# share_file_path='\\\\192.168.1.24\\Git\\test_share_file.txt'
# target_file_path='d:\\test777

# 复制文件
def copy_share_file(share_file_host, share_file_path, target_file_path):
    permission_cmd ='''if [ ! -d "./cim/" ];then
                            mkdir cim
                        else
                            echo "cim文件夹已经存在"
                        fi
                        mount -t cifs //10.201.20.1/cim/b3/product/drill ./cim -o username=b3driller,password=B3dr1325
                        '''
    permission_result = os.popen(permission_cmd)
    print permission_result
    # permission_cmd = 'net use %s %s /user:%s' % (share_file_host, share_file_path, share_password)
    # print(permission_cmd)
    # permission_result = os.popen(permission_cmd)
    # print(permission_result.read())
    # copy_cmd = 'xcopy /y %s %s' % (share_file_path, target_file_path)
    # print(copy_cmd)
    # copy_result = os.popen(copy_cmd)
    # print(copy_result)


# 设置只能输入数字
def validateNum(content):
    try:
        if content == "":
            return True
        else:
            f = float(content)
        return True
    except ValueError:
        return False


# 主界面组件函数
def mainBL(wind):
    # 注册事件
    validateNumcmd = wind.register(validateNum)
    # 创建X标签与单行文本
    label_x = Label(wind, text="涨缩系数X:", anchor="center", bg="white")
    label_x.place(x=20, y=20, width=80, height=25, anchor="nw")
    varX = StringVar()

    global text_x
    text_x = Entry(wind, textvariable=varX, validate="key", validatecommand=(validateNumcmd, "%P"))
    text_x.place(x=100, y=20, width=120)

    # 创建Y标签与单行文本
    label_y = Label(wind, text="涨缩系数Y:", anchor="center", bg="white")
    label_y.place(x=280, y=20, width=80, height=25, anchor="nw")
    varY = StringVar()
    global text_y
    text_y = Entry(wind, textvariable=varY, validate="key", validatecommand=(validateNumcmd, "%P"))
    text_y.place(x=360, y=20, width=120)

    # 创建QR单行文本
    varQR = StringVar()
    global label_QR
    label_QR = Label(wind, text="请扫描二维码:", anchor="center", bg="white")
    label_QR.place(x=20, y=50, width=80, height=25, anchor="nw")
    text_QR = Entry(wind, textvariable=varQR)
    text_QR.place(x=100, y=50, width=380)

    # 显示内容
    varPJ = StringVar()
    label_PJ = Label(wind, textvariable=varPJ, anchor="center", wraplength=400)
    label_PJ.place(x=20, y=80, width=400, height=50, anchor="nw")

    # 创建submit按钮
    button_submit = Button(wind, text="确认", anchor="center", activebackground="red", bg="white",
                           relief="flat")
    button_submit.place(x=100, y=140, width=60)

    # 获取文件
    button_registry = Button(wind, text="获取文件", anchor="center", activebackground="red", bg="white",
                             relief="flat", command=lambda: getFiles(wind, varX.get(), varY.get(), varQR.get(), varPJ))
    button_registry.place(x=230, y=140, width=60)

    # 取消按钮,清除文本框输入内容
    button_cancel = Button(wind, text="清空", anchor="center", activebackground="red", bg="white",
                           relief="flat", command=lambda: (text_x.delete(0, END), text_y.delete(0, END),
                                                           text_QR.delete(0, END), label_QR.set("")))
    button_cancel.place(x=350, y=140, width=60)

    # 销毁主界面控件
    def redraw():
        label_x.destroy()
        text_x.destroy()
        label_y.destroy()
        text_y.destroy()
        button_submit.destroy()
        button_registry.destroy()
        button_cancel.destroy()


# 解析文件名
def getFilesName(X, Y, varPJ13, varPJ):
    logger.info('13位码:%s' % varPJ13)
    pjLayer = varPJ13[11:13]
    pjver = varPJ13[3:10]
    print os.name+"   aaaaa"
    if varPJ13[0] == 'Q' or varPJ13[0] == "H":
        varName1 = "S"
        varPath = "\\cim\\B3\\Sample\\drill\\"
        varPJ.set(varPJ.get() + "样本，")
    else:
        varName1 = "P"
        varPJ.set(varPJ.get() + "生产板，")
        # X,Y
        if X != "" and Y != "" and X != "0" and Y != "0":
            varXY = "D" + pjLayer + "_X+" + str(float(X) / 10000) + "%Y+" + str(float(Y) / 10000) + "%"
            varPath = "\\cim\\B3\\Product\\drill\\TCF\\" + varPJ13[3:7] + "\\" + varXY + "\\"
        else:
            varPath = "\\cim\\B3\\Product\\drill\\tool\\" + varPJ13[3:7] + "\\"
    varPJ.set(varPJ.get() + " 路径：" + varPath)
    logger.info('地址:%s' % varPath)
    # 后缀判断
    if pjLayer == "00":
        varDrlName2 = ".DRL"
        varDtlName2 = ".DTL"
    else:
        varDrlName2 = ".D" + pjLayer
        varDtlName2 = ".T" + pjLayer

    drlName = varPath + varName1 + pjver + varDrlName2
    dtlName = varPath + varName1 + pjver + varDtlName2
    logger.info('文件地址名称：DRL:%s，DTL:%s' % (drlName, dtlName))
    return dtlName, drlName


# 获取文件
def getFiles(wind, varX, varY, varQR, varPJ):
    try:
        if varX != "" or varY != "":
            text_x.config(background="White")
            text_y.config(background="White")

        else:
            text_x.config(background="Red")
            text_y.config(background="Red")
            return
        print text_x.get()+" text_xtext_xtext_x"
        logger.info('X:%s,Y:%s,QR:%s' % (varX, varY, varQR))
        varPJ13 = varQR[varQR.find('"P":"') + 5:varQR.find('","Q"')]
        varPJ.set("PJ:" + varPJ13 + " x:" + varX + ", y:" + varY + ", ")
        varFiles = getFilesName(varX, varY, varPJ13, varPJ)  # 解析获取文件地址名称

        for varFile in varFiles:
            copy_share_file("\\10.201.20.1\\",varFile,"D:\\")
            print varFile

    except Exception as e:
        tkm.showerror('showerror', "名字解析失败", parent=wind)
        logger.error("error%s" % e.message)


# 创建主窗口对象，并定义大小（固定）和位置，添加窗口icon
wind = Tk()
title = "自动获取文件"
wind.title(title)
wind.geometry("500x240+400+240")

# 调用主界面控件函数
mainBL(wind)

# 主循环
wind.mainloop()
