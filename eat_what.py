# -*- coding: utf-8 -*-

"""
Created on 2/27/21 10:44 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

from random import randint

arr = ["台菜", "意大利面", "泰国菜", "韩料"]

test = dict()
for _ in range(1000):
    curr = randint(0, 3)
    if curr not in test:
        test.setdefault(curr, 1)
    else:
        test[curr] += 1

curr = randint(0, 3)
print("明天吃{}".format(arr[curr]))
