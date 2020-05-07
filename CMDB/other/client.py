#!/usr/bin/env python
# coding:utf8
# date: 2020/3/31 22:39
# author: bestmem
import socket
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9004))
    re_data = input()
    s.send(re_data.encode("utf8"))
    data = s.recv(1024)
    print(data.decode("utf8"))
