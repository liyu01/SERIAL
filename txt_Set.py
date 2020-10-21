# -*- coding: utf-8 -*-
import time

fname = r".\log"


def GetNowTime():  # 获取当前时间并以年月日时间方式显示
    return time.strftime("%m%d%H%M%S", time.localtime(time.time()))


if __name__ == '__main__':
    now = int(time.time())  # 1533952277
    timeArray = time.localtime(now)
    print(timeArray)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
    fname1 = r"" + otherStyleTime + ".txt"  # 设置根据当前时间动态命名txt文件，注意r主要用于特殊符号，因此r后需要存在特殊符号
    pathtxt = "./log" + "/" + fname1
    strpath_txt = pathtxt.replace(":", "-")
    # print(type(strpath_txt))
    # print(pathtxt)
    # fname+=fname1
    # f = open("D:/Users/JCDN/Desktop/abc/test.txt", "r")
    # print(f.read())
    t = open(strpath_txt, 'w')
    t.write("你好11\n")
    t.close()
