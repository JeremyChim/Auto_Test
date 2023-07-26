# -*- coding: utf-8 -*-
# @Time ： 2023/7/26 18:13
# @Auth ： JeremyChim
# @File ：sleep.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from time import sleep
from datetime import datetime

for i in range(999):
    sleep(0.1)
    n = datetime.now()
    print(n)