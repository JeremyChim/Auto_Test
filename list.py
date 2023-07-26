# -*- coding: utf-8 -*-
# @Time ： 2023/7/25 15:15
# @Auth ： JeremyChim
# @File ：list.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

def ret_lst(a:str):
    a = a.split(',')
    return a

if __name__ == '__main__':
    a = "cat /oemdata/configs/7B120-1.cfg | grep ICCID,exit"
    a = ret_lst(a)
    print(a)