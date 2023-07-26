# -*- coding: utf-8 -*-
# @Time ： 2023/7/25 15:59
# @Auth ： JeremyChim
# @File ：if.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

def ret_pass_fail(a:str, b:str):
    if a in b:
        res = 'pass'
    else:
        res = 'fail'
    return res

if __name__ == '__main__':
    a = '123456'
    b = 'vin:00001234560000'
    c = ret_pass_fail(a, b)
    print(c)
