# -*- coding=UTF-8
import os
import time
import serial
import yaml


class SerialSet:

    def ser_set(self, com):
        #  串口设置
        bamp = serial.Serial(com, 115200, timeout=10)
        return bamp

    def read_yml(self):
        # 文件是否存在
        if not os.path.isfile("./date/ser.yml"):
            raise FileNotFoundError("文件路径不存在， 请检查路劲是否正确： %s" % "./date/ser.yml")
        else:
            # open 方法打开直接读出来
            f = open("./date/ser.yml", 'r', encoding='utf-8')
            cfg = f.read()
            # 将其转化为字典形式
            d = yaml.load(cfg, Loader=yaml.FullLoader)
            # print("读取的测试文件数据： %s" % d)
            return d

    def script_write(self, order, com):
        #  串口指令操作
        if order == None:
            com.write("\n".encode())
        else:
            com.write("\n".encode())
            com.write(order.encode())
            com.write("\n".encode())
        time.sleep(3)
        return None

    def log_Read(self, order, com, expect, count):
        """串口读取"""
        # print(com)
        t = SerialSet().make_Txt()
        # 控制重启次数
        counts = count + 1
        for i in range(1, counts):
            for y in order:
                SerialSet().script_write(y, com)
            print(f"重启第 {i} 次")
            SerialSet().Date_txtpath(t, f"重启第 {i} 次" + "\n")
            while True:
                #  按行读取串口数据
                date = com.readline()
                strdate = str(date)
                SerialSet().Date_txtpath(t, strdate + "\n")
                for x in expect:
                    if x in strdate:
                        print(strdate)
                if strdate == "b''":
                    print("退出")
                    break
        return None


    def make_Txt(self):
        # 获取时间戳转换时间
        now = int(time.time())
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        # print(otherStyleTime)
        fname1 = otherStyleTime + ".txt"
        #  拼接log地址
        pathtxt = "./log" + "/" + fname1
        strpath_txt = pathtxt.replace(":", "-")
        t = open(strpath_txt, 'w')
        return t

    def Date_txtpath(self, t, date):
        #  数据输入
        t.write(date)
        return None


if __name__ == '__main__':
    input("请连接设备，并接通电源，按enter继续")
    d = SerialSet().read_yml()
    com1 = SerialSet().ser_set(d[0]["com"])
    SerialSet().log_Read(com=com1, order=d[1]["order"], expect=d[3]["expect"], count=d[2]["count"])
