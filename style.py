# -*- coding: utf-8 -*-
# @Time ： 2023/7/31 14:36
# @Auth ： JeremyChim
# @File ：style.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import openpyxl as op
from openpyxl.styles import Font,Alignment

def save_style(x:str):
    wb = op.load_workbook('report.xlsx')
    ws = wb.worksheets[0]

    f = Font(name=u'微软雅黑', size=8)
    a = Alignment(horizontal='center', vertical='center')
    c = ws[x]

    c.font = f
    c.alignment = a
    wb.save('report.xlsx')

if __name__ == '__main__':
    x = 'A1'
    save_style(x)