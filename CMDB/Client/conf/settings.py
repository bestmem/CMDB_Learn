#!/usr/bin/env python
# coding:utf8
# date: 2020/1/2 11:02
# author: bestmem

import os

# 远端接收数据的服务器
Params = {
    "server": "192.168.168.194",
    "port": 8000,
    "url": 'assets/report',
    "request_timeout": 30,
}

# 日志文件
PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')
