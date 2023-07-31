# -*- coding: utf-8 -*-
# @Time ： 2023/7/25 16:18
# @Auth ： JeremyChim
# @File ：test.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from os import system
from len import ret_row
from read import ret_val
from list import ret_lst
from adb import ret_out_err
from if_ import ret_pass_fail
from xy import ret_coord
from style import save_style
from save import save_res
from time import time
from date import now
from time import sleep

cmd = 'copy case.xlsx report.xlsx'
system(cmd)

row = ret_row()
row -= 1

for i in range(row):
    try:
        ts1 = time()

        i += 2
        a = ret_val(i, 2)
        print(f'case: {a}')

        a = ret_val(i, 3)
        print(f'order: {a}')

        a = ret_lst(a)
        a, err = ret_out_err(a) # run...
        c = ret_coord(i, 10)
        save_res(c, a)
        save_style(c)

        t = ret_val(i, 8)
        if t:
            print(f'wait: {t}s')
            sleep(t)
            c = ret_coord(i, 8)
            save_res(c, t)
            save_style(c)

        b = ret_val(i, 4)
        print(f'if: {b}')
        a = ret_pass_fail(b, a)
        print(f'case result: {a}')
        c = ret_coord(i, 5)
        save_res(c, a)
        save_style(c)

        ts2 = time()

        ts = ts2 - ts1
        ts = '%.2f' % ts
        ts = float(ts)
        print(f'time: {ts}s')
        c = ret_coord(i, 6)
        save_res(c, ts)
        save_style(c)

        n = now()
        print(f'date: {n}')
        c = ret_coord(i, 7)
        save_res(c, n)
        save_style(c)

        t = ret_val(i, 9)
        if t:
            print(f'sleep: {t}s')
            sleep(t)
            c = ret_coord(i, 9)
            save_res(c, t)
            save_style(c)

    except:
        print(' !!!Σ(⊙▽⊙"a Error !!! '*5)

    print('\n')

print(' ヾ(≧∇≦ Finsh (*^▽^*) '*5)
