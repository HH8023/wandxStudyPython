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

# set 和dict类似，也是一组key，单不存储value，由于key不能重复，所以在set中，没有重复的key
s = set([1, 3, 2])
print('set的key', s)

s1 = set([1, 2, 3, 4, 3, 1, 6])
print('set的方法可以重复添加，但是不会有效果', s1)

s1.add(3)
print('给s1添加一个key为3的元素，但是因为原本就有，所以添加没有效果', s1)

s1.add(7)
print('添加s1的key为7的元素，原本s1里没有，所以会生效，s1.add(7)=', s1)

s1.remove(4)
print('通过remove()的方法进行删除元素，s1.remove()=', s1)

print('s1 & s的交集', s1 & s)
print('s1 | s的并集', s1 | s)


# 再议不可变对象
# 不变对象即相当于php的字符串类型，但是是不能改变的
a = ['c', 'b', 'a']
print('a的数组', a)
a.sort()
print('a进行sort()函数之后变为', a)

print('对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容，相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的')


# 函数
print('函数:')
print('函数调用，python不但可以非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用')

# 抽象
print('抽象:')
print('函数就是最基本的一种代码抽象的方式')

# 调用函数
print('调用函数:')
print('要调用函数，需要知道函数名称和参数，比如求绝对值的函数abs(),只有一个参数')
print('abs(100)的值为', abs(100))
print('abs(-20)的值为', abs(-20))
print('调用函数时，如果传入的参数数量不对，会报TypeError的错误')

# 数据类型转换
print('数据类型转换')
print('内置的常用的函数还有数据类型转换函数，比如int()函数可以把其他数据类型转换为整数')
print('int(\'123\')转换数据类型的值为', int('123'))
print('函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了个\'别名\'')

n1 = 255
n2 = 1000
print('n1 = 255的十六进制表示的字符串是', hex(n1))
print('n2 = 1000的十六进制表示的字符串是', hex(n2))


# 定义函数
print('定义函数')
print('在python中，定义一个函数要使用def语句，依次写出函数名，括号，括号中的参数和冒号：，然后在缩进块中编写函数体，函数的返回值用return语句返回')

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs(-2))

# 空函数
print('空函数')

print('如果想定义什么事也不做的空函数，可以用pass语句')