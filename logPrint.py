# -*- coding=UTF-8

import sys
import os


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


path = os.path.abspath(os.path.dirname(__file__))  # 获取当前py文件的父目录
type = sys.getfilesystemencoding()
sys.stdout = Logger('log/log.txt')  # 输出文件
# 以下print内容将会输出到a.txt中

if __name__ == '__main__':
    print(path)
    print(os.path.dirname(__file__))
    print('------------------')
    for i in range(5, 10):
        print("this is the %d times" % i)
