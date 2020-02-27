#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 222
if age <= 18:
    print('your age is', age)
    print('未成年人')
elif 60 > age >= 18:
    print('your age is', age)
    print('成年人')
else:
    print('老年人')


# 练习题

height = 1.75
weight = 80.5
bmi = weight/(height**2)
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
else:
    print('严重肥胖')


# 循环  eg:
names = ('111', '222', '333')
for name in names:
    print('循环得出', name)

sum = 0
for x in (1, 2, 3, 4, 5):
    sum += x
print(sum)


# range()  函数，可以生成一个整数序列
a = list(range(5))
print('使用list(range(5))生成一个长度为5的有序集合为：', a)


# 使用while循环进行练习
# 计算100以内所有奇数之和
# sum = 0
n = 1
while n < 100:
    sum += n
    n = n + 2
print('计算100以内所有奇数之和', sum)


# dict 的用法，即对象数组  {key:value}形式
# 判断一个key是否存在有 2 种方法 一是通过 in 判断 key 是否存在 所下所示

d = {'a': 1}
print('b' in d, '判断 b 整个key是否在d中')

# 另一种是 get的方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('b'))  # '这个是不显示结果，只显示打印的字符串'
print(d.get('b'), -1)


print('和list比较，dict有以下几个特点：')
print('1、查找和插入的速度极快，不会随着key的增加而增加')
print('2、需要占用大量的内存，内存浪费多')
print('而list相反')
print('1、查找和插入的时间随着元素的增加而增加；')
print('2、占用空间小，浪费内存很少。')
print('所以，dict是用空间来换取时间的一种方法')


# set