# -*- coding: utf-8 -*-
# @Time ： 2023/7/25 14:32
# @Auth ： JeremyChim
# @File ：read.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import openpyxl as op

def ret_val(x:int, y:int):
    '''
    :param x: 单元格行数
    :param y: 单元格列数
    :return: 单元格的值
    '''
    wb = op.load_workbook('report.xlsx')
    ws = wb.worksheets[0]
    a = ws.cell(x, y).value
    return a

if __name__ == '__main__':
    from os import system
    cmd = 'copy case.xlsx report.xlsx'
    system(cmd)

    a = ret_val(1, 2)
    print(a.__class__, a)