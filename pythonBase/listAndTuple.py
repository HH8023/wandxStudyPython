#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list  python内置的一种数据类型是列表 list是一种有序集合，
#       可以随时添加和删除其中的元素，相当于php的数组
aaa = ['11', '22', '33']
print('aaa的长度：', len(aaa), '集合有：', aaa)    # 3  len() 函数获取list元素的个数

# 获取最后一个元素，除了计算索引位置外，
# 还可以用 -1 做索引，直接获取最后一个元素，-2获取倒数第二个，-3获取倒数第三个

# append()    函数可以把元素追加到末尾
aaa.append('44')
print('aaa的长度：', len(aaa), 'append()追加到末尾之后集合有：', aaa)

# insert()   函数可以把元素插入到指定的位置，比如索引号为 1 的位置
aaa.insert(1, '55')
print('aaa的长度：', len(aaa), 'insert()插入索引号为1之后的集合有：', aaa)

# pop()  函数可以删除末尾的元素，pop(i) 其中 i 是索引的位置
aaa.pop()
print('aaa的长度：', len(aaa), 'pop()函数删除以后的集合有：', aaa)

# 赋值的话直接和php的数组赋值类似


# ============= tuple  =====================
# 另一种有序列表叫 元组 tuple  与list类似，
# 但是 tuple 一旦初始化就不能修改，比如同样是列出同学的名字
# 区别  tuple和list
#            tuple                                           list
# 1、定义使用小括号，eg aaa = ('1','2','3')，    1、定义使用中括号 , eg aaa = ['a','b','c']
# 2、定义的时候必须确定下来元素，之后不能修改    2、 定义的时候不用必须确定定义元素，之后也可以修改
# 3、定义一个元素是，必须加一个逗号，用来消除歧义   3、不用,相当于php的数组


# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print('l的集合', L)
print('打印Apple', L[0][0])

print('打印Python', L[1][1])
print('打印Lisa', L[2][2])