#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

class cartesian(object):
    def __init__(self):
        self._data_list=[]

    def add_data(self, data=[]):
        self._data_list.append(data)

    def build(self):
        for item in itertools.product(*self._data_list):
            print(item)

if __name__ == "__main__":
    car=cartesian()
    car.add_data([1,2,3,4])
    car.add_data([5,6,7,8])
    car.add_data([9,10,11,12])
    car.build()
