#!/usr/bin/env python
# coding:utf8
# date: 2020/3/31 22:06
# author: bestmem
import socketserver, os
file_path = "C:/User/1.txt"
file_name = file_path.rsplit(os.sep, 1)
def take_hander(file_path, code="utf8"):



class My_Tcp_Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data=self.request.recv(1024)
        print("{}.received".format(self.data))
        self.request.send(self.data.upper())

if __name__ == "__main__":
    ip_port = ('localhost', '9001')
    server = socketserver.ThreadingTCPServer(('localhost', 9004), My_Tcp_Handler)
    server.serve_forever()
