# -*- coding: utf-8 -*-
# @Time ： 2023/7/26 17:34
# @Auth ： JeremyChim
# @File ：date.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from datetime import datetime

def now():
    a = datetime.now()
    a = str(a)
    a = a[:-7]
    return a

if __name__ == '__main__':
    a = now()
    print(a.__class__, a)