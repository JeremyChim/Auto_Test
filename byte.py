# -*- coding: utf-8 -*-
# @Time ： 2023/7/24 17:59
# @Auth ： JeremyChim
# @File ：byte.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

def ret_byte(a:list):
    a = "\n".join(a) + "\n"
    a = a.encode('utf-8')
    return a

if __name__ == '__main__':
    a = ['ls','exit']
    b = ['cat /oemdata/configs/7B120-1.cfg | grep ICCID','exit']
    c = ['cat /oemdata/configs/7B120-1.cfg | grep SN','exit']
    d = ['cat /oemdata/configs/7B120-1.cfg | grep ware','exit']
    e = ['export DBUS_SESSION_BUS_ADDRESS=`cat /tmp/.default-msgbus-session-address` ',
         'dbus-send --session --type=method_call --print-reply  --dest=com.yuantel.tbox.file    /com/yuantel/tbox/file  com.yuantel.tbox.file.cfg_data_set string:server string:ecall_auto_num string:01056162092',
         'exit']

    print(ret_byte(d))