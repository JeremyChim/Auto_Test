# -*- coding: utf-8 -*-
# @Time ： 2023/7/25 16:41
# @Auth ： JeremyChim
# @File ：xy.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import openpyxl as op

def ret_coord(x:int, y:int):
    wb = op.load_workbook('report.xlsx')
    ws = wb.worksheets[0]
    a = ws.cell(row=x, column=y)
    a = a.coordinate
    return a

if __name__ == '__main__':
    from os import system
    cmd = 'copy case.xlsx report.xlsx'
    system(cmd)

    a = ret_coord(1,1)
    print(a.__class__, a)