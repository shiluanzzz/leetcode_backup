# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 用rand7 实现rand10
import math
import random


def rand7(nums=0):
    if nums==0:
        return random.randint(1,7)
    else:
        return [random.randint(1,7) for i in range(nums)]
def rand10():

    while True:
        nums = rand7()*rand7()
        if nums<41:
            return 1+nums%10
        nums = (nums-40)*rand7()
        if nums<61:
            return 1+nums%10
        nums = (nums-60)*rand7()
        if nums<21:
            return 1+nums%10

def rand10_add():
    while True:
        nums = (rand7()-1)*7+rand7()
        if nums<41:
            return 1+nums%10
        nums = (nums-40-1)*7+rand7()
        if nums<61:
            return 1+nums%10
        nums = (nums-60-1)*7+rand7()
        if nums<21:
            return 1+nums%10


if __name__ == '__main__':
    print(rand7(10))