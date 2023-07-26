# -*- coding: utf-8 -*-
# @Time ： 2023/7/24 17:14
# @Auth ： JeremyChim
# @File ：str.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

def ret_str(a:bytes):
    a = a.decode('utf-8')
    a = a.replace('\r','')
    return a

if __name__ == '__main__':
    a = b'ls\r\r\nexit\r\r\n/ # ls\r\r\nWEBSERVER       etc             oemapp          run             tmp\r\r\nbin             firmware        oemappbak       sbin            usr\r\r\nboot            home            oemappbakromfs  sdcard          var\r\r\nbuild.prop      lib             oemappromfs     share\r\r\ncache           linuxrc         oemdata         sys\r\r\ndata            media           oemlog          system\r\r\ndev             mnt             proc            target\r\r\n/ # exit\r\r\n'
    b = b'cat /oemdata/configs/7B120-1.cfg | grep ICCID\r\r\nexit\r\r\n/ # cat /oemdata/configs/7B120-1.cfg | grep ICCID\r\r\n    ICCID="89860920740036750510";\r\r\n/ # exit\r\r\n'
    c = b'cat /oemdata/configs/7B120-1.cfg | grep SN\r\r\nexit\r\r\n/ # cat /oemdata/configs/7B120-1.cfg | grep SN\r\r\n    TBOXSN="C52XBDLM11190020";\r\r\n/ # exit\r\r\n'
    d = b'cat /oemdata/configs/7B120-1.cfg | grep ware\r\r\nexit\r\r\n/ # cat /oemdata/configs/7B120-1.cfg | grep ware\r\r\n      tbox_software = "1.09";\r\r\n      tbox_hardware = "1.00";\r\r\n      mcu_software = "220815V1.0";\r\r\n      um220_software="R3.6.0.0Build7723";\r\r\n      ec20_firmware = "EC20CEFARGR07A01M4G_OCPU_AMT";\r\r\n/ # exit\r\r\n'
    e = b'export DBUS_SESSION_BUS_ADDRESS=`cat /tmp/.default-msgbus-session-address` \r\r\ndbus-send --session --type=method_call --print-reply  --dest=com.yuantel.tbox.file    /com/yuantel/tbox/file  com.yuantel.tbox.file.cfg_data_set string:server string:ecall_auto_num string:01056162092\r\r\nexit\r\r\n/ # export DBUS_SESSION_BUS_ADDRESS=`cat /tmp/.default-msgbus-session-address` \r\r\n/ # dbus-send --session --type=method_call --print-reply  --dest=com.yuantel.tbo\r\r\r\nx.file    /com/yuantel/tbox/file  com.yuantel.tbox.file.cfg_data_set string:serv\r\r\r\ner string:ecall_auto_num string:01056162092\r\r\nmethod return sender=:1.0 -> dest=:1.9 reply_serial=2\r\r\n/ # exit\r\r\n'

    print(ret_str(d))
