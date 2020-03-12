#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('请定义一个函数quadratic(a,b,c),接收3个参数，返回一元二次方程：'
      'ax^2+bx+c=0'
      '的两个解')

import math

def quadratic(a, b, c):
    m = b*b-4*a*c
    if m >= 0:
        x = (-b+math.sqrt(m))/(2*a)
        y = (-b-math.sqrt(m))/(2*a)
        return x,y
    else:
        return 'no answer'

print(quadratic(2,3,1))