# -*- coding: utf-8 -*-
# @Time ： 2023/8/1 16:48
# @Auth ： JeremyChim
# @File ：can.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import zcanpro as z
import time

stopTask = False

def z_main():
    busID = init()
    sgn = [{"can_id": 0x10A,"is_canfd": 0,"canfd_brs": 0,"data": [0, 1, 2, 3, 4],"interval_ms": 500}]
    for i in range(100):
        send(busID, sgn)
        time.sleep(0.1)

def init():
    bus = z.get_buses()
    busID = bus[0]["busID"]
    devType = bus[0]["devType"]
    devIndex = bus[0]["devIndex"]
    chnIndex = bus[0]["chnIndex"]
    z.write_log("="*10 + "总线信息" + "="*10)
    z.write_log(f"总线ID: {str(busID)}")
    z.write_log(f"设备类型: {str(devType)}")
    z.write_log(f"设备索引号: {str(devIndex)}")
    z.write_log(f"通道索引号: {str(chnIndex)}")
    z.write_log("="*30)
    return busID

def send(busID, sgn):
    res = z.dev_auto_send_start(busID, sgn)
    if res == 1:
        z.write_log(f"成功：{sgn}")
    else:
        z.write_log(f"失败：{sgn}")
    return res

def z_notify(type, obj):
    zcanpro.write_log("Notify " + str(type) + " " + str(obj))
    if type == "stop":
        zcanpro.write_log("Stop...")
        global stopTask
        stopTask = True