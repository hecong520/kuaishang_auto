# -*- coding: UTF-8 -*-
'''
Created on 2020/3/3
@File  : zl_client.py
@author: ZL
@Desc  :
'''

import socket
import time


class ZlClient:

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5000
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            self.conn.connect((self.host, self.port))
            while True:
                self.conn.send(("来自客户端发送的数据 : " + str(time.time())).encode())
                data = self.conn.recv(1024).decode()
                print("来自服务端数据 :" + data + "|" + str(time.time()))
                time.sleep(0.1)
        except:
            print("服务器连接异常,尝试重新连接 (10s) ...")
            self.conn.close()
            time.sleep(10)  # 断开连接后,每10s重新连接一次
            ZlClient().run()

        finally:
            print("客户端已关闭 ...")


if __name__ == "__main__":
    emsc = ZlClient()
    emsc.run()
