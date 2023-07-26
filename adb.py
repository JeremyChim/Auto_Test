# -*- coding: utf-8 -*-
# @Time ： 2023/7/24 16:42
# @Auth ： JeremyChim
# @File ：app.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from subprocess import *
from byte import ret_byte
from str import ret_str


def ret_out_err(a:list):
    pop = Popen('adb shell', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    a = ret_byte(a)
    out, err = pop.communicate(input=a, timeout=1000)
    out, err = ret_str(out), ret_str(err)
    return out, err

if __name__ == '__main__':
    a = ['ls','exit']
    b = ['cat /oemdata/configs/7B120-1.cfg | grep ICCID','exit']
    c = ['cat /oemdata/configs/7B120-1.cfg | grep SN','exit']
    d = ['cat /oemdata/configs/7B120-1.cfg | grep ware','exit']
    e = ['export DBUS_SESSION_BUS_ADDRESS=`cat /tmp/.default-msgbus-session-address` ',
         'dbus-send --session --type=method_call --print-reply  --dest=com.yuantel.tbox.file    /com/yuantel/tbox/file  com.yuantel.tbox.file.cfg_data_set string:server string:ecall_auto_num string:01056162092',
         'exit']

    out, err = ret_out_err(d)
    print(out, err)