# -*- coding: utf-8 -*-
# @Time ： 2023/7/25 15:38
# @Auth ： JeremyChim
# @File ：write.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import openpyxl as op

def save_res(x:str, t:str):
    wb = op.load_workbook('case.xlsx')
    ws = wb.worksheets[0]
    ws[x] = t
    wb.save('case.xlsx')

if __name__ == '__main__':
    x = 'E2'
    t = 'fail'
    save_res(x, t)


