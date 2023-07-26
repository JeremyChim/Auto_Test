# -*- coding: utf-8 -*-
# @Time ： 2023/7/26 17:00
# @Auth ： JeremyChim
# @File ：time.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from time import time

def fun():
    print('fun is running...')
    for i in range(99999):
        i += 1
        print(f'fun time:{i}')
    print('fun is finsh.')

a = time()
fun()
b = time()

c = b - a
c = '%.2f' % c
c = float(c)
print(c.__class__, c)
print(f'运行时间：{c}秒')
