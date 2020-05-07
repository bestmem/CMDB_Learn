#!/usr/bin/env python
# coding:utf8
# date: 2020/3/19 15:22
# author: bestmem
class MyListIterator(object):       #迭代器对象
    def __init__(self, data):
        self.data = data
        self.now = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.now < self.data:
            self.now += 1
            return self.now - 1
        raise StopIteration

class MyList():   #可迭代对象
    def __init__(self, num):
        self.data = num
    def __iter__(self):
        return MyListIterator(self.data)

l = MyList(6)
for i in l:
    print(i)

