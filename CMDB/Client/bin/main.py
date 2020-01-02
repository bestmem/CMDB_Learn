#!/usr/bin/env python
# coding:utf8
# date: 2020/1/2 10:07
# author: bestmem
import os
import sys
from core import handler
BASE_DIR = os.path.dirname(os.getcwd())
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    handler.ArgHandler(sys.argv)

